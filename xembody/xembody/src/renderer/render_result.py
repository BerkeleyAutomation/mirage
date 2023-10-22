import torch
import open3d as o3d

class RenderResult:

    def __init__(self,
                 rgb: torch.Tensor, 
                 segmentation_mask: torch.Tensor, 
                 point_cloud: o3d.geometry.PointCloud
                 ) -> None:
        """
        :param rgb: The RGB image of the rendered view.
        :param segmentation_mask: The segmentation mask of the robot in the rendered view.
        :param point_cloud: The point cloud of the rendered view.
        """
        self.rgb = rgb
        self.segmentation_mask = segmentation_mask
        self.point_cloud = point_cloud