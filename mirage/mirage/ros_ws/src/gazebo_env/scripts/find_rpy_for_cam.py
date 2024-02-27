import numpy as np
from scipy.spatial.transform import Rotation

camera_link_to_real_camera_link = np.array([[0,0,1],
                                            [-1,0,0],
                                            [0,-1,0]])
world_to_real_camera_link = np.array([[-0.9065319 ,  0.25194152, -0.33871137],
                                      [0.41907041,  0.44056495, -0.79390334],
                                      [-0.05079286, -0.86164261, -0.50496742]])

real_camera_link_to_camera_link = np.linalg.inv(camera_link_to_real_camera_link)

world_to_camera_link = world_to_real_camera_link @ real_camera_link_to_camera_link

print(world_to_camera_link)

rpy_angles = Rotation.from_matrix(world_to_camera_link).as_euler('xyz', degrees=False)

print(rpy_angles)
