from xembody.src.renderer.renderer import Renderer
from xembody.src.renderer.render_result import RenderResult

from omni.isaac.orbit.sensors.camera import Camera, PinholeCameraCfg
from omni.isaac.orbit.sensors.camera.utils import create_pointcloud_from_rgbd
import omni.replicator.core as rep
import warp as wp
import torch
import numpy as np
import open3d as o3d

from typing import List
import transforms3d as t3d

class OrbitRenderer(Renderer):

    ROBOT_CLASS_NAME = 'robot'

    def __init__(self, 
                 robot_path: str, 
                 pinhole_camera_config: PinholeCameraCfg = None,
                 device: str = "cpu",
                 use_segmentation: bool = True,
                 resolution: List[int] = [480, 640]
                ):
        """
        :param robot_arm: The arm that will be rendered
        :param pinhole_camera_config: The configuration of the pinhole camera used internally.
        :param intrinsic_matrix: The intrinsic matrix of the camera.
        :param device: The device to use for running computations.
        """
        super().__init__()
        self._robot_path = robot_path
        self._device = device
        self._cam_config = pinhole_camera_config if pinhole_camera_config \
            else PinholeCameraCfg(
                sensor_tick=0,
                height=resolution[0],
                width=resolution[1],
                data_types=["rgb", "semantic_segmentation", "distance_to_image_plane"],
                usd_params=PinholeCameraCfg.UsdCameraCfg(
                    focal_length=24.0, focus_distance=400.0, horizontal_aperture=20.955, clipping_range=(0.1, 1.0e5)
                ),
            )
        self._cam = Camera(cfg=self._cam_config, device=self._device)
        
        self._robot_segmentation_label = None
        self._robot_prim = rep.get.prims(path_pattern=self._robot_path)
        # TODO FIX FOR FRANKA!
        if use_segmentation:
            with self._robot_prim:
                rep.modify.semantics([('class', OrbitRenderer.ROBOT_CLASS_NAME)])

    def initialize(self, translation: np.array = None, rot_quat: np.array = None, intrinsics: np.array = None) -> None:
        """
        Initializes the appropriate camera in the simulator.
        :param translation: The translation of the camera in world cameras.
        :param rot_quat: The rotation of the camera in the form of a quaternion that is consistent with the ROS coordinate system.
        :param intrinsics: The intrinsic matrix of the camera.
        """
        self._cam.spawn("/World/CameraSensor")
        if intrinsics is not None:
            self._cam.set_intrinsic_matrix(intrinsics)
        self._cam.initialize()
        if translation is None or rot_quat is None:
            eye_pos = [1.5, 1.5, 1.5] if translation is None else translation
            self._cam.set_world_pose_from_view(eye=eye_pos, target=[0.0, 0.0, 0.0])
        else:
            self._cam.set_world_pose_ros(translation, rot_quat)

    def render_current_view(self) -> RenderResult:
        """
        Renders the current view of the robot in a particular state.
        :return: RenderResult: The result of the rendering.
        """
        self._cam.update(dt=0.0)
        rgb = wp.to_torch(self._cam.data.output["rgb"])
        segmentation_data = self._cam.data.output["semantic_segmentation"]
        segmentation_mask = wp.to_torch(segmentation_data['data'])
        if self._robot_segmentation_label is None:
            for id, label in segmentation_data['info']['idToLabels'].items():
                if label['class'] == OrbitRenderer.ROBOT_CLASS_NAME:
                    self._robot_segmentation_label = int(id)
                    break
        if self._robot_segmentation_label is None:
            print('WARNING: Robot not found in Camera View')
        else:
            segmentation_mask = torch.where(segmentation_mask == self._robot_segmentation_label, 255, 0)
        
        depth = wp.to_torch(self._cam.data.output["distance_to_image_plane"])
        point_cloud = self.create_point_cloud_from_segmentation_mask(
            depth_image=depth,
            rgb_image=rgb,
            intrinsic_matrix=self._cam.data.intrinsic_matrix,
            segmentation_mask=segmentation_mask,
            translation=self._cam.data.position,
            orientation=self._cam.data.orientation
        )
        
        rgbd = torch.concat((rgb, depth), dim=2)
        return RenderResult(rgb=rgb, segmentation_mask=segmentation_mask, point_cloud=point_cloud, rgbd_image=rgbd)

    def create_point_cloud_from_segmentation_mask(
        self,
        depth_image: torch.Tensor, 
        rgb_image: torch.Tensor,
        intrinsic_matrix: np.ndarray, 
        segmentation_mask: torch.Tensor,
        translation: np.ndarray = None, 
        orientation: np.ndarray = None
    ) -> o3d.geometry.PointCloud:
        """
        Creates an Open3D point cloud from the segmentation mask.

        Args:
        - depth_image (torch.Tensor): The depth image.
        - rgb_image (torch.Tensor): The RGB image.
        - intrinsic_matrix (np.ndarray): The camera intrinsic matrix.
        - segmentation_mask (torch.Tensor): The segmentation mask.
        - translation (np.ndarray, optional): The translation for the camera position. Defaults to None.
        - orientation (np.ndarray, optional): The quaternion (w, x, y, z) for the camera position. Defaults to None.

        Returns:
        - o3d.geometry.PointCloud: The resulting Open3D point cloud.
        """
        depth_image_np = depth_image.cpu().numpy()
        rgb_image_np = rgb_image.cpu().numpy()
        segmentation_mask_np = segmentation_mask.cpu().numpy()
        # segmentation_mask_np = np.ones_like(segmentation_mask_np)

        h, w = depth_image_np.shape[:2]
        
        v, u = np.indices((h, w))
        valid_mask = segmentation_mask_np > 0
        valid_mask = valid_mask.squeeze()
        
        u_valid = u[valid_mask]
        v_valid = v[valid_mask]
        depth_valid = depth_image_np[valid_mask].squeeze()

        x = (u_valid - intrinsic_matrix[0, 2]) * depth_valid / intrinsic_matrix[0, 0]
        y = (v_valid - intrinsic_matrix[1, 2]) * depth_valid / intrinsic_matrix[1, 1]
        z = depth_valid

        points = np.column_stack((x, y, z))
        colors = rgb_image_np[valid_mask][:, :3]

        if translation is not None and orientation is not None:
            rotation_matrix = t3d.quaternions.quat2mat(orientation)
            transformed_points = np.dot(points, rotation_matrix.T) + translation
            points = transformed_points

        point_cloud = o3d.geometry.PointCloud()
        point_cloud.points = o3d.utility.Vector3dVector(points)
        point_cloud.colors = o3d.utility.Vector3dVector(colors / 255.0)
        return point_cloud
