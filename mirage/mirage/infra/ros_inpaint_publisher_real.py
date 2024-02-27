from input_filenames_msg.msg import InputFilesRealDataMulti, InputFilesRealData
from mirage.src.infra.ros_inpaint_publisher import ROSInpaintPublisher
import numpy as np
from typing import List

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
            InputFilesRealDataMulti, 'input_files_data_real', 1)

    def publish_to_ros_node(self, data: List[ROSInpaintRealData]):
        """
        Publishes the RGB image, segmentation mask, and joint angles to the ROS2 node.
        :param data: The ROS Inpainting data to be published.
        """
        msg = InputFilesRealDataMulti()

        out_msg_data = []
        for inpaint_data in data:
            current_data_msg = InputFilesRealData()
            current_data_msg.rgb = self._cv_bridge.cv2_to_imgmsg(inpaint_data.rgb)
            current_data_msg.depth_map = inpaint_data.depth_map.flatten().tolist()

            joints_out = inpaint_data.joints
            if type(joints_out) == np.ndarray:
                joints_out = joints_out.tolist()

            current_data_msg.joints = joints_out
            current_data_msg.camera_name = inpaint_data.camera_name
            out_msg_data.append(current_data_msg)
        msg.data_pieces = out_msg_data
        self._publisher.publish(msg)
