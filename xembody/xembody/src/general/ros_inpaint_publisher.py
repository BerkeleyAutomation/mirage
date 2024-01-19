import rclpy
from sensor_msgs.msg import Image, PointCloud2
from cv_bridge import CvBridge
from xembody.src.general.xembody_publisher import XEmbodyPublisher
from sensor_msgs.msg import PointCloud2, PointField
import cv2
import numpy as np
import threading
import message_filters

class ROSInpaintPublisher(XEmbodyPublisher):
    """
    Handles the ROS2 communication for receiving inpainted images from a target robot. 
    Publishing data is left to sim or real subclasses.
    """

    def __init__(self, use_diffusion: bool = False):
        """
        Initializes the ROS2 node.
        """
        super().__init__()
        rclpy.init(args=None)
        self.node = rclpy.create_node('ros_inpaint_publisher')
        
        self._use_diffusion = use_diffusion

        self.spin_thread = threading.Thread(target=rclpy.spin, args=(self.node,))
        self.spin_thread.start()

        self._pcd_publisher = self.node.create_publisher(
            PointCloud2, 'point_cloud_output', 1)
        
        self._analytic_inpaint_subscriber = message_filters.Subscriber(self.node, Image, 'inpainted_image')
        self._mask_subscriber = message_filters.Subscriber(self.node, Image, 'full_mask_image')
        self._time_sync = message_filters.ApproximateTimeSynchronizer(
            [self._analytic_inpaint_subscriber, self._mask_subscriber], 
            10, 
            0.1
        )
        self._time_sync.registerCallback(self._inpaint_image_callback)
        
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

    def _inpaint_image_callback(self, inpaint_msg, mask_msg):
        """
        Callback function for the inpainted image.
        :param msg: The ROS2 message.
        """
        self.node.get_logger().info('Received inpainted & mask images')
        with self._internal_lock:
            inpainted_msg = self._cv_bridge.imgmsg_to_cv2(inpaint_msg)\
            mask_msg = self._cv_bridge.imgmsg_to_cv2(mask_msg)
            self._cv_image = inpainted_msg
            
            if self._use_diffusion:
                # TODO: add the diffusion code here
                # self._cv_image = diffusion output
                pass
            
            with self._blocking_cond_variable:
                self._blocking_cond_variable.notify()