import open3d as o3d
import numpy as np
# Load a PCD file
pcd = o3d.io.read_point_cloud("point_cloud.pcd")  # Replace with the path to your PCD file
gazebo_pcd = o3d.io.read_point_cloud("gazebo_pointcloud.pcd")
mesh_coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame()
#pcd.rotate(gazebo_rotation,[0,0,0])
# Visualize the point cloud

o3d.visualization.draw_geometries([pcd,gazebo_pcd,mesh_coordinate_frame])

