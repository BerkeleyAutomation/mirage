#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import trimesh
import open3d as o3d
from std_msgs.msg import Header, Bool
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
from input_filenames_msg.msg import InputFilesRealData, InputFilesRealDataMulti

class ReadData(Node):
    def __init__(self):
        super().__init__('read_data_node')
        self.is_ready_ = False
        self.cv_bridge_ = CvBridge()
        self.franka_info_folder_ = '/home/lawrence/cross_embodiment_ws/src/gazebo_env/ur5_check'
        self.check_npy_file_ = "/home/lawrence/cross_embodiment_ws/src/gazebo_env/ur5_check/check_ur5.npy"
        self.check_npy_ = np.load(self.check_npy_file_,allow_pickle=True).tolist()
        print("Left Intrinsic matrix: " + str(self.check_npy_['cam_intrinsic_matrix_left']))
        print("Left Extrinsic matrix: " + str(self.check_npy_['cam_extrinsic_matrix_left']))
        self.left_rgb_np_ = self.check_npy_['img_0']['img_left']
        self.left_depth_np_ = self.check_npy_['img_0']['depth']
        
        cv2.imwrite('fake_depth.png',self.normalize_depth_image(self.left_depth_np_))
        self.joints_np_ = np.array(self.check_npy_['img_0']['joint_angles'])
        self.left_rgb_ = self.cv_bridge_.cv2_to_imgmsg(self.left_rgb_np_,'bgr8')
        self.left_depth_ = self.left_depth_np_.astype('float64').flatten().tolist()
        self.joints_ = self.joints_np_.astype('float64').tolist()
        self.publisher_ = self.create_publisher(InputFilesRealDataMulti,'/input_files_data_real_multi',1)
        left_input_file_msg = InputFilesRealData()
        left_input_file_msg.rgb = self.left_rgb_
        left_input_file_msg.depth_map = self.left_depth_
        left_input_file_msg.joints = self.joints_
        left_input_file_msg.camera_name = "left"

        print("Right Intrinsic matrix: " + str(self.check_npy_['cam_intrinsic_matrix_right']))
        print("Right Extrinsic matrix: " + str(self.check_npy_['cam_extrinsic_matrix_right']))
        self.right_rgb_np_ = self.check_npy_['img_0']['img_right']
        self.right_depth_np_ = self.check_npy_['img_0']['depth']
        
        self.joints_np_ = np.array(self.check_npy_['img_0']['joint_angles'])
        self.right_rgb_ = self.cv_bridge_.cv2_to_imgmsg(self.right_rgb_np_,'bgr8')
        self.right_depth_ = self.right_depth_np_.astype('float64').flatten().tolist()
        self.joints_ = self.joints_np_.astype('float64').tolist()
        self.publisher_ = self.create_publisher(InputFilesRealDataMulti,'/input_files_data_real_multi',1)
        right_input_file_msg = InputFilesRealData()
        right_input_file_msg.rgb = self.right_rgb_
        right_input_file_msg.depth_map = self.right_depth_
        right_input_file_msg.joints = self.joints_
        right_input_file_msg.camera_name = "right"

        self.input_file_msg = InputFilesRealDataMulti()
        self.input_file_msg.data_pieces = [left_input_file_msg, right_input_file_msg]
        time.sleep(1)
        self.publisher_.publish(self.input_file_msg)
        print("Published")
        self.is_ready_ = True

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
    
def main(args=None):
    rclpy.init(args=args)

    read_data = ReadData()

    rclpy.spin(read_data)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    read_data.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()