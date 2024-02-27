import cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle
import imageio
# Load the data
# data = np.load("/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/inpaint_ur5_offline_data.npy", allow_pickle=True)[0]
data = np.load("/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/inpaint_data_for_analysis.npy", allow_pickle=True)
# data = np.load("/home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/one_trajectory_source_target_with_inpainted.npy", allow_pickle=True)
# data = data.tolist()
# breakpoint()
# Create a list to store the images
images_ur5 = []
images_franka = []
images_franka_inpaint = []
# Loop through the dictionary items and append images to the list
# for i in range(len(data)):
#     # Ensure the image data is in the correct format (e.g., uint8)
#     image_data = np.uint8(data[i]['agentview']['rgb'])
#     images_ur5.append(image_data)
#     image_data2 = np.uint8(data[i]['ground_truth_source_robot']['inpainting']['rgb']*255)
#     images_franka_inpaint.append(image_data2)
#     image_data2 = np.uint8(data[i]['ground_truth_source_robot']['source_robot']['rgb']*255)
#     images_franka.append(image_data2)
# # Save the images as a GIF using imageio
# imageio.mimsave('images_ur5.gif', images_ur5)
# imageio.mimsave('images_franka.gif', images_franka)
# imageio.mimsave('images_franka_inpaint.gif', images_franka_inpaint)

breakpoint()
# data = data.tolist()[0] # first trajectory


# from controlnet import ControlNet
# controlnet = ControlNet()
    
# for traj_idx in range(len(data)):
#     for i in range(len(data[traj_idx])):
#         # show ["agentview"]["rgb"] and ["ground_truth_source_robot_rgb"] side by side
#         plt.subplot(1, 4, 1)
#         plt.imshow(data[traj_idx][i]["target_robot"]["agentview"]["rgb"])
#         plt.title("agentview")
#         plt.subplot(1, 4, 2)
#         plt.imshow(data[traj_idx][i]['source_robot']['ground_truth']["rgb"])
#         plt.title("ground_truth_source_robot")
#         # inpainted_image, inpainted_image_84 = controlnet.inpaint(data[i]["target_robot"]["agentview"]["rgb"])
#         inpainted_image = data[traj_idx][i]["source_robot"]["inpainting"]["rgb"]
#         plt.subplot(1, 4, 3)
#         plt.imshow(inpainted_image)
#         plt.title("inpainted_image")
#         # image difference
#         plt.subplot(1, 4, 4)
#         plt.imshow(np.abs(data[traj_idx][i]['source_robot']['ground_truth']["rgb"] - inpainted_image))
#         plt.title("difference")
#         plt.show()

# breakpoint()
# save the above four images instead of showing them
# for traj_idx in range(len(data)):
#     for i in range(len(data[traj_idx])):
#         cv2.imwrite(f"/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/data/diffusion_lift_online_masked_256_delta/target_robot_{traj_idx}_{i}.png", cv2.cvtColor(data[traj_idx][i]["target_robot"]["agentview"]["rgb"], cv2.COLOR_RGB2BGR) * 255)
#         cv2.imwrite(f"/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/data/diffusion_lift_online_masked_256_delta/ground_truth_source_robot_{traj_idx}_{i}.png", cv2.cvtColor(data[traj_idx][i]['source_robot']['ground_truth']["rgb"], cv2.COLOR_RGB2BGR) * 255)
#         inpainted_image_256 = data[traj_idx][i]['source_robot']['inpainting']["rgb"]
#         cv2.imwrite(f"/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/data/diffusion_lift_online_masked_256_delta/inpainted_image_{traj_idx}_{i}.png", cv2.cvtColor(inpainted_image_256, cv2.COLOR_RGB2BGR) * 255)
#         # inpainted_image_256, inpainted_image = controlnet.inpaint(data[i]["target_robot"]["agentview"]["rgb"])
#         # cv2.imwrite(f"/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/data/diffusion_online/inpainted_image_{i}.png", cv2.cvtColor(inpainted_image_256, cv2.COLOR_RGB2BGR) * 255)
#         cv2.imwrite(f"/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/data/diffusion_lift_online_masked_256_delta/difference_{traj_idx}_{i}.png", np.abs(data[traj_idx][i]['source_robot']['ground_truth']["rgb"] - inpainted_image_256) * 255)

breakpoint()
# data = np.load("/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/inpaint_data_for_analysis.npy", allow_pickle=True)#.tolist()
for traj_idx in range(len(data)):
    print("Trajectory", traj_idx)
    predicted_states = []
    actual_states = []
    predicted_actions = []
    actual_actions = []
    actions_8d_predicted = []
    actions_8d_actual = []
    
    # data = data.tolist()[0] # first trajectory

    for i in range(len(data[traj_idx])):
        predicted_actions.append(data[traj_idx][i]['source_robot']['inpainting']['predicted_action']) # 7D
        predicted_states.append(data[traj_idx][i]['source_robot']['inpainting']['predicted_state'][:-2]) # 9D (3+4+2)
        
        actual_actions.append(data[traj_idx][i]['source_robot']['ground_truth']['action'])
        actual_states.append(data[traj_idx][i]['source_robot']['ground_truth']['target_state']) # 7D
        
        actions_8d_predicted.append(data[traj_idx][i]['inpaint_action']) # 8D
        actions_8d_actual.append(data[traj_idx][i]['ground_truth_action']) # 8D
    
    predicted_actions = np.vstack(predicted_actions)
    predicted_states = np.vstack(predicted_states)
    actual_actions = np.vstack(actual_actions)
    actual_states = np.vstack(actual_states)
    actions_8d_predicted = np.vstack(actions_8d_predicted)
    actions_8d_actual = np.vstack(actions_8d_actual)
    # breakpoint()
    # plot 2x7 subplots, top for actions, bottom for states
    for i in range(8):
        if i < 7:
            plt.subplot(3, 8, i + 1)
            plt.plot(predicted_actions[:, i], label=f"predicted action {i}")
            plt.plot(actual_actions[:, i], label=f"actual action {i}")
            plt.legend(fontsize=6)
            plt.subplot(3, 8, i + 9)
            plt.plot(predicted_states[:, i], label=f"predicted state {i}")
            plt.plot(actual_states[:, i], label=f"actual state {i}")
            plt.legend(fontsize=6)
        # plt.subplot(3, 8, i + 17)
        # plt.plot(actions_8d_predicted[:, i], label=f"predicted action {i}")
        # plt.plot(actions_8d_actual[:, i], label=f"actual action {i}")
        # plt.legend()
    plt.show()