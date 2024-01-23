import open3d as o3d
import numpy as np
import cv2

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

rgbd = np.load('/home/benchturtle/cross_embodiment_ws/src/gazebo_env/franka_1/rgbd.npy')
seg = cv2.imread('/home/benchturtle/cross_embodiment_ws/src/gazebo_env/franka_1/seg.jpg',0)
_, seg = cv2.threshold(seg, 128, 255, cv2.THRESH_BINARY)
intrinsic = np.array([[528.433756558705,0,320.5],[0,528.433756558705,240.5],[0,0,1]])
color_image = rgbd[:,:,0:3]
color_image = cv2.cvtColor(color_image,cv2.COLOR_BGR2RGB)
depth_image = rgbd[:,:,-1]
depth_image = depth_image[:,:,np.newaxis]
rgbd_image = np.concatenate((color_image,depth_image),axis=2)
inverted_mask = cv2.bitwise_not(seg)
masked_rgbd_image = cv2.bitwise_and(rgbd_image,rgbd_image,mask=inverted_mask)
cv2.imwrite('/home/benchturtle/cross_embodiment_ws/src/gazebo_env/scripts/rgb_image.png',masked_rgbd_image[:,:,0:3])
masked_rgb_image = masked_rgbd_image[:,:,0:3]
masked_depth_image = masked_rgbd_image[:,:,-1]
cv2.imwrite('/home/benchturtle/cross_embodiment_ws/src/gazebo_env/scripts/depth_image.png',normalize_depth_image(masked_depth_image))

gazebo_rgb = cv2.imread('/home/benchturtle/cross_embodiment_ws/src/gazebo_env/franka_1/gazebo_robot_only.jpg')
gazebo_depth = np.load('/home/benchturtle/cross_embodiment_ws/src/gazebo_env/franka_1/gazebo_robot_depth.npy')
joined_depth = np.concatenate((gazebo_depth[np.newaxis],masked_depth_image[np.newaxis]),axis=0)
joined_depth[joined_depth == 0] = 1000
joined_depth_argmin = np.argmin(joined_depth,axis=0)
attempt = masked_rgb_image * joined_depth_argmin[:,:,np.newaxis]
inverted_joined_depth_argmin = 1 - joined_depth_argmin
attempt2 = gazebo_rgb * inverted_joined_depth_argmin[:,:,np.newaxis]
inpainted_image = attempt + attempt2
cv2.imwrite('/home/benchturtle/cross_embodiment_ws/src/gazebo_env/franka_1/pog.png',inpainted_image)
# import pdb
# pdb.set_trace()
# rows, cols = masked_depth_image.shape
# y, x = np.meshgrid(range(rows), range(cols), indexing='ij')
# Z = masked_depth_image
# X = (x - intrinsic[0][2]) * Z / intrinsic[0][0]
# Y = (y - intrinsic[1][2]) * Z / intrinsic[1][1]
# points = np.column_stack((X.flatten(),Y.flatten(),Z.flatten()))
# pcd = o3d.geometry.PointCloud()
# pcd.points = o3d.utility.Vector3dVector(points)
# coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame()
# o3d.visualization.draw_geometries([pcd,coordinate_frame])

