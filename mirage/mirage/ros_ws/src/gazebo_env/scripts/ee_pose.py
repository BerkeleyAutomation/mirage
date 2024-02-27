#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Float64MultiArray
import pathlib
import time
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
from tracikpy import TracIKSolver
import numpy as np
from ament_index_python.packages import get_package_share_directory


class EEPose(Node):

    def __init__(self):
        super().__init__('ee_pose')
        self.publisher_ = self.create_publisher(String, 'ee_pose', 10)
        self.joint_publisher_ = self.create_publisher(Float64MultiArray,'/forward_position_controller/commands',10)
        self.subscriber_ = self.create_subscription(
            String,
            'ee_pose',
            self.listener_callback,
            10)
        #self.image_subscriber_ = self.create_subscription(Image,'/camera/image_raw',self.image_listener_callback,10)
        msg = String()
        x = 0.6
        y = -0.2
        z = 0.525
        msg.data = str(x) + ' ' + str(y) + ' ' + str(z)
        self.orientation_ = [[[1,0,0],[0,1,0],[0,0,1]],[[0,0,-1],[0,1,0],[1,0,0]],[[1,0,0],[0,0,1],[0,-1,0]],[[-1,0,0],[0,0,-1],[0,-1,0]]]
        self.i = 0
        self.length_ = 3
        self.done_ = False
        self.wrote_video_ = False
        self.bridge_ = CvBridge()
        self.frames_ = []
        self.first_time_bool_ = True
        self.first_time_ = None
        self.last_time_ = None
        self.num_joints_ = 6
        urdf_file_path = get_package_share_directory('gazebo_env') + "/urdf/ur5e_analytical.urdf"
        self.ik_solver_ = TracIKSolver(
                        urdf_file_path,
                        "base_link",
                        "ft_frame",
                    )
        self.publisher_.publish(msg)

    def image_listener_callback(self,msg):
        if(self.first_time_bool_):
            self.first_time_bool_ = False
            self.first_time_ = time.time()
        if(not self.done_):
            frame = self.bridge_.imgmsg_to_cv2(msg,desired_encoding='bgr8')
            self.frames_.append(frame)
        elif(self.done_ and not self.wrote_video_):
            self.last_time_ = time.time()
            print("ITS OVER")
            print(len(self.frames_))
            print(str(self.last_time_ - self.first_time_))
            result = cv2.VideoWriter('filename.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         int(len(self.frames_)/(self.last_time_ - self.first_time_)), (640,480))
            for frame in self.frames_:
                result.write(frame)
            result.release()
            self.wrote_video_ = True

    def listener_callback(self, msg):
        if(self.first_time_bool_):
            self.first_time_bool_ = False
            time.sleep(1)
        print("IN HERE")
        xyz_str = msg.data
        xyz_arr = xyz_str.split(' ')
        x = float(xyz_arr[0])
        y = float(xyz_arr[1])
        z = float(xyz_arr[2])  
        print([x,y,z])
        print(self.orientation_[self.i][0])
        print(self.orientation_[self.i][1])
        rotation = np.array(self.orientation_[self.i]).T
        translation = [x,y,z]
        base = [0,0,0,1]
        translation = np.array([translation])
        base = np.array([base])
        ee_pose = np.concatenate((np.concatenate((rotation,translation.T),axis=1),base),axis=0)
        print(ee_pose)
        self.i += 1
        start_configuration = np.zeros(self.num_joints_)

        configuration = self.ik_solver_.ik(ee_pose, qinit=start_configuration)
        print(configuration)
        configuration = [float(i) for i in configuration]
        joint_message = Float64MultiArray()
        joint_message.data = configuration

        time.sleep(2)
        self.joint_publisher_.publish(joint_message)
        print("PRIME STUFF")
        if(self.i >= self.length_):
            #time.sleep(1)
            self.done_ = True

def main(args=None):
    rclpy.init(args=args)

    ee_pose = EEPose()

    rclpy.spin(ee_pose)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    ee_pose.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()