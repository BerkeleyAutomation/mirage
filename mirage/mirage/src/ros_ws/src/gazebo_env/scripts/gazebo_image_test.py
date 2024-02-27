#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageSubscriberNode(Node):
    def __init__(self):
        super().__init__('image_subscriber_node')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',  # Replace with your image topic name
            self.image_callback,
            10  # Adjust the QoS profile as needed
        )
        self.subscription  # Prevent unused variable warning
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            # Convert the ROS Image message to a OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f"Error converting image message: {str(e)}")
            return

        # Save the received image using cv2.imwrite
        save_path = '/home/benchturtle/gazebo_img.jpg'  # Specify your save path
        cv2.imwrite(save_path, cv_image)
        self.get_logger().info(f"Image saved to {save_path}")

def main(args=None):
    rclpy.init(args=args)
    image_subscriber_node = ImageSubscriberNode()
    rclpy.spin(image_subscriber_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
