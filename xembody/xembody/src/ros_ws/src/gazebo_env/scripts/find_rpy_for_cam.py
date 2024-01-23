import numpy as np
from scipy.spatial.transform import Rotation

camera_link_to_real_camera_link = np.array([[0,0,1],
                                            [-1,0,0],
                                            [0,-1,0]])
world_to_real_camera_link = np.array([[-2.83437012e-08,  6.55035550e-01, -7.55598060e-01],
                                      [1.00000000e+00, -1.81704295e-07, -1.95032891e-07],
                                      [-2.65048890e-07, -7.55598060e-01, -6.55035550e-01]])

real_camera_link_to_camera_link = np.linalg.inv(camera_link_to_real_camera_link)

world_to_camera_link = world_to_real_camera_link @ real_camera_link_to_camera_link

print(world_to_camera_link)

rpy_angles = Rotation.from_matrix(world_to_camera_link).as_euler('xyz', degrees=False)

print(rpy_angles)
