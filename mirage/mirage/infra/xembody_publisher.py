import numpy as np
import threading    
from typing import Any

class XEmbodyPublisher:
    """
    General interface for publishing RGBD images, segmentation masks, and joint angles to a ROS2 node.
    """
    
    def __init__(self) -> None:
        """
        Initializes the publisher code.
        """
        self._blocking_cond_variable = threading.Condition()
    
    def publish_to_ros_node(self, data: Any) -> None:
        """
        Publishes the RGB image, segmentation mask, and joint angles to the ROS2 node.
        :param data: The data to be published.        
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