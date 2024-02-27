from input_filenames_msg.msg import InputFilesSimData
from mirage.src.infra.ros_inpaint_publisher import ROSInpaintPublisher
from mirage.mirage.src.gripper_interpolation.gripper_interpolator import GripperInterpolator
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

    def __init__(self, source_robot_info: str, target_robot_info: str):
        """
        Initializes the ROS2 node.
        :param source_robot_info: the information about the source robot to determine which interpolation scheme to use
        :param target_robot_info: the information about the target robot to determine which interpolation scheme to use
        """
        super().__init__(uses_single_img=True)

        self._publisher = self.node.create_publisher(
            InputFilesSimData, '/input_files_data_sim', 1)

        # TODO: generalize this
        self.gripper_interpolator = GripperInterpolator(source_robot_info, target_robot_info, ['/home/mirage/x-embody/xembody/xembody_robosuite/paired_trajectories_collection/gripper_interpolation_results_no_task_diff.pkl',
                                                                                               '/home/mirage/x-embody/xembody/xembody_robosuite/paired_trajectories_collection/gripper_interpolation_results_20_rollouts.pkl'])
        # self.gripper_interpolator = GripperInterpolator('panda', 'panda', ['/home/mirage/x-embody/xembody/xembody_robosuite/paired_trajectories_collection/gripper_interpolation_results_no_task_diff.pkl'])
        # self.gripper_interpolator = GripperInterpolator('panda', 'ur5', '/home/mirage/x-embody/xembody/xembody_robosuite/paired_trajectories_collection/gripper_interpolation_results_no_task_diff.pkl')

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
        # msg.camera_name = data.camera_name
        self._publisher.publish(msg)
        print("Published message")