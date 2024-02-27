#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import trimesh
import open3d as o3d
from std_msgs.msg import Header, Bool, Float64MultiArray, Int16
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
from input_filenames_msg.msg import InputFilesRobosuite, InputFilesRobosuiteData, InputFilesDiffusionData

class ReadData(Node):
    def __init__(self):
        super().__init__('read_data_node')
        self.is_ready_ = False
        self.franka_info_folder_ = '/home/benchturtle/diffusion_data_noisy'
        self.rgb_folder_ = self.franka_info_folder_ + '/ur5e_rgb'
        self.rgb_folder_list_ = os.listdir(self.rgb_folder_)
        self.rgb_ = "rgb.png"
        self.depth_ = "depth.npy"
        self.segmentation_ = "seg.png"
        self.joints_ = "joints.npy"
        self.cv_bridge_ = CvBridge()
        self.publisher_ = self.create_publisher(InputFilesDiffusionData,'/input_files_data',1)
        self.i_ = 0
        self.j_ = 0
        self.i_limit_ = len([item for item in self.rgb_folder_list_ if os.path.isdir(os.path.join(self.rgb_folder_, item))])
        self.j_limits_ = []
        for i in range(self.i_limit_):
            str_i = str(i)
            rgb_traj_folder = self.rgb_folder_ + '/' + str_i
            image_list = os.listdir(rgb_traj_folder)
            j_limit = len(image_list)
            self.j_limits_.append(j_limit)
        self.first_time_ = True
        self.is_ready_ = True
        self.sendInput()
    
    def sendInput(self,msg=None):
        for i in range(self.i_limit_):
            for j in range(self.j_limits_[i]):
                print("Publishing Demo " + str(i) + " " + str(j) + '/' + str(self.j_limits_[i]))
                franka_folder = self.franka_info_folder_
                rgb_file = franka_folder + '/ur5e_rgb/' + str(i) + '/' + str(j) + '.jpg'
                depth_file = franka_folder + '/ur5e_depth/' + str(i) + '/' + str(j) + '.npy'
                seg_file = franka_folder + '/ur5e_mask/' + str(i) + '/' + str(j) + '.jpg'
                joint_file = franka_folder + '/ur5e_joint_gripper_pose/' + str(i) + '/' + str(j) + '.txt'
                joint_read_file = open(joint_file,"r")
                joint_file_contents = joint_read_file.read()
                joint_list = [float(x) for x in joint_file_contents[1:-1].split()]
                mod_joint_list = joint_list[:6] + [joint_list[-1]]
                rgb = cv2.imread(rgb_file)
                depth = np.load(depth_file)
                seg = cv2.imread(seg_file)
                rgb_array = rgb.flatten().tolist()
                depth_array = depth.flatten().tolist()
                segmentation_ros_image = self.cv_bridge_.cv2_to_imgmsg(seg)
                input_file_robosuite_data_msg = InputFilesDiffusionData()
                input_file_robosuite_data_msg.rgb = rgb_array
                input_file_robosuite_data_msg.depth_map = depth_array
                input_file_robosuite_data_msg.segmentation = segmentation_ros_image
                input_file_robosuite_data_msg.joints = mod_joint_list
                demo_num_msg = Int16()
                traj_num_msg = Int16()
                demo_num_msg.data = i
                traj_num_msg.data = j
                input_file_robosuite_data_msg.demo_num = demo_num_msg
                input_file_robosuite_data_msg.traj_num = traj_num_msg
                self.publisher_.publish(input_file_robosuite_data_msg)
                time.sleep(0.5)

    def timerCallback(self):
        if self.is_ready_ and self.i_ < 100:
            franka_folder = self.franka_info_folder_+str(int(self.i_ / 2)) +'/'
            rgb = franka_folder + self.rgb_
            depth = franka_folder + self.depth_
            segmentation = franka_folder + self.segmentation_
            joints = franka_folder + self.joints_
            input_file_msg = InputFilesRobosuite()
            input_file_msg.rgb = rgb
            input_file_msg.depth = depth
            input_file_msg.segmentation = segmentation
            input_file_msg.joints = joints
            self.publisher_.publish(input_file_msg)
            self.i_ += 1



    
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