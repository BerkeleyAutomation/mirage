#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import trimesh
import open3d as o3d
from std_msgs.msg import Header
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

class PointCloudPublisher(Node):
    def __init__(self):
        self.is_ready_ = False
        super().__init__('ur5e_point_cloud_publisher')
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
        
        self.full_subscriber_ = self.create_subscription(PointCloud2,'full_pointcloud',self.fullPointcloudCallback,10)
        self.full_mask_image_publisher_ = self.create_publisher(Image,"full_mask_image",10)
        setup_mesh_timer = self.create_timer(timer_period,self.setupMeshes)
        self.is_ready_ = True
        
        #exit()
        #self.sync_ = TimeSynchronizer(self.subscribers_,10)
        #self.sync_.registerCallback(self.pointcloud_callback)

    def imageRawCallback(self,msg):
        if(self.is_ready_):
            self.original_image_ = self.cv_bridge_.imgmsg_to_cv2(msg,desired_encoding="passthrough")

    def fullPointcloudCallback(self,msg):
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
                print("I am the Senate")

    def setupMeshesFast(self):
        if(self.is_ready_):
            print(self.original_meshes_)
            full_open3d_mesh = None
            start_time = time.time()        
            for [filename,link_name,mesh,rpy_str,xyz_str] in self.links_info_:
                print(self.links_info_[0])
                resulting_mesh = self.setupMesh(filename,link_name,mesh,rpy_str,xyz_str)
                copied_mesh = o3d.geometry.TriangleMesh()
                copied_mesh.vertices = o3d.utility.Vector3dVector(np.asarray(resulting_mesh.vertices))
                copied_mesh.triangles = o3d.utility.Vector3iVector(np.asarray(resulting_mesh.triangles))
                if full_open3d_mesh is None:
                    full_open3d_mesh = copied_mesh
                else:
                    full_open3d_mesh += copied_mesh
            pcd = full_open3d_mesh.sample_points_uniformly(number_of_points=20000)
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
            end_time = time.time()

    def setupMeshes(self):
        if(self.is_ready_):
            print("HERE")
            
            open3d_mesh = None
            start_time = time.time()        
            for [filename,link_name,rpy_str,xyz_str] in self.links_info_:
                if open3d_mesh is None:
                    open3d_mesh = self.setupMesh(filename,link_name,rpy_str,xyz_str)
                else:
                    open3d_mesh += self.setupMesh(filename,link_name,rpy_str,xyz_str)
            print("Total time: " + str(time.time() - start_time))
            pcd = open3d_mesh.sample_points_uniformly(number_of_points=20000)
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
            end_time = time.time()

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

    def setupMeshFast(self,filename,link_name,open3d_mesh,rpy_str,xyz_str):
        if(self.is_ready_):
            rpy_str_list = rpy_str.split()
            rpy_floats = [float(x) for x in rpy_str_list]
            rpy_np = np.array(rpy_floats)
            xyz_str_list = xyz_str.split()
            xyz_floats = [float(x) for x in xyz_str_list]
            xyz_np = 1000 * np.array(xyz_floats)
            R2 = self.eulerToR(rpy_np)
            open3d_mesh.rotate(R2,[0,0,0])
            open3d_mesh.translate(xyz_np)
            
            # REQUIRES CAMERA TO BE IN GAZEBO SCENE
            while True:
                try:
                    t = self.tf_buffer_.lookup_transform(
                        "camera_color_optical_frame",
                        link_name,
                        rclpy.time.Time(),
                    )
                    t_matrix = self.transformStampedToMatrix(t.transform.rotation,t.transform.translation)
                    print(t_matrix,flush=True)
                    open3d_mesh.transform(t_matrix)
                    return open3d_mesh
                except TransformException as ex:
                    #TODO Change This
                    pass    

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
                    #print("Error finding transform between camera frame and " + str(link_name))

    def cameraInfoCallback(self,msg):
        if(self.is_ready_):
            self.camera_intrinsic_matrix_ = np.array([[msg.k[0],msg.k[1],msg.k[2],0],[msg.k[3],msg.k[4],msg.k[5],0],[msg.k[6],msg.k[7],msg.k[8],0]])
            self.image_shape_ = (msg.height,msg.width,3)

    def pointcloud_callback(self,msg1,msg2,msg3,msg4,msg5,msg6,msg7):
        if(self.is_ready_):
            if(self.camera_intrinsic_matrix_ is None):
                return
            else:
                msg1_pixels = self.getPixels(msg1)
                msg2_pixels = self.getPixels(msg2)
                msg3_pixels = self.getPixels(msg3)
                msg4_pixels = self.getPixels(msg4)
                msg5_pixels = self.getPixels(msg5)
                msg6_pixels = self.getPixels(msg6)
                msg7_pixels = self.getPixels(msg7)
                all_pixels = np.vstack((msg1_pixels,msg2_pixels,msg3_pixels,msg4_pixels,msg5_pixels,msg6_pixels,msg7_pixels))
                mask_image = np.zeros(self.image_shape_, dtype=np.uint8)
                white_color = (255,255,255)
                for coord in all_pixels:
                    x,y = coord
                    mask_image[round(y),round(x)] = white_color
                #mask_image = cv2.convertScaleAbs(mask_image, alpha=(255.0/65535.0))
                ros_mask_image = self.cv_bridge_.cv2_to_imgmsg(mask_image,encoding="bgr8")
                self.mask_image_publisher_.publish(ros_mask_image)

    def getPixels(self,msg):
        if(self.is_ready_):
            msg_data = point_cloud2.read_points(msg)
            msg_data = np.array([[item.tolist() for item in row] for row in msg_data])
            depth_data = msg_data[:,2]
            msg_data_homogenous = np.hstack((msg_data,np.ones((msg_data.shape[0],1))))
            pixel_data_homogenous = np.dot(self.camera_intrinsic_matrix_,msg_data_homogenous.T).T
            pixel_data = pixel_data_homogenous[:,:2] / pixel_data_homogenous[:,2:]
            return pixel_data, depth_data

    def createTransform(self,rpy_str,xyz_str):
        if(self.is_ready_):
            rpy_array = rpy_str.split(' ')
            xyz_array = xyz_str.split(' ')
            roll = float(rpy_array[0])
            pitch = float(rpy_array[1])
            yaw = float(rpy_array[2])
            x = float(xyz_array[0])
            y = float(xyz_array[1])
            z = float(xyz_array[2])

            rotation_x = np.array([[1, 0, 0],
                            [0, math.cos(roll), -math.sin(roll)],
                            [0, math.sin(roll), math.cos(roll)]])

            rotation_y = np.array([[math.cos(pitch), 0, math.sin(pitch)],
                                [0, 1, 0],
                                [-math.sin(pitch), 0, math.cos(pitch)]])

            rotation_z = np.array([[math.cos(yaw), -math.sin(yaw), 0],
                                [math.sin(yaw), math.cos(yaw), 0],
                                [0, 0, 1]])

            rotation_matrix = np.dot(rotation_z, np.dot(rotation_y, rotation_x))
            translation_vector = np.array([[x],[y],[z]])
            transform_matrix = np.concatenate((rotation_matrix,translation_vector),axis=1)
            transform_matrix = np.concatenate((transform_matrix,np.array([[0,0,0,1]])),axis=0)
            return transform_matrix

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
    
    def debugTimerCallback(self,filename,link_name,publisher,publisher_camera,rpy_str,xyz_str):
        if(self.is_ready_):
            mesh_scene = trimesh.load(filename)
            mesh = trimesh.util.concatenate(tuple(trimesh.Trimesh(vertices=g.vertices, faces=g.faces)
                                                for g in mesh_scene.geometry.values()))
            # Convert Trimesh to Open3D TriangleMesh
            vertices = o3d.utility.Vector3dVector(mesh.vertices)
            triangles = o3d.utility.Vector3iVector(mesh.faces)
            open3d_mesh = o3d.geometry.TriangleMesh(vertices, triangles)
            # pcd = open3d_mesh.sample_points_uniformly(number_of_points=100000)
            # pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points) / 1000)
            # pcd_data = np.asarray(pcd.points)
            # if(link_name == "base_link_inertia"):
            #     pcd_data = pcd_data[:,[0,2,1]]
            #     pcd_data[:,1] *= -1
            # elif(link_name == "shoulder_link"):
            #     # R = np.array([[-1,0,0],[0,0,1],[0,1,0]])
            #     # open3d_mesh.rotate(R,[0,0,0])
            #     # # print("RPY")
            #     # # print(rpy_str)
            #     # # print("XYZ Str")
            #     # # print(xyz_str)
            #     # rpy_str_list = rpy_str.split()
            #     # rpy_floats = [float(x) for x in rpy_str_list]
            #     # rpy_np = np.array(rpy_floats)
            #     # # print("RPY NUMPY")
            #     # # print(rpy_np)
            #     # R2 = pcd.get_rotation_matrix_from_xyz(rpy_np)
            #     # # print("We have R2 with us")
            #     # # print(R2)
            #     # open3d_mesh.rotate(R2,[0,0,0])
            #     # pcd = open3d_mesh.sample_points_uniformly(number_of_points=100000)
            #     # pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points) / 1000)
            #     # pcd_data = np.asarray(pcd.points)
            #     # #pcd_data = pcd_data[:,[0,2,1]]
            #     # #pcd_data[:,0] *= -1

            #     R = np.array([[-1,0,0],[0,0,1],[0,1,0]])
            #     open3d_mesh.rotate(R,[0,0,0])
            #     # print("RPY")
            #     # print(rpy_str)
            #     # print("XYZ Str")
            #     # print(xyz_str)
            #     rpy_str_list = rpy_str.split()
            #     rpy_floats = [float(x) for x in rpy_str_list]
            #     rpy_np = np.array(rpy_floats)
            #     xyz_str_list = xyz_str.split()
            #     xyz_floats = [float(x) for x in xyz_str_list]
            #     xyz_np = 1000 * np.array(xyz_floats)
            #     print("XYZ NUMPY")
            #     print(xyz_np)
            #     R21 = pcd.get_rotation_matrix_from_xyz(rpy_np)
            #     print("We have R21 with us")
            #     print(R21)
            #     R22 = pcd.get_rotation_matrix_from_xzy(rpy_np)
            #     print("We have R22 with us")
            #     print(R22)
            #     R23 = pcd.get_rotation_matrix_from_yxz(rpy_np)
            #     print("We have R23 with us")
            #     print(R23)
            #     R24 = pcd.get_rotation_matrix_from_yzx(rpy_np)
            #     print("We have R24 with us")
            #     print(R24)
            #     R25 = pcd.get_rotation_matrix_from_zxy(rpy_np)
            #     print("We have R25 with us")
            #     print(R25)
            #     R26 = pcd.get_rotation_matrix_from_zyx(rpy_np)
            #     print("We have R26 with us")
            #     print(R26)
            #     R2 = self.eulerToR(rpy_np)
            #     print("We have R2 with us")
            #     print(R2)
            #     open3d_mesh.rotate(R2,[0,0,0])
            #     open3d_mesh.translate(xyz_np)
            #     pcd = open3d_mesh.sample_points_uniformly(number_of_points=100000)
            #     pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points) / 1000)
            #     pcd_data = np.asarray(pcd.points)
            # elif(link_name == "upper_arm_link"):
            #     R = np.array([[-1,0,0],[0,0,1],[0,1,0]])
            #     open3d_mesh.rotate(R,[0,0,0])
            #     # print("RPY")
            #     # print(rpy_str)
            #     # print("XYZ Str")
            #     # print(xyz_str)
            #     rpy_str_list = rpy_str.split()
            #     rpy_floats = [float(x) for x in rpy_str_list]
            #     rpy_np = np.array(rpy_floats)
            #     xyz_str_list = xyz_str.split()
            #     xyz_floats = [float(x) for x in xyz_str_list]
            #     xyz_np = 1000 * np.array(xyz_floats)
            #     print("XYZ NUMPY")
            #     print(xyz_np)
            #     R21 = pcd.get_rotation_matrix_from_xyz(rpy_np)
            #     print("We have R21 with us")
            #     print(R21)
            #     R22 = pcd.get_rotation_matrix_from_xzy(rpy_np)
            #     print("We have R22 with us")
            #     print(R22)
            #     R23 = pcd.get_rotation_matrix_from_yxz(rpy_np)
            #     print("We have R23 with us")
            #     print(R23)
            #     R24 = pcd.get_rotation_matrix_from_yzx(rpy_np)
            #     print("We have R24 with us")
            #     print(R24)
            #     R25 = pcd.get_rotation_matrix_from_zxy(rpy_np)
            #     print("We have R25 with us")
            #     print(R25)
            #     R26 = pcd.get_rotation_matrix_from_zyx(rpy_np)
            #     print("We have R26 with us")
            #     print(R26)
            #     R2 = self.eulerToR(rpy_np)
            #     print("We have R2 with us")
            #     print(R2)
            #     open3d_mesh.rotate(R2,[0,0,0])
            #     open3d_mesh.translate(xyz_np)
            #     pcd = open3d_mesh.sample_points_uniformly(number_of_points=100000)
            #     pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points) / 1000)
            #     pcd_data = np.asarray(pcd.points)
            # elif(link_name == "forearm_link"):
            #     R = np.array([[-1,0,0],[0,0,1],[0,1,0]])
            #     open3d_mesh.rotate(R,[0,0,0])
            #     rpy_str_list = rpy_str.split()
            #     rpy_floats = [float(x) for x in rpy_str_list]
            #     rpy_np = np.array(rpy_floats)
            #     xyz_str_list = xyz_str.split()
            #     xyz_floats = [float(x) for x in xyz_str_list]
            #     xyz_np = 1000 * np.array(xyz_floats)
            #     print("XYZ NUMPY")
            #     print(xyz_np)
            #     R2 = self.eulerToR(rpy_np)
            #     print("We have R2 with us")
            #     print(R2)
            #     open3d_mesh.rotate(R2,[0,0,0])
            #     open3d_mesh.translate(xyz_np)
            #     pcd = open3d_mesh.sample_points_uniformly(number_of_points=100000)
            #     pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points) / 1000)
            #     pcd_data = np.asarray(pcd.points)
            #     #pcd_data = pcd_data[:,[1,0,2]]
            #     #pcd_data[:,0] *= -1

            R = np.array([[-1,0,0],[0,0,1],[0,1,0]])
            open3d_mesh.rotate(R,[0,0,0])
            rpy_str_list = rpy_str.split()
            rpy_floats = [float(x) for x in rpy_str_list]
            rpy_np = np.array(rpy_floats)
            xyz_str_list = xyz_str.split()
            xyz_floats = [float(x) for x in xyz_str_list]
            xyz_np = 1000 * np.array(xyz_floats)
            R2 = self.eulerToR(rpy_np)
            open3d_mesh.rotate(R2,[0,0,0])
            open3d_mesh.translate(xyz_np)
            try:
                t = self.tf_buffer_.lookup_transform(
                    "camera_color_optical_frame",
                    link_name,
                    rclpy.time.Time()
                )
                t_matrix = self.transformStampedToMatrix(t.transform.rotation,t.transform.translation)
                open3d_mesh.transform(t_matrix)
            except TransformException as ex:
                print("Tough")
                return
            pcd = open3d_mesh.sample_points_uniformly(number_of_points=100)
            pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points) / 1000)
            pcd_data = np.asarray(pcd.points)

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
            publisher.publish(point_cloud_msg)

    def timerCallback(self,filename,link_name,publisher,rpy_str,xyz_str):
        if(self.is_ready_):
            mesh = trimesh.load(filename)
            transform_matrix = self.createTransform(rpy_str,xyz_str)
            o3d_mesh = None
            pcds = []
            points = None
            R = np.array([[1,0,0],[0,0,-1],[0,1,0]])
            R2 = np.array([[-1,0,0],[0,-1,0],[0,0,1]])
            for item in mesh.geometry:
                o3d_mesh = mesh.geometry[item].as_open3d
                #o3d_mesh = o3d_mesh.rotate(R)
                pcd = o3d_mesh.sample_points_uniformly(number_of_points=100000)
                if points is None:
                    points = np.asarray(pcd.points)
                else:
                    points = np.concatenate((points,pcd.points),axis=0)
                pcds.append(pcd)
            new_pcd = o3d.geometry.PointCloud()
            new_pcd.points = o3d.utility.Vector3dVector(points)
            center_translation = -new_pcd.get_center()
            new_pcd = new_pcd.translate(center_translation)
            new_pcd = new_pcd.rotate(R)
            new_pcd = new_pcd.rotate(R2)
            
            new_pcd = new_pcd.transform(transform_matrix)
            #print(transform_matrix)
            #mesh = mesh.apply_transform(transform_matrix)
            # vertices = None
            # for item in mesh.geometry:
            #     if vertices is None:
            #         vertices = mesh.geometry[item].vertices
            #     else:
            #         vertices = np.concatenate((vertices,mesh.geometry[item].vertices),axis=0)

            # # Create a visualization window
            # pcd = o3d.geometry.PointCloud()
            # pcd.points = o3d.utility.Vector3dVector(vertices)
            # R = np.array([[1,0,0],[0,0,-1],[0,1,0]])
            # R2 = np.array([[-1,0,0],[0,-1,0],[0,0,1]])
            # pcd = pcd.rotate(R)
            # pcd = pcd.rotate(R2)
            #pcd = pcd.transform(transform_matrix)
            # Pointcloud still rotated incorrectly
            #additional_transform = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
            #pcd = pcd.transform(additional_transform)
            pcd_data = np.asarray(new_pcd.points) / 1000
            point_cloud_msg = PointCloud2()
            point_cloud_msg.header = Header()
            point_cloud_msg.header.frame_id = link_name
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

            publisher.publish(point_cloud_msg)
        #     self.dae_paths_ = glob.glob(self.dae_main_path_ + '/*.dae')
        #     self.publishers_ = []
        #     self.timers_ = []
        #     timer_period = 0.5
        #     for dae_path in self.dae_paths_:
        #         ur5_part = dae_path[dae_path.rfind('/')+1:dae_path.rind('.')]
        #         publisher = self.create_publisher(PointCloud2,ur5_part+'_pointcloud',10)
        #         self.publishers_.append(publisher)
        #         timer = self.create_timer(timer_period,partial(self.timerCallback,param1=dae_path))

        #     self.ur5_parts_ = ['base','forearm','shoulder','upperarm','wrist1','wrist2','wrist3']
        #     self.publishers_ = []
        #     self.timers_ = []
        #     timer_period = 0.5
        #     for ur5_part in self.ur5_parts_:
        #         publisher = self.create_publisher(PointCloud2,ur5_part+'_pointcloud',10)
        #         self.publishers_.append(publisher)
        #         timer = self.create_timer(timer_period,partial(self.timerCallback,param1=ur5_part))
        #     self.publisher_ = self.create_publisher(PointCloud2, '/base_pointcloud', 10)
        #     timer_period = 0.5  # seconds
        #     self.timer = self.create_timer(timer_period, self.timer_callback)
        #     self.i = 0
            
        #     print(glob.glob(self.dae_main_path_ + '/*.dae'))
        #     exit()
        #     self.base_filepath_ = "/home/benchturtle/cross_embodiment_ws/src/gazebo_env/meshes/ur5e/visual/base.dae"

        # def timer_callback(self):
        #     mesh = trimesh.load(self.base_filepath_)
        #     vertices = None
        #     for item in mesh.geometry:
        #         if vertices is None:
        #             vertices = mesh.geometry[item].vertices
        #         else:
        #             vertices = np.concatenate((vertices,mesh.geometry[item].vertices),axis=0)

        #     # Create a visualization window
        #     pcd = o3d.geometry.PointCloud()
        #     pcd.points = o3d.utility.Vector3dVector(vertices)

        #     pcd_data = np.asarray(pcd.points) / 1000
        #     np.savetxt('data.csv',pcd_data,delimiter=", ")
        #     point_cloud_msg = PointCloud2()
        #     point_cloud_msg.header = Header()
        #     point_cloud_msg.header.frame_id = 'base_link_inertia'
        #     fields =[PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
        #     PointField(name='z', offset=4, datatype=PointField.FLOAT32, count=1),
        #     PointField(name='y', offset=8, datatype=PointField.FLOAT32, count=1),
        #     ]
        #     point_cloud_msg.height = 1
        #     point_cloud_msg.width = len(pcd_data)
        #     point_cloud_msg.fields = fields
        #     point_cloud_msg.is_bigendian = False
        #     point_cloud_msg.point_step = 3 * 4
        #     point_cloud_msg.row_step = point_cloud_msg.point_step * len(pcd_data)
        #     point_cloud_msg.is_dense = True
        #     point_cloud_msg.data = bytearray(pcd_data.astype('float32').tobytes())

        #     self.publisher_.publish(point_cloud_msg)
        #     self.i += 1

def main(args=None):
    rclpy.init(args=args)

    point_cloud_publisher = PointCloudPublisher()

    rclpy.spin(point_cloud_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    point_cloud_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()