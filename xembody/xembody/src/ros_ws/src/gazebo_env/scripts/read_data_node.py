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
from input_filenames_msg.msg import InputFiles

class ReadData(Node):
    def __init__(self):
        super().__init__('read_data_node')
        self.is_ready_ = False
        self.franka_info_folder_ = '/home/benchturtle/cross_embodiment_ws/src/gazebo_env/franka_1/'
        timer_period = 2
        self.timer_ = self.create_timer(timer_period, self.timerCallback)
        self.depth_file_ = "rgbd.npy"
        self.segmentation_ = "seg.jpg"
        self.joints_ = "joints.txt"
        self.publisher_ = self.create_publisher(InputFiles,'/input_files',1)
        self.is_ready_ = True
    
    def timerCallback(self):
        if self.is_ready_:
            depth_file = self.franka_info_folder_ + self.depth_file_
            segmentation = self.franka_info_folder_ + self.segmentation_
            joints = self.franka_info_folder_ + self.joints_
            input_file_msg = InputFiles()
            input_file_msg.depth_file = depth_file
            input_file_msg.segmentation = segmentation
            input_file_msg.joints = joints
            self.publisher_.publish(input_file_msg)



    
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