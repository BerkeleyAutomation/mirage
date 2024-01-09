import numpy as np
import cv2
import matplotlib.pyplot as plt

def difference(filename1, filename2):
    data1 = np.load(filename1, allow_pickle=True)
    data2 = np.load(filename2, allow_pickle=True)
    cv2.imshow('data1', data1.item()['agentview']['rgb'])
    cv2.imshow('data2', data2[6]['agentview']['rgb'])
    cv2.waitKey(0)

    plt.imshow(data1.item()['agentview']['seg'])
    plt.show()

    plt.imshow(data2[6]['agentview']['seg'])
    plt.show()

    plt.imshow(data1.item()['agentview']['real_depth_map'])
    plt.show()

    plt.imshow(data2[6]['agentview']['real_depth_map'])
    plt.show()

    import pdb; pdb.set_trace()

if __name__ == '__main__':
    difference('/home/lawrence/xembody/output.npy', '/home/lawrence/xembody/xembody/xembody_robosuite/rendering/output/UR5e_output.npy')