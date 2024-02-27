import cv2
import numpy as np
import json
import open3d as o3d
from scipy.spatial.transform import Rotation as R

def normalize_depth_image(depth_image):
  # Define the minimum and maximum depth values in your depth image
  min_depth = np.min(depth_image)
  max_depth = np.max(depth_image)

  # Normalize the depth image to the range [0, 1]
  normalized_depth_image = (depth_image - min_depth) / (max_depth - min_depth)

  # Optionally, you can scale the normalized image to a different range
  # For example, to scale it to [0, 255] for visualization:
  normalized_depth_image = (normalized_depth_image * 255).astype(np.uint8)
  return normalized_depth_image

ur5e_output = np.load('UR5e_output3.npy',allow_pickle=True)
# Convert dictionary to a string
ur5e_output_dict = ur5e_output.item()
joints = ur5e_output_dict['joint_angles']
np.save('joints.npy',joints)
print(joints)
ee_pos = ur5e_output_dict['robot_eef_pos']
print(ee_pos)
ee_quat = ur5e_output_dict['robot_eef_quat']
print(ee_quat)
rotation_ee = R.from_quat(ee_quat)
rotation_matrix_ee = rotation_ee.as_matrix()
print(rotation_matrix_ee)
translation_ee = np.array([1.6,0,1.45])
agentview_image = ur5e_output_dict['agentview']['rgb']
agentview_image = cv2.cvtColor(agentview_image,cv2.COLOR_BGR2RGB)
cv2.imwrite('rgb.png',agentview_image)
points = ur5e_output_dict['agentview']['points']
points_np = np.array(points)
points_np = points_np[:,:3]


# Creating an Open3D PointCloud object from the numpy array
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points_np)
color = [1.0, 0.0, 0.0]
pcd.colors = o3d.utility.Vector3dVector(np.tile(color, (points_np.shape[0], 1)))
world_to_camera = np.array([[-5.55111512e-17,  2.58174524e-01, -9.66098295e-01,
         1.60000000e+00],
       [ 1.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         0.00000000e+00],
       [ 0.00000000e+00, -9.66098295e-01, -2.58174524e-01,
         1.45000000e+00],
       [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         1.00000000e+00]])
pcd.transform(np.linalg.inv(world_to_camera))
# Convert Open3D point cloud to NumPy array
pcd_points = np.asarray(pcd.points)
print(pcd_points.shape)
np.save('pointcloud.npy',pcd_points)
robosuite_seg = ur5e_output_dict['agentview']['seg']
robosuite_seg *= 255
cv2.imwrite('seg.png',robosuite_seg)
real_depth_map = ur5e_output_dict['agentview']['real_depth_map']
np.save('depth.npy',real_depth_map)
