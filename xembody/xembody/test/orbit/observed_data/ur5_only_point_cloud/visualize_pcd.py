import open3d as o3d

# Load a PCD file
pcd = o3d.io.read_point_cloud("point_cloud.pcd")  # Replace with the path to your PCD file
import pdb
pdb.set_trace()
# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])
