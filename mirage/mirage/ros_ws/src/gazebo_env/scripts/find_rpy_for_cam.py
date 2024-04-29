import numpy as np
from scipy.spatial.transform import Rotation

camera_link_to_real_camera_link = np.array([[0,0,1],
                                            [-1,0,0],
                                            [0,-1,0]])

world_to_real_camera_link = np.array([[-0.86235505,0.32847092,-0.38529289],
                                      [0.50327672,  -0.72315981,  0.35937403],
                                      [-0.05528389,  -0.81752946 , -0.57322707]])


real_camera_link_to_camera_link = np.linalg.inv(camera_link_to_real_camera_link)

world_to_camera_link = world_to_real_camera_link @ real_camera_link_to_camera_link

print(world_to_camera_link)

rpy_angles = Rotation.from_matrix(world_to_camera_link).as_euler('xyz', degrees=False)

print(rpy_angles)
