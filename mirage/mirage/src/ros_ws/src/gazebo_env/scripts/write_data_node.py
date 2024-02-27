#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import trimesh
import open3d as o3d
from std_msgs.msg import Header, Float64MultiArray
from sensor_msgs.msg import PointCloud2, PointField, CameraInfo, Image
import numpy as np
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
import os
import glob
import subprocess
import xml.etree.ElementTree as ET
from functools import partial
import math
from message_filters import TimeSynchronizer, Subscriber
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from sensor_msgs_py import point_cloud2
import cv2
from cv_bridge import CvBridge
import time
from input_filenames_msg.msg import InputFiles, InputFilesData
from sensor_msgs.msg import JointState
from tracikpy import TracIKSolver
from mdh.kinematic_chain import KinematicChain
from mdh import UnReachable
import kinpy as kp
from geometry_msgs.msg import Vector3, Quaternion

class WriteData(Node):
    def __init__(self):
        super().__init__('write_data_node')
        self.is_ready_ = False
        self.thetas_ = None
        self.panda_urdf_ = "/home/benchturtle/cross_embodiment_ws/src/gazebo_env/description/urdf/panda_arm_hand_only_ik.urdf"
        self.panda_solver_ = TracIKSolver(self.panda_urdf_,"world","panda_hand")
        self.ur5e_urdf_ = "/home/benchturtle/cross_embodiment_ws/src/gazebo_env/description/urdf/ur5e_nvidia_with_gripper_solo_ik.urdf"
        self.chain_ = kp.build_chain_from_urdf(open("/home/benchturtle/cross_embodiment_ws/src/gazebo_env/description/urdf/ur5e_nvidia_with_gripper_solo_ik.urdf").read())
        self.ur5e_solver_ = TracIKSolver(self.ur5e_urdf_,"world","tool0")
        self.camera_to_base_link_ = np.array([[-0.707,0.707,0,0],
                                              [0.408 , 0.408, -0.816,  0],
                                              [-0.577, -0.577 ,-0.577 , 2598],
                                              [0,0,0,1]])
        self.ur5e_joint_command_publisher_ = self.create_publisher(Float64MultiArray,'/joint_commands',1)
        self.ur5e_joint_state_publisher_ = self.create_publisher(
            JointState,
            '/joint_states',  # Topic name for /joint_states
            1)
        self.subscription_ = self.create_subscription(
            InputFiles,
            'input_files',
            self.listenerCallback,
            1)
        self.subscription_data_ = self.create_subscription(
            InputFilesData,
            'input_files_data',
            self.listenerCallbackData,
            1)
        self.joint_state_msg = JointState()
        self.q_init_ = np.zeros(self.ur5e_solver_.number_of_joints)

        self.urdf_xacro_path_ = os.path.join(FindPackageShare(package="gazebo_env").find("gazebo_env"),"urdf","ur5e_nvidia_with_gripper_solo.urdf.xacro")
        xacro_command = "ros2 run xacro xacro " + self.urdf_xacro_path_
        xacro_subprocess = subprocess.Popen(
            xacro_command,
            shell=True,
            stdout=subprocess.PIPE,
        )
        urdf_string = ""
        while True:
            line = xacro_subprocess.stdout.readline()
            if line:
                line_byte = line.strip()
                line = line_byte.decode("utf-8")
                urdf_string += line
            else:
                break
        
        root = ET.fromstring(urdf_string)
        self.publishers_ = []
        self.subscribers_ = []
        self.timers_ = []
        self.tf_buffer_ = Buffer()
        self.tf_listener_ = TransformListener(self.tf_buffer_, self)
        self.camera_intrinsic_matrix_ = None
        self.image_shape_ = None
        self.original_image_ = None
        self.camera_intrinsic_subscription_ = self.create_subscription(
            CameraInfo,
            '/camera/camera_info',
            self.cameraInfoCallback,
            10
        )
        self.camera_raw_subscription_ = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.imageRawCallback,
            10
        )
        self.cv_bridge_ = CvBridge()
        self.mask_image_publisher_ = self.create_publisher(Image,"mask_image",10)
        self.just_robot_image_publisher_ = self.create_publisher(Image,"plain_ur5_image",10)
        
        timer_period = 0.5
        self.links_info_ = []
        self.original_meshes_ = []
        for link in root.iter('link'):
            element_name1 = "visual"
            found_element1 = link.find(".//" + element_name1)
            element_name2 = "geometry"
            found_element2 = link.find(".//" + element_name2)
            element_name3 = "mesh"
            found_element3 = link.find(".//" + element_name3)
            if (found_element1 is not None) and (found_element2 is not None) and (found_element3 is not None):
                link_name = link.attrib.get('name')
                for visual in link.iter("visual"):
                    origin_element = visual.find(".//origin")
                    rpy_str = origin_element.attrib.get('rpy')
                    xyz_str = origin_element.attrib.get('xyz')
                    for geometry in visual.iter("geometry"):
                        for mesh in geometry.iter("mesh"):
                            filename = mesh.attrib.get('filename')[7:]
                            #publisher = self.create_publisher(PointCloud2,link_name+"_pointcloud",10)
                            #publisher_camera = self.create_publisher(PointCloud2,link_name+"_pointcloud_camera",10)
                            #self.publishers_.append(publisher)
                            #self.publishers_.append(publisher_camera)
                            #subscriber = Subscriber(self,PointCloud2,link_name+"_pointcloud")
                            #self.subscribers_.append(subscriber)
                            mesh = self.prelimMeshFast(filename)
                            self.original_meshes_.append(mesh)
                            self.links_info_.append([filename,link_name,rpy_str,xyz_str])
                            #timer = self.create_timer(timer_period,partial(self.debugTimerCallback,filename,link_name,publisher,publisher_camera,rpy_str,xyz_str))
                            #self.timers_.append(timer)
        
        self.full_publisher_ = self.create_publisher(PointCloud2,"full_pointcloud",10)
        self.inpainted_publisher_ = self.create_publisher(Image,"inpainted_image",1)
        #self.full_subscriber_ = self.create_subscription(PointCloud2,'full_pointcloud',self.fullPointcloudCallback,10)
        self.full_mask_image_publisher_ = self.create_publisher(Image,"full_mask_image",10)
        self.is_ready_ = True
    
    def cameraInfoCallback(self,msg):
        if(self.is_ready_):
            self.camera_intrinsic_matrix_ = np.array([[msg.k[0],msg.k[1],msg.k[2],0],[msg.k[3],msg.k[4],msg.k[5],0],[msg.k[6],msg.k[7],msg.k[8],0]])
            self.image_shape_ = (msg.height,msg.width,3)

    def imageRawCallback(self,msg):
        if(self.is_ready_):
            self.original_image_ = self.cv_bridge_.imgmsg_to_cv2(msg,desired_encoding="passthrough")

    def prelimMeshFast(self,filename):
        # RPY is in ZYX I'm pretty sure
        mesh_scene = trimesh.load(filename)
        mesh = trimesh.util.concatenate(tuple(trimesh.Trimesh(vertices=g.vertices, faces=g.faces)
                                            for g in mesh_scene.geometry.values()))
        # Convert Trimesh to Open3D TriangleMesh
        vertices = o3d.utility.Vector3dVector(mesh.vertices)
        triangles = o3d.utility.Vector3iVector(mesh.faces)
        open3d_mesh = o3d.geometry.TriangleMesh(vertices, triangles)
        test_pcd = open3d_mesh.sample_points_uniformly(number_of_points=500)
        test_pcd_data = np.asarray(test_pcd.points)
        diff = max(np.max(test_pcd_data[:, 0]) - np.min(test_pcd_data[:, 0]),np.max(test_pcd_data[:, 1]) - np.min(test_pcd_data[:, 1]),np.max(test_pcd_data[:, 2]) - np.min(test_pcd_data[:, 2]))
        # Checks to make sure units are in mm instead of m (We convert uniformly to meters later)
        if(diff < 1):
            open3d_mesh.vertices = o3d.utility.Vector3dVector(np.asarray(open3d_mesh.vertices) * 1000)
        else:
            R = np.array([[-1,0,0],[0,0,1],[0,1,0]])
            open3d_mesh.rotate(R,[0,0,0])
        return open3d_mesh
    
    def getPixels(self,msg):
        if(self.is_ready_):
            msg_data = point_cloud2.read_points(msg)
            msg_data = np.array([[item.tolist() for item in row] for row in msg_data])
            depth_data = msg_data[:,2]
            msg_data_homogenous = np.hstack((msg_data,np.ones((msg_data.shape[0],1))))
            pixel_data_homogenous = np.dot(self.camera_intrinsic_matrix_,msg_data_homogenous.T).T
            pixel_data = pixel_data_homogenous[:,:2] / pixel_data_homogenous[:,2:]
            return pixel_data, depth_data
        
    def inpainting(self,rgbd_file,seg_file,gazebo_rgb,gazebo_depth):
        
        # TODO(kush): Clean this up to use actual data, not file names
        if type(rgbd_file) == str:
            rgbd = np.load(rgbd_file)
            seg = cv2.imread(seg_file,0)
        else:
            rgbd = rgbd_file
            seg = seg_file
            seg = seg.astype(np.uint8)

        _, seg = cv2.threshold(seg, 128, 255, cv2.THRESH_BINARY)
        color_image = rgbd[:,:,0:3]
        color_image = cv2.cvtColor(color_image,cv2.COLOR_BGR2RGB)
        depth_image = rgbd[:,:,-1]
        depth_image = depth_image[:,:,np.newaxis]
        rgbd_image = np.concatenate((color_image,depth_image),axis=2)
        inverted_mask = cv2.bitwise_not(seg)
        masked_rgbd_image = cv2.bitwise_and(rgbd_image,rgbd_image,mask=inverted_mask)
        masked_rgb_image = masked_rgbd_image[:,:,0:3]
        masked_depth_image = masked_rgbd_image[:,:,-1]

        joined_depth = np.concatenate((gazebo_depth[np.newaxis],masked_depth_image[np.newaxis]),axis=0)
        joined_depth[joined_depth == 0] = 1000
        joined_depth_argmin = np.argmin(joined_depth,axis=0)
        attempt = masked_rgb_image * joined_depth_argmin[:,:,np.newaxis]
        inverted_joined_depth_argmin = 1 - joined_depth_argmin
        attempt2 = gazebo_rgb * inverted_joined_depth_argmin[:,:,np.newaxis]
        inpainted_image = attempt + attempt2
        image_8bit = cv2.convertScaleAbs(inpainted_image)  # Convert to 8-bit image
        inpainted_image_msg = self.cv_bridge_.cv2_to_imgmsg(image_8bit,encoding="bgr8")
        self.inpainted_publisher_.publish(inpainted_image_msg)

    def fullPointcloudCallback(self,msg,depth_file,segmentation):
        if(self.is_ready_):
            if(self.camera_intrinsic_matrix_ is None):
                return
            all_pixels,depth_data = self.getPixels(msg)
            mask_image = np.zeros(self.image_shape_, dtype=np.uint8)
            depth_image = np.zeros(self.image_shape_[:2], dtype=np.float64)
            white_color = (255,255,255)
            i = 0
            for coord in all_pixels:
                x,y = coord
                # TODO Change 5 pixel hardcoded offset. Sorry Professor Chen, I'll do better :)
                mask_image[round(y),round(x)-5] = white_color
                depth_image[round(y),round(x)-5] = depth_data[i]
                i += 1
            np.save('/home/benchturtle/gazebo_robot_depth.npy',depth_image)
            old_mask_image = mask_image
            mask_image = cv2.cvtColor(mask_image, cv2.COLOR_RGB2GRAY)
            _, mask_image = cv2.threshold(mask_image, 128, 255, cv2.THRESH_BINARY)
            if(self.original_image_ is not None):
                mask_image = cv2.resize(mask_image, (mask_image.shape[1], mask_image.shape[0]))

                # Create a new image with the same size as the original image
                gazebo_masked_image = np.zeros_like(self.original_image_)

                # Apply the gazebo_mask to the original image using element-wise multiplication
                gazebo_masked_image = cv2.bitwise_and(self.original_image_, self.original_image_, mask=mask_image)
                gazebo_masked_image[:, :, 0], gazebo_masked_image[:, :, 2] = gazebo_masked_image[:, :, 2].copy(), gazebo_masked_image[:, :, 0].copy()
                cv2.imwrite('/home/benchturtle/gazebo_robot_only.jpg',gazebo_masked_image)
                cv2.imwrite('/home/benchturtle/gazebo_mask.jpg',mask_image)
                #mask_image = cv2.convertScaleAbs(mask_image, alpha=(255.0/65535.0))
                ros_mask_image = self.cv_bridge_.cv2_to_imgmsg(old_mask_image,encoding="bgr8")
                self.full_mask_image_publisher_.publish(ros_mask_image)
                self.inpainting(depth_file,segmentation,gazebo_masked_image,depth_image)
                print("I am the Senate")

    def setupMesh(self,filename,link_name,rpy_str,xyz_str):
        if(self.is_ready_):
            # RPY is in ZYX I'm pretty sure
            mesh_scene = trimesh.load(filename)
            mesh = trimesh.util.concatenate(tuple(trimesh.Trimesh(vertices=g.vertices, faces=g.faces)
                                                for g in mesh_scene.geometry.values()))
            # Convert Trimesh to Open3D TriangleMesh
            vertices = o3d.utility.Vector3dVector(mesh.vertices)
            triangles = o3d.utility.Vector3iVector(mesh.faces)
            open3d_mesh = o3d.geometry.TriangleMesh(vertices, triangles)
            test_pcd = open3d_mesh.sample_points_uniformly(number_of_points=500)
            test_pcd_data = np.asarray(test_pcd.points)
            diff = max(np.max(test_pcd_data[:, 0]) - np.min(test_pcd_data[:, 0]),np.max(test_pcd_data[:, 1]) - np.min(test_pcd_data[:, 1]),np.max(test_pcd_data[:, 2]) - np.min(test_pcd_data[:, 2]))
            # Checks to make sure units are in mm instead of m (We convert uniformly to meters later)
            if(diff < 1):
                open3d_mesh.vertices = o3d.utility.Vector3dVector(np.asarray(open3d_mesh.vertices) * 1000)
            else:
                R = np.array([[-1,0,0],[0,0,1],[0,1,0]])
                open3d_mesh.rotate(R,[0,0,0])
            #open3d_mesh = fast_mesh
            start_time = time.time()
            rpy_str_list = rpy_str.split()
            rpy_floats = [float(x) for x in rpy_str_list]
            rpy_np = np.array(rpy_floats)
            xyz_str_list = xyz_str.split()
            xyz_floats = [float(x) for x in xyz_str_list]
            xyz_np = 1000 * np.array(xyz_floats)
            R2 = self.eulerToR(rpy_np)
            open3d_mesh.rotate(R2,[0,0,0])
            open3d_mesh.translate(xyz_np)
            
            transform = self.fks_[link_name]

            position = Vector3()
            quaternion = Quaternion()
            position.x = transform.pos[0]
            position.y = transform.pos[1]
            position.z = transform.pos[2]

            quaternion.w = transform.rot[0]
            quaternion.x = transform.rot[1]
            quaternion.y = transform.rot[2]
            quaternion.z = transform.rot[3]

            robot_fk = self.transformStampedToMatrix(quaternion,position)
            t_matrix = self.camera_to_base_link_ @ robot_fk
            open3d_mesh.transform(t_matrix)
            return open3d_mesh
            
            # REQUIRES CAMERA TO BE IN GAZEBO SCENE
            while True:
                try:
                    t = self.tf_buffer_.lookup_transform(
                        "camera_color_optical_frame",
                        link_name,
                        rclpy.time.Time(),
                    )
                    t_matrix = self.transformStampedToMatrix(t.transform.rotation,t.transform.translation)
                    open3d_mesh.transform(t_matrix)
                    return open3d_mesh
                except TransformException as ex:
                    #TODO Change This
                    pass

    def transformStampedToMatrix(self,rotation,translation):
        if(self.is_ready_):
            q0 = rotation.w
            q1 = rotation.x
            q2 = rotation.y
            q3 = rotation.z
            # First row of the rotation matrix
            r00 = 2 * (q0 * q0 + q1 * q1) - 1
            r01 = 2 * (q1 * q2 - q0 * q3)
            r02 = 2 * (q1 * q3 + q0 * q2)
            
            # Second row of the rotation matrix
            r10 = 2 * (q1 * q2 + q0 * q3)
            r11 = 2 * (q0 * q0 + q2 * q2) - 1
            r12 = 2 * (q2 * q3 - q0 * q1)
            
            # Third row of the rotation matrix
            r20 = 2 * (q1 * q3 - q0 * q2)
            r21 = 2 * (q2 * q3 + q0 * q1)
            r22 = 2 * (q0 * q0 + q3 * q3) - 1
            t_matrix = np.array(
                [[r00, r01, r02,translation.x * 1000],
                [r10, r11, r12,translation.y * 1000],
                [r20, r21, r22,translation.z * 1000],
                [0,0,0,1]]
            )
            return t_matrix

    def setupMeshes(self,depth_file,segmentation):
        if(self.is_ready_):
            print("HERE")
            open3d_mesh = None
            start_time = time.time()        
            for [filename,link_name,rpy_str,xyz_str] in self.links_info_:
                if open3d_mesh is None:
                    open3d_mesh = self.setupMesh(filename,link_name,rpy_str,xyz_str)
                else:
                    open3d_mesh += self.setupMesh(filename,link_name,rpy_str,xyz_str)
            pcd = open3d_mesh.sample_points_uniformly(number_of_points=200000)
            pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points) / 1000)
            pcd_data = np.asarray(pcd.points)
            o3d.io.write_point_cloud('/home/benchturtle/ur5e.pcd',pcd)
            point_cloud_msg = PointCloud2()
            point_cloud_msg.header = Header()
            point_cloud_msg.header.frame_id = "camera_color_optical_frame"
            fields =[PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
            ]
            point_cloud_msg.height = 1
            point_cloud_msg.width = len(pcd_data)
            point_cloud_msg.fields = fields
            point_cloud_msg.is_bigendian = False
            point_cloud_msg.point_step = 3 * 4
            point_cloud_msg.row_step = point_cloud_msg.point_step * len(pcd_data)
            point_cloud_msg.is_dense = True
            point_cloud_msg.data = bytearray(pcd_data.astype('float32').tobytes())
            self.full_publisher_.publish(point_cloud_msg)
            self.fullPointcloudCallback(point_cloud_msg,depth_file,segmentation)

    def eulerToR(self,rpy_np):
        if(self.is_ready_):
            rotation_x = rpy_np[0]
            rotation_y = rpy_np[1]
            rotation_z = rpy_np[2]
            Rx = np.array([[1,0,0],[0,np.cos(rotation_x),-np.sin(rotation_x)],[0,np.sin(rotation_x),np.cos(rotation_x)]])
            Ry = np.array([[np.cos(rotation_y),0,np.sin(rotation_y)],[0,1,0],[-np.sin(rotation_y),0,np.cos(rotation_y)]])
            Rz = np.array([[np.cos(rotation_z),-np.sin(rotation_z),0],[np.sin(rotation_z),np.cos(rotation_z),0],[0,0,1]])
            R = np.matmul(Rz,Ry)
            R = np.matmul(R,Rx)
            return R
        
    def listenerCallback(self,msg):
        if self.is_ready_:
            start_time = time.time()
            depth_file = msg.depth_file
            segmentation = msg.segmentation
            joints = msg.joints
            f = open(joints)
            joint_array = f.read().split(' ')
            joint_array = [float(item) for item in joint_array ]

            f.close()
            ee_pose = self.panda_solver_.fk(np.array(joint_array))
            qout = self.ur5e_solver_.ik(ee_pose,qinit=np.zeros(self.ur5e_solver_.number_of_joints))#self.q_init_)
            self.q_init_ = qout
            # Hardcoded gripper
            qout_list = qout.tolist()
            qout_list.append(0.0)
            qout_msg = Float64MultiArray()
            qout_msg.data = qout_list
            self.ur5e_joint_command_publisher_.publish(qout_msg)
            self.joint_commands_callback(qout_msg)
            self.setupMeshes(depth_file,segmentation)
            end_time = time.time()
            print("Total time: " + str(end_time - start_time) + " s")

    def listenerCallbackData(self,msg):
        if self.is_ready_:
            start_time = time.time()
            depth_data = msg.depth_data

            segmentation_data = msg.segmentation_data
            depth_data_reshaped = np.array(depth_data) \
                            .reshape((segmentation_data.width, segmentation_data.height, 4))

            segmentation_data = self.cv_bridge_.imgmsg_to_cv2(segmentation_data)

            joints = msg.joints
            joint_array = joints

            ee_pose = self.panda_solver_.fk(np.array(joint_array))
            qout = self.ur5e_solver_.ik(ee_pose,qinit=np.zeros(self.ur5e_solver_.number_of_joints))#self.q_init_)
            self.q_init_ = qout
            # Hardcoded gripper
            qout_list = qout.tolist()
            qout_list.append(0.0)
            qout_msg = Float64MultiArray()
            qout_msg.data = qout_list
            self.ur5e_joint_command_publisher_.publish(qout_msg)
            self.joint_commands_callback(qout_msg)
            self.setupMeshes(depth_data_reshaped, segmentation_data)
            end_time = time.time()
            print("Total time: " + str(end_time - start_time) + " s")


    def joint_commands_callback(self, msg):
        # Fill the JointState message with data from the Float64MultiArray
        self.joint_state_msg.header.stamp = self.get_clock().now().to_msg()
        #self.joint_state_msg.name = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint","wrist_1_joint", "wrist_2_joint", "wrist_3_joint","robotiq_85_left_knuckle_joint","robotiq_85_right_knuckle_joint","robotiq_85_left_inner_knuckle_joint","robotiq_85_right_inner_knuckle_joint","robotiq_85_left_finger_tip_joint","robotiq_85_right_finger_tip_joint"]  # Replace with your joint names
        self.joint_state_msg.name = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint","wrist_1_joint", "wrist_2_joint", "wrist_3_joint","robotiq_85_left_knuckle_joint","robotiq_85_right_knuckle_joint","robotiq_85_left_inner_knuckle_joint","robotiq_85_right_inner_knuckle_joint","robotiq_85_left_finger_tip_joint","robotiq_85_right_finger_tip_joint"]  # Replace with your joint names
        gripper_val = msg.data[6]
        msg.data.append(gripper_val)
        msg.data.append(gripper_val)
        msg.data.append(gripper_val)
        msg.data.append(-gripper_val)
        msg.data.append(-gripper_val)
        #msg.data.append(gripper_val)
        #msg.data.append(gripper_val)
        # for i in range(5):
        #     if(i == 1 or i == 4):
        #         msg.data.append(gripper_val)
        #     else:
        #         msg.data.append(gripper_val)
        self.joint_state_msg.position = msg.data
        
        self.thetas_ = {key:value for key,value in zip(self.joint_state_msg.name,msg.data)}
        self.fks_ = self.chain_.forward_kinematics(self.thetas_)
        self.ur5e_joint_state_publisher_.publish(self.joint_state_msg)



    
def main(args=None):
    rclpy.init(args=args)

    write_data = WriteData()

    rclpy.spin(write_data)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    write_data.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()