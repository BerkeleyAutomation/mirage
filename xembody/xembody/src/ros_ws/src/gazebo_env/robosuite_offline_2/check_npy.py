import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = np.load("one_trajectory_source_target.npy", allow_pickle=True)
for i in range(len(data)):
    # show ["agentview"]["rgb"] and ["ground_truth_source_robot_rgb"] side by side
    plt.subplot(1, 2, 1)
    plt.imshow(data[i]["agentview"]["rgb"])
    plt.title("agentview")
    plt.subplot(1, 2, 2)
    plt.imshow(data[i]["ground_truth_source_robot"]["rgb"])
    plt.title("ground_truth_source_robot_rgb")
    plt.show()
    