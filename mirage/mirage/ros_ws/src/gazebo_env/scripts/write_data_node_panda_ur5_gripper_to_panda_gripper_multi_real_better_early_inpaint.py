#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import trimesh
from std_msgs.msg import Header, Float64MultiArray,Bool
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
from input_filenames_msg.msg import InputFilesRobosuite, InputFilesRobosuiteData, InputFilesRealData, InputFilesRealDataMulti, MultipleInpaintImages
from sensor_msgs.msg import JointState
from tracikpy import TracIKSolver
from mdh.kinematic_chain import KinematicChain
from mdh import UnReachable
from geometry_msgs.msg import Vector3, Quaternion
from scipy.spatial.transform import Rotation as R
from message_filters import ApproximateTimeSynchronizer, Subscriber
import pathlib


class WriteData(Node):
    def __init__(self):
        super().__init__('write_data_node')
        self.is_ready_ = False
        self.thetas_ = None
        self.debug_ = True
        self.float_image_ = False
        file_directory = pathlib.Path(__file__).parent.resolve()
        self.panda_panda_gripper_urdf_ = os.path.join(file_directory,'../../../../src/gazebo_env/description/urdf/panda_gripper_ik_real.urdf')        
        self.panda_panda_gripper_solver_ = TracIKSolver(self.panda_panda_gripper_urdf_,"panda_link0","panda_ee")
        self.panda_ur5_gripper_urdf_ = os.path.join(file_directory,'../../../../src/gazebo_env/description/urdf/panda_ur5_gripper_ik_real.urdf')
        # self.chain_ = kp.build_chain_from_urdf(open(self.panda_panda_gripper_urdf_).read())
        self.panda_ur5_gripper_solver_ = TracIKSolver(self.panda_ur5_gripper_urdf_,"panda_with_ur5_gripper_link0","ur5_ee_gripper")

        # real_camera_link to world and then multiply translation by 1000
        # self.camera_to_world_ = np.array([[0,1,0,0],
        #                                       [0.258,0,-0.966,989],
        #                                       [-0.966,0,-0.258,1919],
        #                                       [0,0,0,1]])
        self.camera_to_world_ = np.array([[0.000,  1.000, 0.000 , -1],
                                          [0.706, 0.000 ,-0.708,  603],
                                          [-0.708,  0.000, -0.706 , 1307],
                                          [0,0,0,1]])
        
        self.robosuite_intrinsic_matrix_ = np.array([[101.39696962,   0.        , 42.        ],
       [  0.        , 101.39696962, 42.        ],
       [  0.        ,   0.        ,   1.        ]])
        self.ur5_and_panda_joint_command_publisher_ = self.create_publisher(Float64MultiArray,'/joint_commands',1)
        self.panda_joint_state_publisher_ = self.create_publisher(
            JointState,
            '/joint_states',  # Topic name for /joint_states
            1)
        self.joint_state_subscriber_ = Subscriber(self,JointState,'/gazebo_joint_states')
        self.ur5_rgb_image_subscriber_ = Subscriber(self,Image,'/ur5_camera/image_raw')
        self.ur5_depth_image_subscriber_ = Subscriber(self,Image,'/ur5_camera/depth/image_raw')
        self.panda_rgb_image_subscriber_ = Subscriber(self,Image,'/panda_camera/image_raw')
        self.panda_depth_image_subscriber_ = Subscriber(self,Image,'/panda_camera/depth/image_raw')
        self.gazebo_time_synchronizer_ = ApproximateTimeSynchronizer([self.joint_state_subscriber_,self.ur5_rgb_image_subscriber_,self.ur5_depth_image_subscriber_,self.panda_rgb_image_subscriber_,self.panda_depth_image_subscriber_],1,0.2)
        self.gazebo_time_synchronizer_.registerCallback(self.gazeboCallback)
        self.subscription_ = self.create_subscription(
            InputFilesRobosuite,
            '/input_files',
            self.listenerCallback,
            1)
        self.subscription_data_ = self.create_subscription(
            InputFilesRealDataMulti,
            'input_files_data_real',
            self.listenerCallbackOnlineDebug,
            1)
        self.joint_state_msg = JointState()

        #Harcoding start position
        self.q_init_ = np.array([-0.56332457,  0.06948572,  0.5227356,  -2.26363611, -0.11123186,  2.28321218, -0.09410787])
        
        self.publishers_ = []
        self.subscribers_ = []
        self.timers_ = []
        self.left_real_rgb_ = None
        self.right_real_rgb_ = None
        self.left_real_depth_ = None
        self.right_real_depth_ = None
        self.real_seg_ = None
        self.real_qout_list_ = None
        self.i_ = -1
        self.offline_ = False
        self.seg_file_ = None
        self.tf_buffer_ = Buffer()
        self.tf_listener_ = TransformListener(self.tf_buffer_, self)
        self.camera_intrinsic_matrix_ = None
        self.image_shape_ = None
        # REMEMBER TO HARDCODE THIS
        self.robosuite_image_shape_ = (84,84)
        self.camera_intrinsic_subscription_ = self.create_subscription(
            CameraInfo,
            '/camera/camera_info',
            self.cameraInfoCallback,
            1
        )
        self.camera_color_subscription_ = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.cameraCallback,
            1
        )

        self.ur5_left_rgb_ = None
        self.ur5_left_depth_ = None
        self.panda_left_rgb_ = None
        self.panda_left_depth_ = None
        self.ur5_left_camera_color_subscription_ = self.create_subscription(
            Image,
            '/ur5_left_camera/image_raw',
            self.ur5LeftRgbCallback,
            1
        )

        self.ur5_left_camera_depth_subscription_ = self.create_subscription(
            Image,
            '/ur5_left_camera/depth/image_raw',
            self.ur5LeftDepthCallback,
            1
        )

        self.panda_left_camera_color_subscription_ = self.create_subscription(
            Image,
            '/panda_left_camera/image_raw',
            self.pandaLeftRgbCallback,
            1
        )

        self.panda_left_camera_depth_subscription_ = self.create_subscription(
            Image,
            '/panda_left_camera/depth/image_raw',
            self.pandaLeftDepthCallback,
            1
        )

        self.ur5_right_rgb_ = None
        self.ur5_right_depth_ = None
        self.panda_right_rgb_ = None
        self.panda_right_depth_ = None
        self.ur5_right_camera_color_subscription_ = self.create_subscription(
            Image,
            '/ur5_right_camera/image_raw',
            self.ur5RightRgbCallback,
            1
        )

        self.ur5_right_camera_depth_subscription_ = self.create_subscription(
            Image,
            '/ur5_right_camera/depth/image_raw',
            self.ur5RightDepthCallback,
            1
        )

        self.panda_right_camera_color_subscription_ = self.create_subscription(
            Image,
            '/panda_right_camera/image_raw',
            self.pandaRightRgbCallback,
            1
        )

        self.panda_right_camera_depth_subscription_ = self.create_subscription(
            Image,
            '/panda_right_camera/depth/image_raw',
            self.pandaRightDepthCallback,
            1
        )
        
        self.panda_left_no_gripper_rgb_ = None
        self.panda_left_no_gripper_depth_ = None
        self.panda_right_no_gripper_rgb_ = None
        self.panda_right_no_gripper_depth_ = None
        self.panda_no_gripper_left_camera_color_subscription_ = self.create_subscription(
            Image,
            '/panda_no_gripper_left_camera/image_raw',
            self.pandaLeftNoGripperRgbCallback,
            1
        )

        self.panda_no_gripper_left_camera_depth_subscription_ = self.create_subscription(
            Image,
            '/panda_no_gripper_left_camera/depth/image_raw',
            self.pandaLeftNoGripperDepthCallback,
            1
        )

        self.panda_no_gripper_right_camera_color_subscription_ = self.create_subscription(
            Image,
            '/panda_no_gripper_right_camera/image_raw',
            self.pandaRightNoGripperRgbCallback,
            1
        )

        self.panda_no_gripper_right_camera_depth_subscription_ = self.create_subscription(
            Image,
            '/panda_no_gripper_right_camera/depth/image_raw',
            self.pandaRightNoGripperDepthCallback,
            1
        )

        self.joint_subscription_ = self.create_subscription(
            JointState,
            '/gazebo_joint_states',
            self.noTimeGazeboCallback,
            1
        )
        self.cv_bridge_ = CvBridge()
        self.mask_image_publisher_ = self.create_publisher(Image,"mask_image",1)
        self.ready_for_next_input_publisher_ = self.create_publisher(Bool,"/ready_for_next_input",1)
        timer_period = 0.5
        self.links_info_ = []
        self.original_meshes_ = []
        self.full_publisher_ = self.create_publisher(PointCloud2,"full_pointcloud",1)
        self.inpainted_publisher_ = self.create_publisher(MultipleInpaintImages,"inpainted_image",1)
        #self.full_subscriber_ = self.create_subscription(PointCloud2,'full_pointcloud',self.fullPointcloudCallback,10)
        self.full_mask_image_publisher_ = self.create_publisher(MultipleInpaintImages,"full_mask_image",1)
        self.updated_joints_ = False
        self.is_ready_ = True
    
    def ur5LeftRgbCallback(self,msg):
        self.ur5_left_rgb_ = msg
    
    def ur5LeftDepthCallback(self,msg):
        self.ur5_left_depth_ = msg

    def pandaLeftRgbCallback(self,msg):
        self.panda_left_rgb_ = msg
    
    def pandaLeftDepthCallback(self,msg):
        self.panda_left_depth_ = msg

    def ur5RightRgbCallback(self,msg):
        self.ur5_right_rgb_ = msg
    
    def ur5RightDepthCallback(self,msg):
        self.ur5_right_depth_ = msg

    def pandaRightRgbCallback(self,msg):
        self.panda_right_rgb_ = msg
    
    def pandaRightDepthCallback(self,msg):
        self.panda_right_depth_ = msg

    def pandaLeftNoGripperRgbCallback(self,msg):
        self.panda_left_no_gripper_rgb_ = msg

    def pandaLeftNoGripperDepthCallback(self,msg):
        self.panda_left_no_gripper_depth_ = msg

    def pandaRightNoGripperRgbCallback(self,msg):
        self.panda_right_no_gripper_rgb_ = msg

    def pandaRightNoGripperDepthCallback(self,msg):
        self.panda_right_no_gripper_depth_ = msg

    def noTimeGazeboCallback(self,joint_msg):
        start_time = time.time()
        left_inpainted_image,left_mask = self.doFullInpainting(self.ur5_left_rgb_,self.ur5_left_depth_,self.panda_left_rgb_,self.panda_left_depth_,self.panda_left_no_gripper_depth_,self.left_real_rgb_,self.left_real_depth_)
        right_inpainted_image,right_mask = self.doFullInpainting(self.ur5_right_rgb_,self.ur5_right_depth_,self.panda_right_rgb_,self.panda_right_depth_,self.panda_right_no_gripper_depth_,self.right_real_rgb_,self.right_real_depth_)
        inpainted_image_msg = MultipleInpaintImages()
        mask_image_msg = MultipleInpaintImages()
        inpainted_image_msg.images = [self.cv_bridge_.cv2_to_imgmsg(left_inpainted_image),self.cv_bridge_.cv2_to_imgmsg(right_inpainted_image),self.cv_bridge_.cv2_to_imgmsg(left_mask),self.cv_bridge_.cv2_to_imgmsg(right_mask)]
        mask_image_msg.images = []
        self.inpainted_publisher_.publish(inpainted_image_msg)
        self.full_mask_image_publisher_.publish(mask_image_msg)
        inpaint_number = str(self.i_).zfill(5)
        if not os.path.exists('left_inpainting'):
            os.makedirs('left_inpainting')
        if not os.path.exists('right_inpainting'):
            os.makedirs('right_inpainting')
        if not os.path.exists('left_mask'):
            os.makedirs('left_mask')
        if not os.path.exists('right_mask'):
            os.makedirs('right_mask')
        if(self.float_image_):
            left_inpainted_image = (left_inpainted_image * 255).astype(np.uint8)
            right_inpainted_image = (right_inpainted_image * 255).astype(np.uint8)
            left_mask = (left_mask * 255).astype(np.uint8)
            right_mask = (right_mask * 255).astype(np.uint8)
        cv2.imwrite('left_inpainting/inpaint'+ str(inpaint_number) +'.png',left_inpainted_image)
        cv2.imwrite('right_inpainting/inpaint'+ str(inpaint_number) +'.png',right_inpainted_image)
        cv2.imwrite('left_mask/mask'+ str(inpaint_number) +'.png',left_mask)
        cv2.imwrite('right_mask/mask'+ str(inpaint_number) +'.png',right_mask)

    def doFullInpainting(self,real_rgb,real_depth,gazebo_rgb,gazebo_depth,gazebo_no_gripper_depth,world_rgb,world_depth):
        real_rgb_np = self.cv_bridge_.imgmsg_to_cv2(real_rgb)
        real_depth_np = self.cv_bridge_.imgmsg_to_cv2(real_depth)
        gazebo_rgb_np = self.cv_bridge_.imgmsg_to_cv2(gazebo_rgb)
        
        gazebo_depth_np = self.cv_bridge_.imgmsg_to_cv2(gazebo_depth)
        cv2.imwrite('real_rgb.png',real_rgb_np)
        cv2.imwrite('real_depth.png',self.normalize_depth_image(real_depth_np))
        cv2.imwrite('gazebo_rgb.png',gazebo_rgb_np)
        cv2.imwrite('gazebo_depth.png',self.normalize_depth_image(gazebo_depth_np))
        gazebo_no_gripper_depth_np = self.cv_bridge_.imgmsg_to_cv2(gazebo_no_gripper_depth)
        
        real_seg_np = (real_depth_np < 8).astype(np.uint8)
        real_seg_255_np = 255 * real_seg_np
        gazebo_seg_np = (gazebo_depth_np < 8).astype(np.uint8)
        gazebo_seg_255_np = 255 * gazebo_seg_np
        cv2.imwrite('real_seg.png',real_seg_255_np)
        cv2.imwrite('gazebo_seg.png',gazebo_seg_255_np)
        real_no_gripper_seg_255_np = (gazebo_no_gripper_depth_np < 8).astype(np.uint8)
        real_no_gripper_seg_255_np = 255 * real_no_gripper_seg_255_np
        real_rgb = world_rgb
        real_depth = world_depth
        real_seg = real_seg_255_np
        gazebo_rgb_np = cv2.cvtColor(gazebo_rgb_np,cv2.COLOR_BGR2RGB)
        return self.dummyInpaintingEarly(real_rgb,real_seg,real_no_gripper_seg_255_np,gazebo_rgb_np,gazebo_seg_255_np)
    
    def dummyInpaintingEarly(self,rgb,seg_file,seg_file_no_gripper,gazebo_rgb,gazebo_seg):
        rgb = self.cv_bridge_.imgmsg_to_cv2(rgb)
        if(rgb.dtype == np.float32):
            rgb = (rgb * 255).astype(np.uint8)
        # rgb = cv2.resize(rgb,(128,128))
        # seg_file = cv2.resize(seg_file,(128,128))
        # gazebo_rgb = cv2.resize(gazebo_rgb,(128,128))
        # gazebo_seg = cv2.resize(gazebo_seg,(128,128))
        _, gazebo_seg = cv2.threshold(gazebo_seg, 128, 255, cv2.THRESH_BINARY)
        _, seg_file = cv2.threshold(seg_file, 128, 255, cv2.THRESH_BINARY)
        _, seg_file_no_gripper = cv2.threshold(seg_file_no_gripper, 128, 255, cv2.THRESH_BINARY)
        cv2.imwrite('seg_file.png',seg_file)
        cv2.imwrite('seg_file_no_gripper.png',seg_file_no_gripper)
        seg_file_gripper = abs(seg_file - seg_file_no_gripper)
        seg_file_gripper = cv2.erode(seg_file_gripper,np.ones((3,3),np.uint8),iterations=3)
        seg_file_gripper = cv2.dilate(seg_file_gripper,np.ones((3,3),np.uint8),iterations=15)
        cv2.imwrite('seg_file_gripper.png',seg_file_gripper)
        gazebo_segmentation_mask_255 = gazebo_seg
        inverted_segmentation_mask_255_original = cv2.bitwise_not(seg_file_no_gripper)
        cv2.imwrite('inverted_mask1.png',inverted_segmentation_mask_255_original)
        inverted_segmentation_mask_255 = cv2.erode(inverted_segmentation_mask_255_original,np.ones((3,3),np.uint8),iterations=30)
        cv2.imwrite('inverted_mask2.png',inverted_segmentation_mask_255)
        eroded_segmentation_mask_255 = cv2.bitwise_not(inverted_segmentation_mask_255)
        cv2.imwrite('eroded_mask1.png',eroded_segmentation_mask_255)
        eroded_segmentation_mask_255 = eroded_segmentation_mask_255 + seg_file_gripper
        cv2.imwrite('eroded_mask2.png',eroded_segmentation_mask_255)
        inverted_segmentation_mask_255 = cv2.bitwise_not(eroded_segmentation_mask_255)
        cv2.imwrite('final_mask.png',inverted_segmentation_mask_255)
        gazebo_only = cv2.bitwise_and(gazebo_rgb,gazebo_rgb,mask=gazebo_segmentation_mask_255)
        # gazebo_only = cv2.cvtColor(gazebo_only,cv2.COLOR_BGR2RGB)
        #gazebo_robot_only_lab = cv2.cvtColor(gazebo_only,cv2.COLOR_BGR2LAB)
        #gazebo_robot_only_lab[:,:,0] += 10
        #gazebo_robot_only_lab[:,:,0] = np.where(gazebo_segmentation_mask_255 > 0, gazebo_robot_only_lab[:,:,0] + 150, gazebo_robot_only_lab[:,:,0])
        #gazebo_only = cv2.cvtColor(gazebo_robot_only_lab,cv2.COLOR_LAB2BGR)
        cv2.imwrite('gazebo_robot_only.png',gazebo_only)
        cv2.imwrite('background_only_pre1.png',rgb)
        cv2.imwrite('background_only_pre2.png',inverted_segmentation_mask_255)
        _, inverted_segmentation_mask_255 = cv2.threshold(inverted_segmentation_mask_255, 128, 255, cv2.THRESH_BINARY)
        cv2.imwrite('background_only_pre2.png',inverted_segmentation_mask_255)
        background_only = cv2.bitwise_and(rgb,rgb,mask=inverted_segmentation_mask_255)
        cv2.imwrite('background_only_pre3.png',background_only)
        background_only = cv2.inpaint(background_only,cv2.bitwise_not(inverted_segmentation_mask_255),3,cv2.INPAINT_TELEA)
        cv2.imwrite('background_only2.png',background_only)
        inverted_seg_file_original = cv2.bitwise_not(seg_file)
        inverted_seg_file = cv2.erode(inverted_seg_file_original,np.ones((3,3),np.uint8),iterations=3)
        background_only = cv2.bitwise_and(background_only,background_only,mask=cv2.bitwise_not(gazebo_segmentation_mask_255))
        cv2.imwrite('background_only3.png',background_only)
        inpainted_image = gazebo_only + background_only
        cv2.imwrite('background_only4.png',inpainted_image)
        better_dilated_blend_mask = cv2.bitwise_not(inverted_seg_file)*cv2.bitwise_not(gazebo_seg)*255
        diffusion_input = cv2.bitwise_and(inpainted_image,inpainted_image,mask=cv2.bitwise_not(better_dilated_blend_mask))
        if(self.float_image_):
            inpainted_image = (inpainted_image / 255.0).astype(np.float32)
            diffusion_input = (diffusion_input / 255.0).astype(np.float32)
        return inpainted_image,diffusion_input

    def gazeboCallback(self,joints,real_rgb,real_depth,gazebo_rgb,gazebo_depth,):
        return
        start_time = time.time()
        real_rgb_np = self.cv_bridge_.imgmsg_to_cv2(real_rgb)
        real_depth_np = self.cv_bridge_.imgmsg_to_cv2(real_depth)
        gazebo_rgb_np = self.cv_bridge_.imgmsg_to_cv2(gazebo_rgb)
        
        gazebo_depth_np = self.cv_bridge_.imgmsg_to_cv2(gazebo_depth)
        cv2.imwrite('real_rgb.png',real_rgb_np)
        cv2.imwrite('real_depth.png',self.normalize_depth_image(real_depth_np))
        cv2.imwrite('gazebo_rgb.png',gazebo_rgb_np)
        cv2.imwrite('gazebo_depth.png',self.normalize_depth_image(gazebo_depth_np))
        
        real_seg_np = (real_depth_np < 8).astype(np.uint8)
        real_seg_255_np = 255 * real_seg_np
        gazebo_seg_np = (gazebo_depth_np < 8).astype(np.uint8)
        gazebo_seg_255_np = 255 * gazebo_seg_np
        cv2.imwrite('real_seg.png',real_seg_255_np)
        cv2.imwrite('gazebo_seg.png',gazebo_seg_255_np)
        real_rgb = self.real_rgb_
        real_depth = self.real_depth_
        real_seg = real_seg_255_np
        gazebo_rgb_np = cv2.cvtColor(gazebo_rgb_np,cv2.COLOR_BGR2RGB)
        self.inpainting(real_rgb,real_depth,real_seg,gazebo_rgb_np,gazebo_seg_255_np,gazebo_depth_np)
        self.updated_joints_ = False
        end_time = time.time()
        print("Algo time Part 3: " + str(end_time - start_time) + " seconds")
        return
        #if(np.linalg.norm(joint_command_np - gazebo_joints_np,2) < 0.01):
            
        #elif(np.linalg.norm(joint_command_np - gazebo_joints_np,2) < 0.01 and not self.updated_joints_):
        #    self.updated_joints_ = True

    def cameraInfoCallback(self,msg):
        if(self.is_ready_):
            self.camera_intrinsic_matrix_ = np.array([[msg.k[0],msg.k[1],msg.k[2],0],[msg.k[3],msg.k[4],msg.k[5],0],[msg.k[6],msg.k[7],msg.k[8],0]])
            self.image_shape_ = (msg.height,msg.width,3)

    def cameraCallback(self,msg):
        if(self.is_ready_):
            self.original_image_ = self.cv_bridge_.imgmsg_to_cv2(msg,desired_encoding="passthrough")
            #cv2.imwrite('gazebo_rgb.png',self.original_image_)

    def prelimMeshFast(self,filename,link_name,rpy_str,xyz_str):
        # RPY is in ZYX I'm pretty sure
        mesh_scene = trimesh.load(filename)
        if(link_name == "panda_link6"):
            meshes = mesh_scene.geometry
            for mesh in meshes:
                if(mesh != 'Shell006_000-mesh'):
                    vertices = o3d.utility.Vector3dVector(meshes[mesh].vertices)
                    triangles = o3d.utility.Vector3iVector(meshes[mesh].faces)
                    open3d_mesh = o3d.geometry.TriangleMesh(vertices, triangles)
                    open3d_mesh.translate(np.array([0,0,-0.028439417985386614/2]))
                    meshes[mesh] = trimesh.Trimesh(vertices=open3d_mesh.vertices,faces=open3d_mesh.triangles)
            #meshes['Shell012_000-mesh'] = trimesh.Trimesh(vertices=open3d_mesh.vertices,faces=open3d_mesh.triangles)
            mesh = trimesh.util.concatenate(tuple(trimesh.Trimesh(vertices=g.vertices, faces=g.faces)
                                            for g in meshes.values()))

        mesh = trimesh.util.concatenate(tuple(trimesh.Trimesh(vertices=g.vertices, faces=g.faces)
                                            for g in mesh_scene.geometry.values()))
        # Convert Trimesh to Open3D TriangleMesh
        vertices = o3d.utility.Vector3dVector(mesh.vertices)
        triangles = o3d.utility.Vector3iVector(mesh.faces)
        open3d_mesh = o3d.geometry.TriangleMesh(vertices, triangles)
        test_pcd = open3d_mesh.sample_points_uniformly(number_of_points=50000)
        test_pcd_data = np.asarray(test_pcd.points)
        
        diff = max(np.max(test_pcd_data[:, 0]) - np.min(test_pcd_data[:, 0]),np.max(test_pcd_data[:, 1]) - np.min(test_pcd_data[:, 1]),np.max(test_pcd_data[:, 2]) - np.min(test_pcd_data[:, 2]))
        # Checks to make sure units are in mm instead of m (We convert uniformly to meters later)
        
        if(diff < 1):
            open3d_mesh.vertices = o3d.utility.Vector3dVector(np.asarray(open3d_mesh.vertices) * 1000)
        else:
            R = np.array([[-1,0,0],[0,0,1],[0,1,0]])
            open3d_mesh.rotate(R,[0,0,0])
        test_pcd = open3d_mesh.sample_points_uniformly(number_of_points=50000)
        #mesh_coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=100, origin=[0,0,0])
        #o3d.visualization.draw_geometries([test_pcd,mesh_coordinate_frame])
        rpy_str_list = rpy_str.split()
        rpy_floats = [float(x) for x in rpy_str_list]
        rpy_np = np.array(rpy_floats)
        xyz_str_list = xyz_str.split()
        xyz_floats = [float(x) for x in xyz_str_list]
        if(link_name == "panda_link1"):
            xyz_floats = [0, 0, -0.1929999099]
        elif(link_name == "panda_link3"):
            xyz_floats = [0,0,-0.1219998142]
        elif(link_name == "panda_link5"):
            xyz_floats = [0,0,-0.2630000007]
        elif(link_name == "panda_link7"):
            rpy_np = np.array([0,0,-math.pi/4])
            xyz_floats = [0,0,0.03679997502 + (0.028439417985386614/2)]
        xyz_np = 1000 * np.array(xyz_floats)
        R2 = self.eulerToR(rpy_np)
        # Create a 4x4 identity matrix
        transform_matrix = np.eye(4)

        # Replace the top-left 3x3 submatrix with the rotation matrix
        transform_matrix[:3, :3] = R2

        # Set the first three elements in the fourth column to the translation vector
        transform_matrix[:3, 3] = xyz_np

        # Set the bottom-right element to 1
        transform_matrix[3, 3] = 1.0
        open3d_mesh.transform(transform_matrix)
        return open3d_mesh
    
    def getPixels(self,msg):
        if(self.is_ready_):
            msg_data = point_cloud2.read_points(msg)
            msg_data = np.array([[item.tolist() for item in row] for row in msg_data])
            depth_data = msg_data[:,2]
            camera_transform = np.vstack((self.camera_intrinsic_matrix_,np.array([0,0,0,1]).reshape(1,4)))
            pixel_data = self.project_points_from_world_to_camera(msg_data,camera_transform,self.image_shape_[1],self.image_shape_[0])
            return pixel_data, depth_data
        
    def project_points_from_world_to_camera(self,points, world_to_camera_transform, camera_height, camera_width,pixel_to_point_dicts=False):
        """
        Helper function to project a batch of points in the world frame
        into camera pixels using the world to camera transformation.

        Args:
            points (np.array): 3D points in world frame to project onto camera pixel locations. Should
                be shape [..., 3].
            world_to_camera_transform (np.array): 4x4 Tensor to go from robot coordinates to pixel
                coordinates.
            camera_height (int): height of the camera image
            camera_width (int): width of the camera image

        Return:
            pixels (np.array): projected pixel indices of shape [..., 2]
        """
        assert points.shape[-1] == 3  # last dimension must be 3D
        assert len(world_to_camera_transform.shape) == 2
        assert world_to_camera_transform.shape[0] == 4 and world_to_camera_transform.shape[1] == 4

        # convert points to homogenous coordinates -> (px, py, pz, 1)
        ones_pad = np.ones(points.shape[:-1] + (1,))
        points = np.concatenate((points, ones_pad), axis=-1)  # shape [..., 4]

        # batch matrix multiplication of 4 x 4 matrix and 4 x 1 vectors to do robot frame to pixels transform
        mat_reshape = [1] * len(points.shape[:-1]) + [4, 4]
        cam_trans = world_to_camera_transform.reshape(mat_reshape)  # shape [..., 4, 4]
        pixels = np.matmul(cam_trans, points[..., None])[..., 0]  # shape [..., 4]

        # re-scaling from homogenous coordinates to recover pixel values
        # (x, y, z) -> (x / z, y / z)
        pixels = pixels / pixels[..., 2:3]
        pixels = pixels[..., :2].round().astype(int)  # shape [..., 2]
        # swap first and second coordinates to get pixel indices that correspond to (height, width)
        # and also clip pixels that are out of range of the camera image
        pixels = np.concatenate(
            (
                pixels[..., 1:2].clip(0, camera_height - 1),
                pixels[..., 0:1].clip(0, camera_width - 1),
            ),
            axis=-1,
        )
        if(pixel_to_point_dicts):
            points_to_pixels_robosuite = {tuple(arr_4): tuple(arr_2) for arr_4, arr_2 in zip(points,pixels)}
            pixels_to_points_robosuite = {}
            for key,value in points_to_pixels_robosuite.items():
                pixels_to_points_robosuite.setdefault(value,[]).append(key)
            return pixels,points_to_pixels_robosuite,pixels_to_points_robosuite
        else:
            return pixels
    
    def normalize_depth_image(self,depth_image):
        # Define the minimum and maximum depth values in your depth image
        min_depth = np.min(depth_image)
        max_depth = np.max(depth_image)

        # Normalize the depth image to the range [0, 1]
        normalized_depth_image = (depth_image - min_depth) / (max_depth - min_depth)

        # Optionally, you can scale the normalized image to a different range
        # For example, to scale it to [0, 255] for visualization:
        normalized_depth_image = (normalized_depth_image * 255).astype(np.uint8)
        return normalized_depth_image
    
    def convertPointcloudToDepth(self,pointcloud):
        if(type(pointcloud) == str):
            pointcloud_np = np.load(pointcloud)
        else:
            pointcloud_np = pointcloud
            world_to_camera = np.array([[-5.55111512e-17,  2.58174524e-01, -9.66098295e-01,
                    1.60000000e+00],
                [ 1.00000000e+00,  0.00000000e+00,  0.00000000e+00,
                    0.00000000e+00],
                [ 0.00000000e+00, -9.66098295e-01, -2.58174524e-01,
                    1.45000000e+00],
                [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
                    1.00000000e+00]])
            pcd = o3d.geometry.PointCloud()
            pcd.points = o3d.utility.Vector3dVector(pointcloud_np)
            pcd.transform(np.linalg.inv(world_to_camera))
            pointcloud_np = np.asarray(pcd.points)

            # loaded = np.load('/home/lawrence/cross_embodiment_ws/src/gazebo_env/robotsuite_outputs/UR5e_output3.npy', allow_pickle=True)

        depth_data = pointcloud_np[:,2]

        fx = self.robosuite_intrinsic_matrix_[0,0]
        fy = self.robosuite_intrinsic_matrix_[1,1]
        cx = self.robosuite_intrinsic_matrix_[0,2]
        cy = self.robosuite_intrinsic_matrix_[1,2]
        u_pixels = ((pointcloud_np[:,0]*fx) / depth_data) + cx
        u_pixels = np.round(u_pixels).astype(int)
        v_pixels = ((pointcloud_np[:,1]*fy) / depth_data) + cy
        v_pixels = np.round(v_pixels).astype(int)
        pixels = np.vstack((u_pixels,v_pixels)).T
        pixels_to_points = {tuple(pixel): tuple(point) for pixel, point in zip(pixels,pointcloud_np)}
        depth_image = np.zeros(self.robosuite_image_shape_)
        for pixel,point in pixels_to_points.items():
            depth_image[pixel[1],pixel[0]] = point[2]
        return depth_image
    
    def dummyInpainting(self,rgb,seg_file,gazebo_rgb,gazebo_seg):
        rgb = self.cv_bridge_.imgmsg_to_cv2(rgb)
        if(rgb.dtype == np.float32):
            rgb = (rgb * 255).astype(np.uint8)
        # rgb = cv2.resize(rgb,(128,128))
        # seg_file = cv2.resize(seg_file,(128,128))
        # gazebo_rgb = cv2.resize(gazebo_rgb,(128,128))
        # gazebo_seg = cv2.resize(gazebo_seg,(128,128))
        _, gazebo_seg = cv2.threshold(gazebo_seg, 128, 255, cv2.THRESH_BINARY)
        gazebo_segmentation_mask_255 = gazebo_seg
        inverted_segmentation_mask_255_original = cv2.bitwise_not(gazebo_seg)
        cv2.imwrite('inverted_mask1.png',inverted_segmentation_mask_255_original)
        inverted_segmentation_mask_255 = cv2.erode(inverted_segmentation_mask_255_original,np.ones((3,3),np.uint8),iterations=10)
        cv2.imwrite('inverted_mask2.png',inverted_segmentation_mask_255)
        outline_mask = abs(inverted_segmentation_mask_255 - inverted_segmentation_mask_255_original)*255
        gazebo_only = cv2.bitwise_and(gazebo_rgb,gazebo_rgb,mask=gazebo_segmentation_mask_255)
        # gazebo_only = cv2.cvtColor(gazebo_only,cv2.COLOR_BGR2RGB)
        #gazebo_robot_only_lab = cv2.cvtColor(gazebo_only,cv2.COLOR_BGR2LAB)
        #gazebo_robot_only_lab[:,:,0] += 10
        #gazebo_robot_only_lab[:,:,0] = np.where(gazebo_segmentation_mask_255 > 0, gazebo_robot_only_lab[:,:,0] + 150, gazebo_robot_only_lab[:,:,0])
        #gazebo_only = cv2.cvtColor(gazebo_robot_only_lab,cv2.COLOR_LAB2BGR)
        cv2.imwrite('gazebo_robot_only.png',gazebo_only)
        background_only = cv2.bitwise_and(rgb,rgb,mask=inverted_segmentation_mask_255_original)
        inverted_seg_file_original = cv2.bitwise_not(seg_file)
        #cv2.imwrite('inverted_seg_file_original.png',inverted_seg_file_original)
        inverted_seg_file = cv2.erode(inverted_seg_file_original,np.ones((3,3),np.uint8),iterations=3)
        #cv2.imwrite('inverted_seg_file.png',inverted_seg_file)
        background_only = cv2.bitwise_and(background_only,background_only,mask=inverted_seg_file)
        cv2.imwrite('background_only.png',background_only)
        inpainted_image = gazebo_only + background_only
        #cv2.imwrite('no_fill.png',inpainted_image)

        better_dilated_blend_mask = cv2.bitwise_not(inverted_seg_file)*cv2.bitwise_not(gazebo_seg)*255
        cv2.imwrite('better_dilated_blend_mask.png',better_dilated_blend_mask)
        cv2.imwrite('pre_inpainted_image.png',inpainted_image)
        cv2_inpaint_image = cv2.inpaint(inpainted_image,better_dilated_blend_mask,3,cv2.INPAINT_TELEA)

        target_color = (39,43,44)
        target_mask = np.zeros_like(inpainted_image)
        target_mask[:,:] = target_color
        inpainted_image = np.where(better_dilated_blend_mask[:,:,None] != 0,target_mask,inpainted_image).astype(np.uint8)
        inpainted_image = cv2_inpaint_image
        cv2.imwrite('og_inpainted_image.png',inpainted_image)
        import pdb
        pdb.set_trace()
        inpaint_number = str(self.i_).zfill(5)
        if not os.path.exists('inpainting'):
            os.makedirs('inpainting')
        if not os.path.exists('mask'):
            os.makedirs('mask')
        cv2.imwrite('inpainting/inpaint'+ str(inpaint_number) +'.png',inpainted_image)
        cv2.imwrite('mask/mask'+ str(inpaint_number) +'.png',better_dilated_blend_mask.astype(np.uint8))
        if(self.float_image_):
            inpainted_image = (inpainted_image / 255.0).astype(np.float32)
        inpainted_image_msg = self.cv_bridge_.cv2_to_imgmsg(inpainted_image)
        mask_image_msg = self.cv_bridge_.cv2_to_imgmsg(better_dilated_blend_mask.astype(np.uint8),encoding="mono8")
        inpainted_image_msg.header.stamp = self.get_clock().now().to_msg()
        mask_image_msg.header.stamp = inpainted_image_msg.header.stamp
        inpainted_image_msgs = MultipleInpaintImages()
        inpainted_image_msgs.images = [inpainted_image_msg,inpainted_image_msg]
        self.inpainted_publisher_.publish(inpainted_image_msgs)
        self.mask_image_publisher_.publish(mask_image_msg)

