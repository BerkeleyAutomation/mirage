import h5py
import matplotlib.pyplot as plt
import cv2
import json
import numpy as np
import imageio.v2 as imageio

# path = "/home/lawrence/xembody/ur5bc/rollout_data/tiger/nonblocking_control_gain_100x3/traj0/images"
# images = []
# for i in range(78):
#     images.append(imageio.imread(os.path.join(path, f"third_person_img_color_{i}.png")))
# imageio.mimsave('test.gif', images)

path = "/home/lawrence/xembody/ur5bc/example_data/Wed_Jan_17_17:27:40_2024/trajectory_im128.h5"
# make a gif
with h5py.File(path, "r") as traj:
    images = traj['observation']['camera']['image']['varied_camera_1_left_image'][()]
    length = len(images)
    # create tmp folder
    import os
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    for i in range(len(images)):
        cv2.imwrite(f"tmp/{i}.png", cv2.cvtColor(images[i], cv2.COLOR_RGB2BGR))

images = []
for i in range(length):
    images.append(imageio.imread(f"tmp/{i}.png"))
imageio.mimsave('test.gif', images)
# delete all the images
import os
for i in range(length):
    os.remove(f"tmp/{i}.png")
# delete the tmp folder
os.rmdir("tmp")