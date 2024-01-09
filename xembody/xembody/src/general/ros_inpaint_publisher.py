import rclpy
from sensor_msgs.msg import Image, PointCloud2
from input_filenames_msg.msg import InputFilesRobosuiteData
from cv_bridge import CvBridge
from xembody.src.general.xembody_publisher import XEmbodyPublisher
from sensor_msgs.msg import PointCloud2, PointField
import cv2
import numpy as np
import threading

class ROSInpaintPublisher(XEmbodyPublisher):
    """
    Handles the ROS2 communication for sending an RGBD image, segmentation mask, and joint angles
    to a node that performs inpainting on a target robot.
    """

    def __init__(self):
        """
        Initializes the ROS2 node.
        """
        super().__init__()
        rclpy.init(args=None)
        self.node = rclpy.create_node('ros_inpaint_publisher')

        self.spin_thread = threading.Thread(target=rclpy.spin, args=(self.node,))
        self.spin_thread.start()

        self._publisher = self.node.create_publisher(
            InputFilesRobosuiteData, 'input_files_data', 1)
        self._pcd_publisher = self.node.create_publisher(
            PointCloud2, 'point_cloud_output', 1)
        self._subscriber = self.node.create_subscription(
            Image, 'inpainted_image', self._inpaint_image_callback, 1)
        self._cv_bridge = CvBridge()
        self._cv_image = None
        self._internal_lock = threading.Lock()

    def _create_pointcloud_msg(self, points: np.array) -> PointCloud2:
        """
        Creates a point cloud message from the points.
        :param points: The points.
        :return: The point cloud message.
        """
        msg = PointCloud2()
        msg.header.frame_id = "world"
        msg.header.stamp = self.node.get_clock().now().to_msg()
        msg.height = 1
        msg.width = points.shape[0]
        msg.fields = [
            PointField(name="x", offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name="y", offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name="z", offset=8, datatype=PointField.FLOAT32, count=1),
        ]
        msg.is_bigendian = False
        msg.point_step = 12
        msg.row_step = msg.point_step * msg.width
        msg.is_dense = True
        msg.data = points.astype(np.float32).tobytes()
        return msg


    def publish_to_ros_node(self, rgb_image: np.array, depth_map: np.array, segmentation_mask: np.array, joint_angles: np.array):
        """
        Publishes the RGB image, segmentation mask, and joint angles to the ROS2 node.
        :param rgb_image: The RGBD image 4 channel numpy.
        :param depth_map: The depth map.
        :param segmentation_mask: The segmentation mask 1 channel numpy.
        :param joint_angles: The joint angles 1D numpy.
        """
        msg = InputFilesRobosuiteData()

        # if rgb_image.dtype == np.float64 or rgb_image.dtype == np.float32:
        #     rgb_image = (rgb_image * 255).astype(np.uint8)

        # msg.rgb = rgb_image.flatten().tolist()

        # msg.depth_map = np.array(depth_map).flatten().tolist()

        # msg.segmentation = self._cv_bridge.cv2_to_imgmsg(segmentation_mask)
        msg.rgb = rgb_image.flatten().tolist()

        msg.depth_map = depth_map.flatten().tolist()

        if segmentation_mask.max() <= 1:
            segmentation_mask = (segmentation_mask * 255).astype(np.uint8)
        msg.segmentation = self._cv_bridge.cv2_to_imgmsg(segmentation_mask)
        msg.joints = joint_angles.tolist()
        self._publisher.publish(msg)

    def _get_inpainted_image_impl(self) -> np.array:
        """
        The implementation of getting an inpainted image.
        :return: The inpainted image.
        """
        with self._internal_lock:
            out_img = self._cv_image
            self._cv_image = None
        return out_img
    
    def _is_item_available(self) -> bool:
        """
        Whether an item is available.
        :return: Whether an item is available.
        """
        return self._cv_image is not None

    def _inpaint_image_callback(self, msg):
        """
        Callback function for the inpainted image.
        :param msg: The ROS2 message.
        """
        self.node.get_logger().info('Received inpainted image')
        with self._internal_lock:
            self._cv_image = self._cv_bridge.imgmsg_to_cv2(msg)
            with self._blocking_cond_variable:
                self._blocking_cond_variable.notify()