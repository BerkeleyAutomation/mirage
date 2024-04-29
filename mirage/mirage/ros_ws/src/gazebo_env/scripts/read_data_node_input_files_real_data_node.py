#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from input_filenames_msg.msg import InputFilesRealData, InputFilesRealDataMulti
import cv2
from cv_bridge import CvBridge

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(InputFilesRealDataMulti, 'input_files_data_real', 10)
        self.ur5_gripper_filepath_ = '/home/lawrence/xembody/xembody/xembody/xembody/src/ros_ws/src/gazebo_env/test_data/2024-04-10-211323.jpg'
        self.cv_bridge_ = CvBridge()
        self.ur5_gt_image_ = cv2.imread(self.ur5_gripper_filepath_)
        test_image = cv2.rotate(self.ur5_gt_image_, cv2.ROTATE_180)
        height, width, _ = test_image.shape
        cropped_left_image = test_image[:, :width // 2]
        cropped_left_image = cv2.resize(cropped_left_image, (1280,720))
        self.ros_ur5_left_image_ = self.cv_bridge_.cv2_to_imgmsg(cropped_left_image)
        cropped_right_image = test_image[:, width // 2:]
        cropped_right_image = cv2.resize(cropped_right_image, (1280,720))
        self.ros_ur5_right_image_ = self.cv_bridge_.cv2_to_imgmsg(cropped_right_image)
        self.joints_ = [-0.56332457,  0.06948572,  0.5227356,  -2.26363611, -0.11123186,  2.28321218, -0.09410787,0.0]
        self.i = 0
        self.timer_callback()

    def timer_callback(self):
        msg = InputFilesRealDataMulti()
        msg_left_data = InputFilesRealData()
        msg_left_data.joints = self.joints_
        msg_left_data.rgb = self.ros_ur5_left_image_
        msg.data_pieces.append(msg_left_data)
        msg_right_data = InputFilesRealData()
        msg_right_data.joints = self.joints_
        msg_right_data.rgb = self.ros_ur5_right_image_
        msg.data_pieces.append(msg_right_data)
        self.publisher_.publish(msg)
        print("Published")


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()