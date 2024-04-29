#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np
import time as time

class JointCommandsPublisher(Node):
    def __init__(self):
        super().__init__('joint_commands_publisher')
        self.publisher_ = self.create_publisher(Float64MultiArray, '/joint_commands', 10)
        self.ur5_subscriber_ = self.create_subscription(Image,'/ur5_left_camera/depth/image_raw',self.ur5_image_callback,10)
        self.panda_subscriber_ = self.create_subscription(Image,'/panda_left_camera/depth/image_raw',self.panda_image_callback,10)
        self.ur5_gripper_filepath_ = '/home/lawrence/xembody/xembody/xembody/xembody/src/ros_ws/src/gazebo_env/test_data/2024-04-10-211323.jpg'
        self.panda_filepath_ = '/home/lawrence/xembody/xembody/xembody/xembody/src/ros_ws/src/gazebo_env/test_data/2024-04-15-005029.jpg'
        self.cv_bridge_ = CvBridge()
        self.ur5_gt_image_ = cv2.imread(self.ur5_gripper_filepath_)
        self.panda_gt_image_ = cv2.imread(self.panda_filepath_)
        self.is_ready_ = False
        self.timer = self.create_timer(1, self.publish_joint_commands)

    def ur5_image_callback(self,msg):
        if self.is_ready_:
            self.get_logger().info('Received image message')
            test_image = cv2.rotate(self.ur5_gt_image_, cv2.ROTATE_180)
            height, width, _ = test_image.shape
            cropped_image = test_image[:, :width // 2]
            cropped_image = cv2.resize(cropped_image, (1280,720))
            cv2.imwrite('output.jpg',cropped_image)
            depth_image = self.cv_bridge_.imgmsg_to_cv2(msg)
            real_seg_np = (depth_image < 8).astype(np.uint8)
            real_seg_255_np = 255 * real_seg_np
            translation_matrix = np.float32([[1, 0, 40], [0, 1, 30]])
            translated_mask = cv2.warpAffine(real_seg_255_np, translation_matrix, (real_seg_255_np.shape[1], real_seg_255_np.shape[0]))
            translated_mask[:30,579:real_seg_255_np.shape[1]] = 255
            translated_mask[:30,76:368] = 255
            cv2.imwrite('output2.jpg',translated_mask)

    def panda_image_callback(self,msg):
        if self.is_ready_:
            self.get_logger().info('Received image message')
            test_image = cv2.rotate(self.panda_gt_image_, cv2.ROTATE_180)
            height, width, _ = test_image.shape
            cropped_image = test_image[:, :width // 2]
            cropped_image = cv2.resize(cropped_image, (1280,720))
            cv2.imwrite('output3.jpg',cropped_image)
            depth_image = self.cv_bridge_.imgmsg_to_cv2(msg)
            real_seg_np = (depth_image < 8).astype(np.uint8)
            real_seg_255_np = 255 * real_seg_np
            translation_matrix = np.float32([[1, 0, 0], [0, 1, 30]])
            translated_mask = cv2.warpAffine(real_seg_255_np, translation_matrix, (real_seg_255_np.shape[1], real_seg_255_np.shape[0]))
            translated_mask[:30,:] = 255
            cv2.imwrite('output4.jpg',translated_mask)
            import pdb
            pdb.set_trace()

    def publish_joint_commands(self):
        msg = Float64MultiArray()
        # Example joint commands, you can modify this list according to your needs
        joint_commands = [-0.56332457,  0.06948572,  0.5227356,  -2.26363611, -0.11123186,  2.28321218, -0.09410787,-0.56332457,  0.06948572,  0.5227356,  -2.26363611, -0.11123186,  2.28321218, -0.09410787,0.04,0.04,0.0,0.0,0.0,0.0,0.0,0.0]
        msg.data = joint_commands
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing joint commands: %s' % joint_commands)
        time.sleep(1)
        self.is_ready_ = True

def main(args=None):
    rclpy.init(args=args)
    joint_commands_publisher = JointCommandsPublisher()
    rclpy.spin(joint_commands_publisher)
    joint_commands_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
