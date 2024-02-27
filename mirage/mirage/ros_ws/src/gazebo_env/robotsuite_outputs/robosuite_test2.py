import cv2
import numpy as np
import json

panda_output = np.load('Panda_output.npy',allow_pickle=True)
# Convert dictionary to a string
panda_output_dict = panda_output[6]
joints = panda_output_dict['joint_angles']
print(joints)
ee_pos = panda_output_dict['robot_eef_pos']
print(ee_pos)
ee_quat = panda_output_dict['robot_eef_quat']
print(ee_quat)
frontview_image = panda_output_dict['frontview']['rgb']
cv2.imwrite('frontview_image.png',frontview_image)