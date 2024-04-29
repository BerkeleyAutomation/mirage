import numpy as np
from scipy.spatial.transform import Rotation

camera_link_to_real_camera_link = np.array([[0,0,1,0],
                                            [-1,0,0,0],
                                            [0,-1,0,0],
                                            [0,0,0,1]])

real_camera_link_to_camera_link = np.linalg.inv(camera_link_to_real_camera_link)

ee_to_real_camera_link  = np.array([[0.72579549, -0.39985199,  0.55976718, -0.07525412],
                                      [0.68784404,  0.43314629, -0.58245589,  0.03308232],
                                      [-0.00956493,  0.80777638,  0.58941143,  0.01456681],
                                      [0,0,0,1]])

real_camera_link_to_ee = np.linalg.inv(ee_to_real_camera_link)


ee_to_camera_link = ee_to_real_camera_link @ real_camera_link_to_camera_link

print(ee_to_camera_link)
ee_to_camera_link_rotation = ee_to_camera_link[:3,:3]
rpy_angles = Rotation.from_matrix(ee_to_camera_link_rotation).as_euler('xyz', degrees=False)

print(rpy_angles)
