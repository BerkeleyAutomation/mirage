from input_filenames_msg.msg import InputFilesSimData
from xembody.src.general.ros_inpaint_publisher import ROSInpaintPublisher
from xembody.src.general.gripper_interpolator import GripperInterpolator
import numpy as np

class ROSInpaintSimData:
    
    def __init__(self, rgb: np.array, depth_map: np.array, segmentation: np.array, ee_pose: np.array, gripper_angles: np.array, camera_name: str = "camera"):
        """
        Contains the data for ROS Inpainting
        
        Args:
            rgb (np.array): W x H x 3 RGB image
            depth_map (np.array): W x H depth map
            segmentation (np.array): W x H segmentation mask
            ee_pose (np.array): 4x4 end effector pose matrix
            gripper_angles (np.array): gripper joint angles that are not interpolated
            camera_name (str): name of the camera
        """
        self.rgb = rgb
        self.depth_map = depth_map
        self.segmentation = segmentation
        self.ee_pose = ee_pose
        self.gripper_angles = gripper_angles
        self.camera_name = camera_name
        
class ROSInpaintPublisherSim(ROSInpaintPublisher):
    """
    Handles the ROS2 communication for sending an RGBD image, segmentation mask, and joint angles
    to a node that performs inpainting on a target robot.
    """

    def __init__(self):
        """
        Initializes the ROS2 node.
        """
        super().__init__()

        self._publisher = self.node.create_publisher(
            InputFilesSimData, 'input_files_data_sim', 1)
        
        # TODO: generalize this
        self.gripper_interpolator = GripperInterpolator('panda', 'ur5')

    def publish_to_ros_node(self, data: ROSInpaintSimData):
        """
        Publishes the RGB image, segmentation mask, and joint angles to the ROS2 node.
        :param data: The ROS Inpainting data to be published.
        """
        msg = InputFilesSimData()
        msg.rgb = self._cv_bridge.cv2_to_imgmsg(data.rgb)
        msg.depth_map = data.depth_map.flatten().tolist()
        segmentation_mask = data.segmentation
        if segmentation_mask.max() <= 1:
            segmentation_mask = (segmentation_mask * 255).astype(np.uint8)
        msg.segmentation = segmentation_mask.flatten().tolist()
        msg.ee_pose = data.ee_pose.flatten().tolist()
        msg.interpolated_gripper = self.gripper_interpolator.interpolate_gripper(data.gripper_angles).flatten().tolist()
        msg.camera_name = data.camera_name
        self._publisher.publish(msg)