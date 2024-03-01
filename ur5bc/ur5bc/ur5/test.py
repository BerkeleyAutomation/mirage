import pyrealsense2 as rs
import numpy as np
import matplotlib.pyplot as plt
# from utils import *
import argparse
import os
parser = argparse.ArgumentParser()
# parser.add_argument("--name", type=str, required=True)
parser.add_argument("--clip", type=float, required=False, default=1.0)
parser.add_argument("--normalize_mean", type=float, required=False, default=-0.5)
parser.add_argument("--normalize_std", type=float, required=False, default=0.4)
parser.add_argument("--crop_left", type=int, default=0)
parser.add_argument("--crop_right", type=int, default=0)
parser.add_argument("--crop_top", type=int, default=None)
parser.add_argument("--crop_bottom", type=int, default=None)
args = parser.parse_args()

os.makedirs("depth_images",exist_ok=True)
os.makedirs("depth_arr",exist_ok=True)
COMPRESSED_DEPTH_DIM = 128
# resize_transform = torchvision.transforms.Resize((58, 87), interpolation=torchvision.transforms.InterpolationMode.BICUBIC)

def get_depth():
    pipeline = rs.pipeline()
    config = rs.config()
  
    hole_filling = rs.hole_filling_filter()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    # profile = pipeline.start(config)
    profile = pipeline.start()
    depth_scale = profile.get_device().first_depth_sensor().get_depth_scale()
    
    ctr = 0
    while True:
        try:
            depth_frame = pipeline.wait_for_frames(timeout_ms = 100)

        except:
            continue
        frame = depth_frame.get_depth_frame()
        color = depth_frame.get_color_frame()

        frame = hole_filling.process(frame)
        np_frame = (np.asanyarray(frame.get_data(), np.float32) * depth_scale)
        # low_res = process_depth_image(np_frame, args)#.T 
        
        low_res = np_frame
        plt.imsave("/home/lawrence/robotlerf/ur5bc/data/depth_images/low_res_{}.png".format(ctr), low_res * 0.2 + 0.6)
        plt.imsave("/home/lawrence/robotlerf/ur5bc/data/depth_images/color_{}.png".format(ctr), np.asanyarray(color.get_data()))

        # np.save("depth_arr/low_res_{}.npy".format(ctr), low_res)
        # plt.imsave("depth_images/np_frame_{}.png".format(ctr), np_frame)
        # np.save("depth_arr/np_frame_{}.npy".format(ctr), np_frame)
        
        ctr +=1
    
  
if __name__ == '__main__':
    get_depth()

