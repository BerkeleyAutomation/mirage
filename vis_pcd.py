import open3d as o3d
import numpy as np
# Load the .npy file containing the point cloud data
point_cloud_data = np.load('pcd.npy')
# Create an Open3D point cloud from the loaded data
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(point_cloud_data)
# Visualize the point cloud
o3d.visualization.draw_geometries([point_cloud])