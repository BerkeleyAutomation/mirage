import numpy as np
import matplotlib.pyplot as plt
import cv2
# Load the data
data = np.load("one_trajectory_source_target.npy", allow_pickle=True)
folder_path = '/home/benchturtle/cross_embodiment_ws/src/gazebo_env/robosuite_offline_2/offline_ur5e/results/inpaint'

for i in range(len(data)):
    image_path = folder_path + str(i) +'.png'
    inpainted_result = cv2.imread(image_path)    # show ["agentview"]["rgb"] and ["ground_truth_source_robot_rgb"] side by side
    inpainted_result = cv2.cvtColor(inpainted_result,cv2.COLOR_BGR2RGB)
    plt.subplot(1, 3, 1)
    plt.imshow(inpainted_result)
    plt.title("inpainted")
    plt.subplot(1, 3, 2)
    plt.imshow(data[i]["ground_truth_source_robot"]["rgb"])
    plt.title("ground_truth_source_robot_rgb")
    plt.subplot(1,3,3)
    ground_truth_255 = data[i]["ground_truth_source_robot"]["rgb"] * 255
    plt.imshow(abs(inpainted_result-ground_truth_255.astype(np.uint8)))
    plt.show()
    
