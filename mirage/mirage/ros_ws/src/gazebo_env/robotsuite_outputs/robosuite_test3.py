import cv2
import numpy as np
import json
import open3d as o3d
from scipy.spatial.transform import Rotation as R


def project_points_from_world_to_camera(points, world_to_camera_transform, camera_height, camera_width):
    """
    Helper function to project a batch of points in the world frame
    into camera pixels using the world to camera transformation.

    Args:
        points (np.array): 3D points in world frame to project onto camera pixel locations. Should
            be shape [..., 3].
        world_to_camera_transform (np.array): 4x4 Tensor to go from robot coordinates to pixel
            coordinates.
        camera_height (int): height of the camera image
        camera_width (int): width of the camera image

    Return:
        pixels (np.array): projected pixel indices of shape [..., 2]
    """
    assert points.shape[-1] == 3  # last dimension must be 3D
    assert len(world_to_camera_transform.shape) == 2
    assert world_to_camera_transform.shape[0] == 4 and world_to_camera_transform.shape[1] == 4

    # convert points to homogenous coordinates -> (px, py, pz, 1)
    ones_pad = np.ones(points.shape[:-1] + (1,))
    points = np.concatenate((points, ones_pad), axis=-1)  # shape [..., 4]

    # batch matrix multiplication of 4 x 4 matrix and 4 x 1 vectors to do robot frame to pixels transform
    mat_reshape = [1] * len(points.shape[:-1]) + [4, 4]
    cam_trans = world_to_camera_transform.reshape(mat_reshape)  # shape [..., 4, 4]
    pixels = np.matmul(cam_trans, points[..., None])[..., 0]  # shape [..., 4]

    # re-scaling from homogenous coordinates to recover pixel values
    # (x, y, z) -> (x / z, y / z)
    pixels = pixels / pixels[..., 2:3]
    pixels = pixels[..., :2].round().astype(int)  # shape [..., 2]
    # swap first and second coordinates to get pixel indices that correspond to (height, width)
    # and also clip pixels that are out of range of the camera image
    pixels = np.concatenate(
        (
            pixels[..., 1:2].clip(0, camera_height - 1),
            pixels[..., 0:1].clip(0, camera_width - 1),
        ),
        axis=-1,
    )
    points_to_pixels_robosuite = {tuple(arr_4): tuple(arr_2) for arr_4, arr_2 in zip(points,pixels)}
    pixels_to_points_robosuite = {}
    for key,value in points_to_pixels_robosuite.items():
        pixels_to_points_robosuite.setdefault(value,[]).append(key)
    return pixels,points_to_pixels_robosuite,pixels_to_points_robosuite

# panda_output = np.load('Panda_output.npy',allow_pickle=True)
panda_output = np.load('Panda_output.npy',allow_pickle=True)

# Convert dictionary to a string
panda_output_dict = panda_output[6]
joints = panda_output_dict['joint_angles']
print(joints)
ee_pos = panda_output_dict['robot_eef_pos']
print(ee_pos)
ee_quat = panda_output_dict['robot_eef_quat']
print(ee_quat)
rotation_ee = R.from_quat(ee_quat)
rotation_matrix_ee = rotation_ee.as_matrix()
print(rotation_matrix_ee)
translation_ee = np.array([1.6,0,1.45])
frontview_image = panda_output_dict['frontview']['rgb']
cv2.imwrite('frontview_image.png',frontview_image)
points = panda_output_dict['frontview']['points']
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
gazebo_output = np.load('panda_gazebo_pointcloud.npy')
pcd_gazebo = o3d.geometry.PointCloud()
pcd_gazebo.points = o3d.utility.Vector3dVector(gazebo_output)
color = [0.0,0.0,1.0]
pcd_gazebo.colors = o3d.utility.Vector3dVector(np.tile(color, (gazebo_output.shape[0], 1)))
mesh_coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame()
# Visualizing the point cloud

gazebo_output = gazebo_output.astype('float64')
rvec = np.array([0,0,0]).reshape(3,1)
rvec = rvec.astype('float64')
tvec = np.array([0,0,0]).reshape(3,1)
tvec = tvec.astype('float64')
camera_matrix = np.array([[309.01933598,   0.        , 128.        ],
       [  0.        , 309.01933598, 128.        ],
       [  0.        ,   0.        ,   1.        ]])
dist_coeffs = np.array([0,0,0,0])
dist_coeffs = dist_coeffs.astype('float64')

image_points,jacobian = cv2.projectPoints(gazebo_output,rvec,tvec,camera_matrix,dist_coeffs)
gazebo_mask = np.zeros((256,256), dtype=np.uint8)
int_image_points = np.round(image_points).astype(int)
int_image_points = int_image_points.reshape(int_image_points.shape[0],2)
gazebo_mask[int_image_points[:,1],int_image_points[:,0]] = 255
cv2.imwrite('gazebo_mask.png',gazebo_mask)
robosuite_seg = panda_output_dict['frontview']['seg']
robosuite_seg *= 255
cv2.imwrite('robosuite_mask.png',robosuite_seg)
cv2.imwrite('diff.png',abs(robosuite_seg.squeeze() - gazebo_mask))
# o3d.visualization.draw_geometries([pcd,pcd_gazebo,mesh_coordinate_frame])
camera_transform = np.hstack((camera_matrix,np.array([0,0,0]).reshape(3,1)))
camera_transform = np.vstack((camera_transform,np.array([0,0,0,1]).reshape(1,4)))
robosuite_img_points,points_to_pixels_robosuite,pixels_to_points_robosuite = project_points_from_world_to_camera(gazebo_output,camera_transform,256,256)
gazebo_camera_matrix = np.array([[528.433756558705,0,320.5],
                                 [0,528.433756558705,240.5],
                                 [0,0,1]])
gazebo_camera_transform = np.hstack((gazebo_camera_matrix,np.array([0,0,0]).reshape(3,1)))
gazebo_camera_transform = np.vstack((gazebo_camera_transform,np.array([0,0,0,1]).reshape(1,4)))
_,points_to_pixels_gazebo,pixels_to_points_gazebo = project_points_from_world_to_camera(gazebo_output,gazebo_camera_transform,480,640)
gazebo_image = cv2.imread('gazebo_image.png')
inpainted_image = cv2.imread('frontview_image.png')
for pixel in pixels_to_points_robosuite.keys():
    points = pixels_to_points_robosuite[pixel]
    gazebo_pixels = []
    for point in points: 
        gazebo_pixels.append(list(points_to_pixels_gazebo[point]))
    rgb_values = []
    for gazebo_pixel in gazebo_pixels:
        rgb_values.append(gazebo_image[gazebo_pixel[0],gazebo_pixel[1] - 5,:])
    
    rgb_values_np = np.array(rgb_values)
    mean_rgb_value = np.mean(rgb_values_np,axis=0).astype(int)
    inpainted_image[pixel[0],pixel[1],:] = mean_rgb_value
cv2.imwrite('inpaint.png',inpainted_image)
mask2 = np.zeros((256,256), dtype=np.uint8)
mask2[robosuite_img_points[:,0],robosuite_img_points[:,1]] = 255
cv2.imwrite('gazebo_robo_diff.png',abs(mask2 - gazebo_mask))