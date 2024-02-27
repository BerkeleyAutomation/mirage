#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import trimesh
import open3d as o3d
from std_msgs.msg import Header
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
from input_filenames_msg.msg import InputFilesFrankaToFranka
import h5py
from std_msgs.msg import Int16

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
from input_filenames_msg.msg import InputFilesRobosuite

class ReadData(Node):
    def __init__(self):
        super().__init__('read_data_node')
        self.is_ready_ = False
        self.hdf5_ = '/home/benchturtle/cross_embodiment_ws/src/gazebo_env/franka_to_franka/image_v141.hdf5'
        self.rgb_ = "rgb.png"
        self.depth_ = "depth.npy"
        self.segmentation_ = "seg.png"
        self.joints_ = "joints.npy"
        self.cv_bridge_ = CvBridge()
        self.publisher_ = self.create_publisher(InputFilesFrankaToFranka,'/input_data',1)
        self.i_ = 0
        self.j_ = 0
        
        #self.next_input_subscriber = self.create_subscription(Bool,'/ready_for_next_input',self.sendInput,1)
        self.file_  = h5py.File(self.hdf5_,'r+')
        self.i_limit_ = len(self.file_['data'].keys())
        self.demo_list_ = [f"demo_{i}" for i in range(0, self.i_limit_)]
        self.obses_ = []
        self.j_limits_ = []
        for demo_str in self.demo_list_:
            single_obs = self.file_['data'][demo_str]['obs']
            j_limit = single_obs['agentview_image'].shape[0]
            self.obses_.append(self.file_['data'][demo_str]['obs'])
            self.j_limits_.append(j_limit)
        self.sendInput()
        self.is_ready_ = True

    def sendInput(self,msg=None):
        for i in range(self.i_limit_):
            for j in range(self.j_limits_[i]):
                print("Publishing Demo " + str(i) + " " + str(j) + '/' + str(self.j_limits_[i]))
                rgb = self.obses_[i]['agentview_image'][j]
                joints = self.obses_[i]['robot0_joint_pos'][j]
                gripper = abs(self.obses_[i]['robot0_gripper_qpos'][j][0])
                joints_and_gripper = np.append(joints,gripper)
                input_msg = InputFilesFrankaToFranka()
                input_msg.rgb = self.cv_bridge_.cv2_to_imgmsg(rgb)
                input_msg.joints = joints_and_gripper.tolist()
                demo_num_msg = Int16()
                traj_num_msg = Int16()
                demo_num_msg.data = i
                traj_num_msg.data = j
                input_msg.demo_num = demo_num_msg
                input_msg.traj_num = traj_num_msg
                self.publisher_.publish(input_msg)
                time.sleep(1)

    



    
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