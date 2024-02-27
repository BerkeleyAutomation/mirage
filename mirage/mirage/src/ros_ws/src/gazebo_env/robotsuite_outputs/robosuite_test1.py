import cv2
import numpy as np
import json

panda_output = np.load('Panda_output.npy',allow_pickle=True)
ur5e_output = np.load('UR5e_output1.npy',allow_pickle=True)
# Convert dictionary to a string
dict_str = str(panda_output[0])

# Write the dictionary string to a text file
with open('panda.txt', 'w') as file:
    file.write(dict_str)

# Convert dictionary to a string
dict_str = str(ur5e_output[0])

# Write the dictionary string to a text file
with open('ur5e.txt', 'w') as file:
    file.write(dict_str)