# better_blend_mask = joined_depth_argmin * real_segmentation_mask_255
#         better_dilated_blend_mask = joined_depth_argmin * cv2.bitwise_not(inverted_real_segmentation_mask_255)
#         target_color = (39,43,44)
#         target_mask = np.zeros_like(inpainted_image)
#         target_mask[:,:] = target_color
#         got_away = np.where(better_dilated_blend_mask[:,:,None] != 0,target_mask,inpainted_image).astype(np.uint8)
#         #image_8bit = cv2.inpaint(inpainted_image.astype(np.uint8),better_blend_mask.astype(np.uint8),3,cv2.INPAINT_TELEA)
#         image_8bit = cv2.convertScaleAbs(inpainted_image)  # Convert to 8-bit image
#         image_8bit = got_away
    def inpainting(self,rgb,depth,seg_file,gazebo_rgb,gazebo_seg,gazebo_depth):
        return
        if type(rgb) == str:
            rgb_np = cv2.imread(rgb)
            seg = cv2.imread(seg_file,0)
            depth_np = np.load(depth)
            return
        else:
            rgb_np = self.cv_bridge_.imgmsg_to_cv2(rgb)
            # rgb_np = np.array(msg.rgb,dtype=np.uint8).reshape((msg.segmentation.width,msg.segmentation.height,3))
            depth_np = depth
            seg = seg_file
        _, seg = cv2.threshold(seg, 128, 255, cv2.THRESH_BINARY)
        #rgb_np = cv2.resize(rgb_np,(128,128))
        #depth_np = cv2.resize(depth_np,(128,128))
        #seg = cv2.resize(seg,(128,128))
        #gazebo_rgb = cv2.resize(gazebo_rgb,(128,128))
        #gazebo_seg = cv2.resize(gazebo_seg,(128,128))
        #gazebo_depth = cv2.resize(gazebo_depth,(128,128))
        real_depth_image_unmasked = depth_np
        real_rgb_image_unmasked = rgb_np
        real_segmentation_mask_255 = seg
        gazebo_robot_only_rgb = gazebo_rgb
        gazebo_segmentation_mask_255 = gazebo_seg
        gazebo_robot_only_depth = gazebo_depth
        real_rgbd_image_unmasked = np.concatenate((real_rgb_image_unmasked,real_depth_image_unmasked[:,:,np.newaxis]),axis=2)
        inverted_segmentation_mask_255_original = cv2.bitwise_not(real_segmentation_mask_255)
        inverted_real_segmentation_mask_255 = cv2.erode(inverted_segmentation_mask_255_original,np.ones((3,3),np.uint8),iterations=10)
        cv2.imwrite('inverted_real_segmentation_mask_255.png',inverted_real_segmentation_mask_255)
        outline_mask = abs(inverted_real_segmentation_mask_255 - inverted_segmentation_mask_255_original)*255
        real_rgbd_image_masked = cv2.bitwise_and(real_rgbd_image_unmasked,real_rgbd_image_unmasked,mask=inverted_real_segmentation_mask_255)
        real_rgb_image_masked = real_rgbd_image_masked[:,:,0:3].astype(np.uint8)
        
        # real_rgb_image_masked = cv2.inpaint(real_rgb_image_masked,outline_mask,3,cv2.INPAINT_TELEA)
        real_depth_image_masked = real_rgbd_image_masked[:,:,-1]
        joined_depth = np.concatenate((gazebo_robot_only_depth[np.newaxis],real_depth_image_masked[np.newaxis]),axis=0)
        joined_depth[0,:,:][joined_depth[0,:,:] == 0] = 1000
        joined_depth[1,:,:][joined_depth[1,:,:] == 0] = 5
        joined_depth_argmin = np.argmin(joined_depth,axis=0)
        
        real_rgb_image_masked_inpaint = real_rgb_image_masked
        
        
        attempt = real_rgb_image_masked_inpaint * joined_depth_argmin[:,:,np.newaxis]
        inverted_joined_depth_argmin = 1 - joined_depth_argmin
        gazebo_robot_only_lab = cv2.cvtColor(gazebo_robot_only_rgb,cv2.COLOR_BGR2LAB)
        gazebo_robot_only_lab[:,:,0] += 100
        gazebo_robot_only_mod = cv2.cvtColor(gazebo_robot_only_lab,cv2.COLOR_LAB2BGR)
        gazebo_robot_only_rgb = gazebo_robot_only_mod
        attempt2 = gazebo_robot_only_rgb * inverted_joined_depth_argmin[:,:,np.newaxis]
        
        inpainted_image = cv2.add(attempt,attempt2)#attempt + attempt2
        
        better_blend_mask = joined_depth_argmin * real_segmentation_mask_255
        better_dilated_blend_mask = joined_depth_argmin * cv2.bitwise_not(inverted_real_segmentation_mask_255)
        target_color = (39,43,44)
        target_mask = np.zeros_like(inpainted_image)
        target_mask[:,:] = target_color
        got_away = np.where(better_dilated_blend_mask[:,:,None] != 0,target_mask,inpainted_image).astype(np.uint8)
        #image_8bit = cv2.inpaint(inpainted_image.astype(np.uint8),better_blend_mask.astype(np.uint8),3,cv2.INPAINT_TELEA)
        image_8bit = cv2.convertScaleAbs(inpainted_image)  # Convert to 8-bit image
        image_8bit = got_away
        inpaint_number = str(self.i_).zfill(5)
        if not os.path.exists('inpainting'):
            os.makedirs('inpainting')
        if not os.path.exists('mask'):
            os.makedirs('mask')
        cv2.imwrite('inpainting/inpaint'+ str(inpaint_number) +'.png',image_8bit)
        cv2.imwrite('mask/mask'+ str(inpaint_number) +'.png',better_blend_mask.astype(np.uint8))
        # cv2.imwrite('small_inpaint.png',cv2.resize(image_8bit,(128,128)))

        inpainted_image_msg = self.cv_bridge_.cv2_to_imgmsg(image_8bit,encoding="bgr8")
        mask_image_msg = self.cv_bridge_.cv2_to_imgmsg(better_blend_mask.astype(np.uint8),encoding="mono8")
        self.inpainted_publisher_.publish(inpainted_image_msg)
        self.mask_image_publisher_.publish(mask_image_msg)
        ready_for_next_message = Bool()
        ready_for_next_message.data = True
        self.ready_for_next_input_publisher_.publish(ready_for_next_message)
        return

        transformed_gazebo_rgb,transformed_gazebo_depth = self.transformGazeboImage(gazebo_robot_only_rgb,gazebo_segmentation_mask_255,pointcloud_msg)
        real_rgbd_image_unmasked = np.concatenate((real_rgb_image_unmasked,real_depth_image_unmasked[:,:,np.newaxis]),axis=2)
        inverted_real_segmentation_mask_255 = cv2.bitwise_not(real_segmentation_mask_255)
        real_rgbd_image_masked = cv2.bitwise_and(real_rgbd_image_unmasked,real_rgbd_image_unmasked,mask=inverted_real_segmentation_mask_255)
        real_rgb_image_masked = real_rgbd_image_masked[:,:,0:3].astype(np.uint8)
        real_depth_image_masked = real_rgbd_image_masked[:,:,-1]
        joined_depth = np.concatenate((transformed_gazebo_depth[np.newaxis],real_depth_image_masked[np.newaxis]),axis=0)
        joined_depth[joined_depth == 0] = 1000
        joined_depth_argmin = np.argmin(joined_depth,axis=0)
        real_rgb_image_masked_inpaint = cv2.inpaint(real_rgb_image_masked,real_segmentation_mask_255,inpaintRadius=3,flags=cv2.INPAINT_TELEA)
        attempt = real_rgb_image_masked_inpaint * joined_depth_argmin[:,:,np.newaxis]
        inverted_joined_depth_argmin = 1 - joined_depth_argmin
        attempt2 = transformed_gazebo_rgb * inverted_joined_depth_argmin[:,:,np.newaxis]
        inpainted_image = attempt + attempt2
        image_8bit = cv2.convertScaleAbs(inpainted_image)  # Convert to 8-bit image
        last_slash_index = seg_file.rfind('/')
        underscore_before_last_slash_index = seg_file.rfind('_', 0, last_slash_index)
        str_num = seg_file[underscore_before_last_slash_index + 1:last_slash_index]
        inpaint_file = seg_file[:seg_file.rfind('/', 0, seg_file.rfind('/')) + 1] + 'results/inpaint' + str_num +'.png'

        cv2.imwrite(inpaint_file,image_8bit)
        inpainted_image_msg = self.cv_bridge_.cv2_to_imgmsg(image_8bit,encoding="bgr8")
        self.inpainted_publisher_.publish(inpainted_image_msg)

    def custom_mode_filter(self,image, mask, kernel_size):
        result = np.zeros_like(image)
        pad = kernel_size // 2
        for i in range(pad, image.shape[0] - pad):
            for j in range(pad, image.shape[1] - pad):
                if mask[i, j]:
                    neighborhood = image[i - pad: i + pad + 1, j - pad: j + pad + 1]
                    unique, counts = np.unique(neighborhood.reshape(-1, 3), axis=0, return_counts=True)
                    mode_color = unique[np.argmax(counts)]
                    result[i, j] = mode_color

        return result

    def replace_black_with_surrounding_mode(self,img):

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Threshold the grayscale image to identify black pixels
        _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

        # Invert the mask to mark black pixels as True (255) and others as False (0)
        #mask = np.where(thresh == 0, 255, 0)
        mask = thresh
        # Apply custom mode filter to find the mode RGB value of the surrounding pixels
        replaced_img = self.custom_mode_filter(img, mask, kernel_size=3)

        return replaced_img

    def transformGazeboImage(self,gazebo_rgb,gazebo_seg,pointcloud_msg):
        pointcloud = point_cloud2.read_points(pointcloud_msg)
        # Pointcloud is in camera frame
        pointcloud = np.array([[item.tolist() for item in row] for row in pointcloud])
        
        gazebo_camera_transform = np.vstack((self.camera_intrinsic_matrix_,np.array([0,0,0,1]).reshape(1,4)))
        _,points_to_pixels_gazebo,pixels_to_points_gazebo = self.project_points_from_world_to_camera(pointcloud,gazebo_camera_transform,self.image_shape_[0],self.image_shape_[1],True)
        robosuite_camera_transform = np.hstack((self.robosuite_intrinsic_matrix_,np.array([0,0,0]).reshape(3,1)))
        robosuite_camera_transform = np.vstack((robosuite_camera_transform,np.array([0,0,0,1]).reshape(1,4)))
        robosuite_img_points,points_to_pixels_robosuite,pixels_to_points_robosuite = self.project_points_from_world_to_camera(pointcloud,robosuite_camera_transform,self.robosuite_image_shape_[0],self.robosuite_image_shape_[1],True)
        transformed_gazebo_rgb_noisy = np.zeros((self.robosuite_image_shape_[0],self.robosuite_image_shape_[1],3))
        transformed_gazebo_seg = np.zeros((self.robosuite_image_shape_[0],self.robosuite_image_shape_[1]))
        gazebo_depth = np.zeros((self.robosuite_image_shape_[0],self.robosuite_image_shape_[1])) * 1000
        for pixel in pixels_to_points_robosuite.keys():
            points = pixels_to_points_robosuite[pixel]
            points_np = np.array([list(point) for point in points])
            depth_value = np.mean(points_np[:,2])
            gazebo_pixels = []
            for point in points: 
                gazebo_pixels.append(list(points_to_pixels_gazebo[point]))
            rgb_values = []
            for gazebo_pixel in gazebo_pixels:
                rgb_values.append(gazebo_rgb[gazebo_pixel[0],gazebo_pixel[1],:])
            
            rgb_values_np = np.array(rgb_values)
            mean_rgb_value = np.mean(rgb_values_np,axis=0).astype(int)
            transformed_gazebo_rgb_noisy[pixel[0],pixel[1],:] = mean_rgb_value
            gazebo_depth[pixel[0],pixel[1]] = depth_value
            transformed_gazebo_seg[pixel[0],pixel[1]] = 255
        gazebo_depth_after= cv2.dilate(gazebo_depth,(3,3),iterations=3)
        gazebo_depth_after = cv2.erode(gazebo_depth_after,(3,3),iterations=3)
        transformed_gazebo_seg_after= cv2.dilate(transformed_gazebo_seg,(3,3),iterations=3)
        transformed_gazebo_seg_after = cv2.erode(transformed_gazebo_seg_after,(3,3),iterations=3)
        transformed_gazebo_rgb_noisy = transformed_gazebo_rgb_noisy.astype(np.uint8)
        transformed_gazebo_seg_inverted = np.where(transformed_gazebo_seg == 0,255,0)
        #transformed_gazebo_seg_after_inverted = np.where(transformed_gazebo_seg_after == 0,255,0)
        #transformed_gazebo_seg_gray = np.where(transformed_gazebo_seg_after == 0,128,255).astype(np.uint8)
        inpainting_mask = cv2.bitwise_and(transformed_gazebo_seg_inverted,transformed_gazebo_seg_inverted,mask=transformed_gazebo_seg_after.astype(np.uint8))
        transformed_gazebo_rgb = cv2.inpaint(transformed_gazebo_rgb_noisy,inpainting_mask.astype(np.uint8),inpaintRadius=3,flags=cv2.INPAINT_TELEA)
        return transformed_gazebo_rgb,gazebo_depth_after
    
    def fullPointcloudCallback(self,msg,rgb,depth,segmentation):
        if(self.is_ready_):
            if(self.camera_intrinsic_matrix_ is None):
                return
            all_pixels,depth_data = self.getPixels(msg)
            mask_image = np.zeros(self.image_shape_[:2], dtype=np.uint8)
            clean_mask_image = np.zeros(self.image_shape_[:2], dtype=np.uint8)
            depth_image = np.zeros(self.image_shape_[:2], dtype=np.float64)
            clean_depth_image = np.zeros(self.image_shape_[:2], dtype=np.float64)
            white_color = (255,255,255)
            i = 0
            block_background_mask = np.all(self.original_image_ != [155,155,155],axis=2)
            for coord in all_pixels:
                x,y = coord
                mask_image[round(x), round(y)] = 255
                depth_image[round(x), round(y)] = depth_data[i]
                if(block_background_mask[round(x),round(y)]):
                    clean_mask_image[round(x),round(y)] = 255
                    clean_depth_image[round(x),round(y)] = depth_data[i]
                i += 1
            cv2.imwrite('clean_mask_image.png',clean_mask_image)
            cv2.imwrite('mask_image.png',mask_image)
            cv2.imwrite('depth_image.png',self.normalize_depth_image(depth_image))
            mask_image = clean_mask_image
            depth_image = clean_depth_image
            if(self.original_image_ is not None):
                mask_image = cv2.resize(mask_image, (mask_image.shape[1], mask_image.shape[0]))
                gazebo_masked_image = np.zeros_like(self.original_image_)
                gazebo_masked_image = cv2.bitwise_and(self.original_image_, self.original_image_, mask=clean_mask_image)
                cv2.imwrite('original_image.png',self.original_image_)
                cv2.imwrite('gazebo_masked_image.png',gazebo_masked_image)
                self.inpainting(rgb,depth,segmentation,gazebo_masked_image,mask_image,depth_image)
            return
            np.save('/home/lawrence/gazebo_robot_depth.npy',depth_image)
            old_mask_image = mask_image
            mask_image = cv2.cvtColor(mask_image, cv2.COLOR_RGB2GRAY)
            _, mask_image = cv2.threshold(mask_image, 128, 255, cv2.THRESH_BINARY)
            if(self.original_image_ is not None):
                mask_image = cv2.resize(mask_image, (mask_image.shape[1], mask_image.shape[0]))
                im_floodfill = mask_image.copy()
                (h,w) = mask_image.shape
                mask = np.zeros((h+2,w+2),np.uint8)
                cv2.floodFill(im_floodfill,mask,(0,0),255)
                im_floodfill_inv = cv2.bitwise_not(im_floodfill)
                im_out = mask_image | im_floodfill_inv
                mask_image = im_out
                # Create a new image with the same size as the original image
                gazebo_masked_image = np.zeros_like(self.original_image_)

                # Apply the gazebo_mask to the original image using element-wise multiplication
                gazebo_masked_image = cv2.bitwise_and(self.original_image_, self.original_image_, mask=mask_image)
                gazebo_masked_image[:, :, 0], gazebo_masked_image[:, :, 2] = gazebo_masked_image[:, :, 2].copy(), gazebo_masked_image[:, :, 0].copy()
                cv2.imwrite('/home/lawrence/gazebo_robot_only.jpg',gazebo_masked_image)
                cv2.imwrite('/home/lawrence/gazebo_mask.jpg',mask_image)
                #mask_image = cv2.convertScaleAbs(mask_image, alpha=(255.0/65535.0))
                ros_mask_image = self.cv_bridge_.cv2_to_imgmsg(old_mask_image,encoding="bgr8")
                self.full_mask_image_publisher_.publish(ros_mask_image)
                self.inpainting(rgb,depth,segmentation,gazebo_masked_image,mask_image,msg)

    def setupMesh(self,filename,link_name,rpy_str,xyz_str):
        if(self.is_ready_):
            # RPY is in ZYX I'm pretty sure
            mesh_scene = trimesh.load(filename)
            if(link_name == "panda_link6"):
                meshes = mesh_scene.geometry
                for mesh in meshes:
                    if(mesh != 'Shell006_000-mesh'):
                        vertices = o3d.utility.Vector3dVector(meshes[mesh].vertices)
                        triangles = o3d.utility.Vector3iVector(meshes[mesh].faces)
                        open3d_mesh = o3d.geometry.TriangleMesh(vertices, triangles)
                        open3d_mesh.translate(np.array([0,0,-0.028439417985386614/2]))
                        meshes[mesh] = trimesh.Trimesh(vertices=open3d_mesh.vertices,faces=open3d_mesh.triangles)
                #meshes['Shell012_000-mesh'] = trimesh.Trimesh(vertices=open3d_mesh.vertices,faces=open3d_mesh.triangles)
                mesh = trimesh.util.concatenate(tuple(trimesh.Trimesh(vertices=g.vertices, faces=g.faces)
                                                for g in meshes.values()))

            mesh = trimesh.util.concatenate(tuple(trimesh.Trimesh(vertices=g.vertices, faces=g.faces)
                                                for g in mesh_scene.geometry.values()))
            # Convert Trimesh to Open3D TriangleMesh
            vertices = o3d.utility.Vector3dVector(mesh.vertices)
            triangles = o3d.utility.Vector3iVector(mesh.faces)
            open3d_mesh = o3d.geometry.TriangleMesh(vertices, triangles)
            test_pcd = open3d_mesh.sample_points_uniformly(number_of_points=50000)
            test_pcd_data = np.asarray(test_pcd.points)
            
            diff = max(np.max(test_pcd_data[:, 0]) - np.min(test_pcd_data[:, 0]),np.max(test_pcd_data[:, 1]) - np.min(test_pcd_data[:, 1]),np.max(test_pcd_data[:, 2]) - np.min(test_pcd_data[:, 2]))
            # Checks to make sure units are in mm instead of m (We convert uniformly to meters later)
            
            if(diff < 1):
                open3d_mesh.vertices = o3d.utility.Vector3dVector(np.asarray(open3d_mesh.vertices) * 1000)
            else:
                R = np.array([[-1,0,0],[0,0,1],[0,1,0]])
                open3d_mesh.rotate(R,[0,0,0])
            test_pcd = open3d_mesh.sample_points_uniformly(number_of_points=50000)
            #mesh_coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=100, origin=[0,0,0])
            #o3d.visualization.draw_geometries([test_pcd,mesh_coordinate_frame])
            rpy_str_list = rpy_str.split()
            rpy_floats = [float(x) for x in rpy_str_list]
            rpy_np = np.array(rpy_floats)
            xyz_str_list = xyz_str.split()
            xyz_floats = [float(x) for x in xyz_str_list]
            if(link_name == "panda_link1"):
                xyz_floats = [0, 0, -0.1929999099]
            elif(link_name == "panda_link3"):
                xyz_floats = [0,0,-0.1219998142]
            elif(link_name == "panda_link5"):
                xyz_floats = [0,0,-0.2630000007]
            elif(link_name == "panda_link7"):
                rpy_np = np.array([0,0,-math.pi/4])
                xyz_floats = [0,0,0.03679997502 + (0.028439417985386614/2)]
            xyz_np = 1000 * np.array(xyz_floats)
            R2 = self.eulerToR(rpy_np)
            # Create a 4x4 identity matrix
            transform_matrix = np.eye(4)

            # Replace the top-left 3x3 submatrix with the rotation matrix
            transform_matrix[:3, :3] = R2

            # Set the first three elements in the fourth column to the translation vector
            transform_matrix[:3, 3] = xyz_np

            # Set the bottom-right element to 1
            transform_matrix[3, 3] = 1.0
            open3d_mesh.transform(transform_matrix)

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
            t_matrix = self.camera_to_world_ @ robot_fk
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

    def setupMeshes(self,rgb,depth,segmentation):
        if(self.is_ready_):
            open3d_mesh = None        
            for [filename,link_name,rpy_str,xyz_str] in self.links_info_:
                if open3d_mesh is None:
                    open3d_mesh = self.setupMesh(filename,link_name,rpy_str,xyz_str)
                else:
                    open3d_mesh += self.setupMesh(filename,link_name,rpy_str,xyz_str)
            pcd = open3d_mesh.sample_points_uniformly(number_of_points=200000)
            pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points) / 1000)
            pcd_data = np.asarray(pcd.points)
            np.save('panda_gazebo_pointcloud.npy',pcd_data)
            point_cloud_msg = PointCloud2()
            point_cloud_msg.header = Header()
            point_cloud_msg.header.frame_id = "real_camera_link"
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
            self.fullPointcloudCallback(point_cloud_msg,rgb,depth,segmentation)

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
        
    def replace_nan_with_neighbors_average(self,array):
        def replace_function(subarray):
            center = subarray[4]
            if(center != np.nan):
                return center
            valid_values = subarray[subarray != -np.inf]
            if valid_values.size == 0:
                return np.nan
            else:
                return np.nanmean(valid_values)

        return generic_filter(array, replace_function, size=(3, 3), mode='constant', cval=np.nan)
        
    def listenerCallback(self,msg):
        if self.is_ready_:
            self.offline_ = True
            start_time = time.time()
            # path_array = msg.rgb.split('/')
            # online_input_folder = '/'.join(path_array[:-3]) + '/offline_ur5e_input'
            # if not os.path.exists(online_input_folder):
            #     os.makedirs(online_input_folder)
            # online_input_num_folder = online_input_folder + '/' + path_array[-2]
            # if not os.path.exists(online_input_num_folder):
            #     os.makedirs(online_input_num_folder)
            # input_rgb_path = online_input_folder + '/' +'/'.join(path_array[-2:])
            rgb_image = cv2.imread(msg.rgb)
            # cv2.imwrite(input_rgb_path,rgb_image)
            rgb_array = rgb_image.flatten().tolist()
            depth_image = np.load(msg.depth)
            # path_array = msg.depth.split('/')
            # input_depth_path = online_input_folder + '/' +'/'.join(path_array[-2:])
            # np.save(input_depth_path,depth_image)
            depth_array = depth_image.flatten().tolist()
            self.seg_file_ = msg.segmentation
            segmentation_image = cv2.imread(msg.segmentation)
            # path_array = msg.segmentation.split('/')
            # input_segmentation_path = online_input_folder + '/' +'/'.join(path_array[-2:])
            # cv2.imwrite(input_segmentation_path,segmentation_image)
            segmentation_ros_image = self.cv_bridge_.cv2_to_imgmsg(segmentation_image)
            joint_array = np.load(msg.joints).tolist()
            # path_array = msg.joints.split('/')
            # input_joints_path = online_input_folder + '/' +'/'.join(path_array[-2:])
            # np.save(input_joints_path,np.array(joint_array))
            input_file_robosuite_data_msg = InputFilesRobosuiteData()
            input_file_robosuite_data_msg.rgb = rgb_array
            input_file_robosuite_data_msg.depth_map = depth_array
            input_file_robosuite_data_msg.segmentation = segmentation_ros_image
            input_file_robosuite_data_msg.joints = joint_array
            self.listenerCallbackOnlineDebug(input_file_robosuite_data_msg)
            return
            rgb = msg.rgb
            depth = msg.depth
            segmentation = msg.segmentation
            joints = msg.joints
            joint_array = np.load(joints)
            gripper = joint_array[-1]
            joint_array = joint_array[:-1]
            
            ee_pose = self.ur5e_solver_.fk(np.array(joint_array))
            scipy_rotation = R.from_matrix(ee_pose[:3,:3])
            scipy_quaternion = scipy_rotation.as_quat()
            qout = self.panda_panda_gripper_solver_.ik(ee_pose,qinit=self.q_init_)
            self.q_init_ = qout
            # Hardcoded gripper
            qout_list = qout.tolist()
            panda_gripper_command = -0.05702400673569841 * gripper +  0.02670973458948458
            qout_list.append(panda_gripper_command)
            qout_msg = Float64MultiArray()
            qout_msg.data = qout_list
            self.ur5_and_panda_joint_command_publisher_.publish(qout_msg)
            self.joint_commands_callback(qout_msg)
            self.setupMeshes(rgb,depth,segmentation)
            end_time = time.time()

    def listenerCallbackOnlineDebug(self,msg):
        if(len(msg.data_pieces) == 2):
            start_time = time.time()
            self.i_ += 1
            online_input_folder = 'offline_ur5e_input'
            if not os.path.exists(online_input_folder):
                os.makedirs(online_input_folder)
            online_input_num_folder = online_input_folder + '/offline_ur5e_' + str(int(self.i_ / 2)) 
            if not os.path.exists(online_input_num_folder):
                os.makedirs(online_input_num_folder)
            left_msg = msg.data_pieces[0]
            right_msg = msg.data_pieces[1]
        elif(len(msg.data_pieces) == 1):
            left_msg = msg.data_pieces[0]
        left_rgb_np = self.cv_bridge_.imgmsg_to_cv2(left_msg.rgb)
        if(left_rgb_np.dtype == np.float32):
            self.float_image_ = True
            left_rgb_np = (left_rgb_np * 255).astype(np.uint8)
        
        left_rgb_np = self.cv_bridge_.imgmsg_to_cv2(left_msg.rgb)
        # rgb_np = np.array(msg.rgb,dtype=np.uint8).reshape((msg.segmentation.width,msg.segmentation.height,3))
        left_depth_np = np.array(left_msg.depth_map,dtype=np.float64).reshape((left_msg.rgb.height,left_msg.rgb.width))
        left_depth_np[np.isinf(left_depth_np) & (left_depth_np < 0)] = 0.01
        left_depth_np[np.isinf(left_depth_np) & (left_depth_np > 0)] = 10
        left_depth_np[np.isnan(left_depth_np)] = 0
        if(left_rgb_np.dtype == np.float32):
            self.float_image_ = True
            left_rgb_np = (left_rgb_np * 255).astype(np.uint8)

        right_rgb_np = self.cv_bridge_.imgmsg_to_cv2(right_msg.rgb)
        # rgb_np = np.array(msg.rgb,dtype=np.uint8).reshape((msg.segmentation.width,msg.segmentation.height,3))
        right_depth_np = np.array(right_msg.depth_map,dtype=np.float64).reshape((right_msg.rgb.height,right_msg.rgb.width))
        right_depth_np[np.isinf(right_depth_np) & (right_depth_np < 0)] = 0.01
        right_depth_np[np.isinf(right_depth_np) & (right_depth_np > 0)] = 10
        right_depth_np[np.isnan(right_depth_np)] = 0
        if(right_rgb_np.dtype == np.float32):
            self.float_image_ = True
            right_rgb_np = (right_rgb_np * 255).astype(np.uint8)

        panda_ur5_gripper_joints = np.array(msg.data_pieces[0].joints)
        real_ee_gripper_joint = panda_ur5_gripper_joints[-1]
        panda_ur5_gripper_joints = panda_ur5_gripper_joints[:-1]
        ee_pose = self.panda_ur5_gripper_solver_.fk(panda_ur5_gripper_joints)
        end_effector_rotation_with_no_translation = np.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
        ee_pose = ee_pose @ end_effector_rotation_with_no_translation
        scipy_rotation = R.from_matrix(ee_pose[:3,:3])
        scipy_quaternion = scipy_rotation.as_quat()
        qout = self.panda_panda_gripper_solver_.ik(ee_pose,qinit=self.q_init_)
        b_xyz = 1e-5
        b_rpy = 1e-3
        while(qout is None):
            b_xyz *= 10
            b_rpy *= 10
            qout = self.panda_panda_gripper_solver_.ik(ee_pose,qinit=self.q_init_,bx=b_xyz,by=b_xyz,bz=b_xyz,brx=b_rpy,bry=b_rpy,brz=b_rpy)
            if(b_xyz == 0.01):
                print("Couldn't find good IK")
                qout = self.q_init_
        print("Bound xyz: " + str(b_xyz))
        self.q_init_ = qout
        panda_ur5_arm_joints = panda_ur5_gripper_joints.tolist()
        panda_ur5_gripper_joint = 0.8 * real_ee_gripper_joint
        panda_ur5_gripper_joints = [panda_ur5_gripper_joint] * 6
        panda_arm_joints = qout.tolist()
        panda_gripper_joint = -0.04 * real_ee_gripper_joint + 0.04
        panda_gripper_joints = [panda_gripper_joint] * 2
        full_joint_list = []

        full_joint_list.extend(panda_arm_joints)
        full_joint_list.extend(panda_ur5_arm_joints)
        full_joint_list.extend(panda_gripper_joints)
        full_joint_list.extend(panda_ur5_gripper_joints)
        qout_msg = Float64MultiArray()
        qout_msg.data = full_joint_list
        self.ur5_and_panda_joint_command_publisher_.publish(qout_msg)
        self.left_real_rgb_ = left_msg.rgb
        self.right_real_rgb_ = right_msg.rgb

        self.left_real_depth_ = left_depth_np
        self.right_real_depth_ = right_depth_np
        self.real_qout_list_ = full_joint_list
        end_time = time.time()
        print("Algo time Part 1: " + str(end_time - start_time) + " seconds")

        # else:
        #     qout = self.panda_panda_gripper_solver_.ik(ee_pose,qinit=self.q_init_,bx=1e-3,by=1e-3,bz=1e-3)
        #     print("WARNING HIT IK ON FRANKA ERROR")
        

    def listenerCallbackData(self,msg):
        if self.is_ready_:
            start_time = time.time()
            segmentation_data = msg.segmentation
            
            segmentation_data = self.cv_bridge_.imgmsg_to_cv2(segmentation_data)

            rgb = msg.rgb
            rgb = np.array(rgb) \
                            .reshape((segmentation_data.shape[0], segmentation_data.shape[1], 3))
            
            

            depth_map = msg.depth_map
            depth_map = np.array(depth_map) \
                            .reshape(segmentation_data.shape)


            joint_array = msg.joints
            gripper = joint_array[-1]
            joint_array = joint_array[:-1]

            ee_pose = self.ur5e_solver_.fk(np.array(joint_array))
            qout = self.panda_panda_gripper_solver_.ik(ee_pose,qinit=self.q_init_)
            self.q_init_ = qout

            # Hardcoded gripper
            qout_list = qout.tolist()
            panda_gripper_command = -0.05702400673569841 * gripper +  0.02670973458948458
            qout_list.append(panda_gripper_command)
            qout_msg = Float64MultiArray()
            qout_msg.data = qout_list
            self.ur5_and_panda_joint_command_publisher_.publish(qout_msg)
            self.joint_commands_callback(qout_msg)
            self.setupMeshes(rgb, depth_map, segmentation_data)
            # end_time = time.time()
            # print("Total time: " + str(end_time - start_time) + " s")


    def joint_commands_callback(self, msg):
        self.joint_state_msg.header.stamp = self.get_clock().now().to_msg()
        #self.joint_state_msg.name = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint","wrist_1_joint", "wrist_2_joint", "wrist_3_joint","robotiq_85_left_knuckle_joint","robotiq_85_right_knuckle_joint","robotiq_85_left_inner_knuckle_joint","robotiq_85_right_inner_knuckle_joint","robotiq_85_left_finger_tip_joint","robotiq_85_right_finger_tip_joint"]  # Replace with your joint names
        self.joint_state_msg.name = ["panda_joint1", "panda_joint2", "panda_joint3","panda_joint4", "panda_joint5", "panda_joint6","panda_joint7","panda_finger_joint1","panda_finger_joint2"]
        msg.data.append(msg.data[-1])
        #msg.data.append(gripper_val)
        #msg.data.append(gripper_val)
        # for i in range(5):
        #     if(i == 1 or i == 4):
        #         msg.data.append(gripper_val)
        #     else:
        #         msg.data.append(gripper_val)
        self.joint_state_msg.position = msg.data
        self.thetas_ = {key:value for key,value in zip(self.joint_state_msg.name,msg.data)}
        # self.fks_ = self.chain_.forward_kinematics(self.thetas_)
        self.panda_joint_state_publisher_.publish(self.joint_state_msg)



    
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