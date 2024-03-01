import numpy as np
from scipy.spatial.transform import Rotation

camera_link_to_real_camera_link = np.array([[0,0,1],
                                            [-1,0,0],
                                            [0,-1,0]])

world_to_real_camera_link = np.array([[-0.02342304, -0.81669068, -0.57660012],
                                      [-0.99945141,  0.00562112,  0.03263869],
                                      [-0.02341457,  0.5770483 , -0.81637431]])


real_camera_link_to_camera_link = np.linalg.inv(camera_link_to_real_camera_link)

world_to_camera_link = world_to_real_camera_link @ real_camera_link_to_camera_link

print(world_to_camera_link)

rpy_angles = Rotation.from_matrix(world_to_camera_link).as_euler('xyz', degrees=False)

print(rpy_angles)
