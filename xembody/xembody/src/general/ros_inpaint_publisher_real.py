from input_filenames_msg.msg import InputFilesRealData
from xembody.src.general.ros_inpaint_publisher import ROSInpaintPublisher
import numpy as np

class ROSInpaintRealData:
    
    def __init__(self, rgb: np.array, depth_map: np.array, joints: np.array, camera_name: str = "camera"):
        """
        Contains the data for ROS Inpainting
        
        Args:
            rgb (np.array): W x H x 3 RGB image
            depth_map (np.array): W x H depth map
            joints (np.array): N + G size array containing all joint angles and gripper angles
            camera_name (str): name of the camera
        """
        self.rgb = rgb
        self.depth_map = depth_map
        self.joints = joints
        self.camera_name = camera_name

class ROSInpaintPublisherReal(ROSInpaintPublisher):
    """
    Handles the ROS2 communication for sending an RGBD image, segmentation mask, and joint angles
    to a node that performs inpainting on a target robot.
    """

    def __init__(self, use_diffusion: bool = False):
        """
        Initializes the ROS2 node.
        """
        super().__init__(use_diffusion=use_diffusion)

        self._publisher = self.node.create_publisher(
            InputFilesRealData, 'input_files_data_real', 1)

    def publish_to_ros_node(self, data: ROSInpaintRealData):
        """
        Publishes the RGB image, segmentation mask, and joint angles to the ROS2 node.
        :param data: The ROS Inpainting data to be published.
        """
        msg = InputFilesRealData()
        msg.rgb = self._cv_bridge.cv2_to_imgmsg(data.rgb)
        msg.depth_map = data.depth_map.flatten().tolist()

        joints_out = data.joints
        if type(joints_out) == np.ndarray:
            joints_out = joints_out.tolist()

        msg.joints = joints_out
        msg.camera_name = data.camera_name
        self._publisher.publish(msg)
