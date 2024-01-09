import numpy as np
import threading

class XEmbodyPublisher:
    """
    General interface for publishing RGBD images, segmentation masks, and joint angles to a ROS2 node.
    """
    
    def __init__(self) -> None:
        """
        Initializes the publisher code.
        """
        self._blocking_cond_variable = threading.Condition()
    
    def publish_to_ros_node(self, rgb_image: np.array, depth_map: np.array, segmentation_mask: np.array, joint_angles: np.array):
        """
        Publishes the RGB image, segmentation mask, and joint angles to the ROS2 node.
        :param rgb_image: The RGBD image 4 channel numpy.
        :param depth_map: The depth map.
        :param segmentation_mask: The segmentation mask 1 channel numpy.
        :param joint_angles: The joint angles 1D numpy.
        """
        pass
    
    def _get_inpainted_image_impl(self) -> np.array:
        """
        The implementation of getting an inpainted image.
        :return: The inpainted image.
        """
        pass
    
    def _is_item_available(self) -> bool:
        """
        Whether an item is available.
        :return: Whether an item is available.
        """
        pass
    
    def get_inpainted_image(self, blocking: bool) -> np.array:
        """
        Gets the inpainted image.
        :param blocking: Whether to block until the inpainted image is received.
        :return: The inpainted image.
        """
        out_image = None
        if blocking:
            with self._blocking_cond_variable:
                self._blocking_cond_variable.wait_for(self._is_item_available)
                out_image = self._get_inpainted_image_impl()
        else:
            out_image = self._get_inpainted_image_impl()
        return out_image