import os
import numpy as np
import pickle
from xembody.src.general.xembody_publisher import XEmbodyPublisher

class OrbitFilePublisher(XEmbodyPublisher):
    """
    Orbit specific file publisher that works with the ROS publishing code
    """
    
    def __init__(self, data_write_dir) -> None:
        """
        Initializes the publisher code.
        :param data_write_dir: The directory to write the data to.
        """
        super().__init__()
        self._data_write_file = os.path.join(data_write_dir, 'data.pkl')
        self._return_data_file = os.path.join(data_write_dir, 'return_data.pkl')
    
    def publish_to_ros_node(self, rgb_image: np.array, point_cloud: np.array, segmentation_mask: np.array, joint_angles: np.array):
        """
        Publishes the RGB image, segmentation mask, and joint angles to the ROS2 node.
        :param rgb_image: The RGBD image 4 channel numpy.
        :param point_cloud: The point cloud 3 channel numpy.
        :param segmentation_mask: The segmentation mask 1 channel numpy.
        :param joint_angles: The joint angles 1D numpy.
        """
        data = {
            'rgb_image': rgb_image,
            'point_cloud': point_cloud,
            'segmentation_mask': segmentation_mask,
            'joint_angles': joint_angles
        }
        with open(self._data_write_file, 'wb') as f:
            pickle.dump(data, f)
    
    def _get_inpainted_image_impl(self) -> np.array:
        """
        The implementation of getting an inpainted image.
        :return: The inpainted image.
        """
        if not self._is_item_available():
            return None
        inpainted_image = np.load(self._return_data_file, allow_pickle=True)['inpainted_image']
        os.remove(self._return_data_file)
        return inpainted_image
    
    def _is_item_available(self) -> bool:
        """
        Whether an item is available.
        :return: Whether an item is available.
        """
        return os.path.exists(self._return_data_file)