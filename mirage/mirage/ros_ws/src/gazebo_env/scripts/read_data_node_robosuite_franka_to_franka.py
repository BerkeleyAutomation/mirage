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
from std_msgs.msg import Int8

class ReadData(Node):
    def __init__(self):
        super().__init__('read_data_node')
        self.is_ready_ = False
        self.hdf5_ = '/home/benchturtle/cross_embodiment_ws/src/gazebo_env/franka_to_franka/image_v141.hdf5'
        timer_period = 2
        self.timer_ = self.create_timer(timer_period, self.timerCallback)
        self.publisher_ = self.create_publisher(InputFilesFrankaToFranka,'/input_data',1)
        self.cv_bridge_ = CvBridge()
        self.is_ready_ = True
    
    def timerCallback(self):
        if(self.is_ready_):
            with h5py.File(self.hdf5_, 'r+') as file:
                for i in range(len(file['data'].keys())):
                    demo_str = 'demo_'+str(i)
                    obs = file['data'][demo_str]['obs']
                    for j in range(2 * obs['agentview_image'].shape[0]):
                        rgb = obs['agentview_image'][int(j / 2)]
                        joints = obs['robot0_joint_pos'][int(j / 2)]
                        gripper = abs(obs['robot0_gripper_qpos'][int(j / 2)][0])
                        joints_and_gripper = np.append(joints,gripper)
                        input_msg = InputFilesFrankaToFranka()
                        input_msg.rgb = self.cv_bridge_.cv2_to_imgmsg(rgb)
                        input_msg.joints = joints_and_gripper.tolist()
                        demo_num_msg = Int8()
                        traj_num_msg = Int8()
                        demo_num_msg.data = i
                        traj_num_msg.data = int(j / 2)
                        input_msg.demo_num = demo_num_msg
                        input_msg.traj_num = traj_num_msg

                        self.publisher_.publish(input_msg)
                        print("Publishing Demo " + str(i) + " " + str(int(j / 2)) + '/' + str(obs['agentview_image'].shape[0]))
                        time.sleep(2) 
            print("Done")
            exit()



    
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