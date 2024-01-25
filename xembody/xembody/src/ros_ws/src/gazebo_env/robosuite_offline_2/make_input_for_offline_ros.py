import numpy as np
import os
import cv2
import transforms3d.euler as t_euler

def normalize_depth_image(depth_image):
    # Define the minimum and maximum depth values in your depth image
    min_depth = np.min(depth_image)
    max_depth = np.max(depth_image)

    # Normalize the depth image to the range [0, 1]
    normalized_depth_image = (depth_image - min_depth) / (max_depth - min_depth)

    # Optionally, you can scale the normalized image to a different range
    # For example, to scale it to [0, 255] for visualization:
    normalized_depth_image = (normalized_depth_image * 255).astype(np.uint8)
    return normalized_depth_image
if not os.path.exists('offline_ur5e/results'):
    os.makedirs('offline_ur5e/results')
# Load the data
data = np.load("one_trajectory_source_target.npy", allow_pickle=True)
for i in range(data.shape[0]):
    data0 = data[i]
    folder_path = 'offline_ur5e/offline_ur5e_'+str(i)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    panda_folder_path = 'offline_ur5e/offline_ur5e_'+str(i)+'/panda'
    if not os.path.exists(panda_folder_path):
        os.makedirs(panda_folder_path)

    extrinsic_matrix = data0['agentview']['extrinsic_matrix']
    intrinsic_matrix = data0['agentview']['intrinsic_matrix']



    print("Hardcode these values in write data robosuite node")
    print("Intrinsic Matrix: " + str(intrinsic_matrix))
    print("Extrinsic Matrix: " + str(extrinsic_matrix))
    print("Inverse Extrinsic: " + str(np.linalg.inv(extrinsic_matrix)))

    world_to_image = extrinsic_matrix
    image_to_cam = np.array(
        [
            [0,-1,0,0],
            [0,0,-1,0],
            [1,0,0,0],
            [0,0,0,1]
        ]
    )
    world_to_cam = world_to_image @ image_to_cam
    euler_angles = t_euler.mat2euler(world_to_cam[:3,:3],axes='sxyz')
    translation = world_to_cam[:3,3]
    print("Hardcode Extrinsic values in Gazebo sim URDF")
    print("World to cam: " + str(world_to_cam))
    print("Extrinsic Rotation: " + str(euler_angles))
    print("Extrinsic Translation: " + str(translation))

    joints = data0['joint_angles']
    gripper_command = data0['robot0_gripper_qpos'][5]
    grippers = data0['robot0_gripper_qpos']
    joints = np.append(joints,gripper_command)
    np.save(folder_path + '/joints.npy',joints)
    np.save(folder_path + '/gripper.npy',grippers)

    depth = data0['agentview']['real_depth_map']
    normalized_depth_image = normalize_depth_image(depth)
    cv2.imwrite(folder_path + '/normalized_depth.png',normalized_depth_image)
    np.save(folder_path + '/depth.npy',depth)


    rgb = data0['agentview']['rgb']
    rgb = cv2.cvtColor(rgb,cv2.COLOR_BGR2RGB)
    cv2.imwrite(folder_path + '/rgb.png',rgb)

    seg = data0['agentview']['seg']
    seg *= 255
    cv2.imwrite(folder_path + '/seg.png',seg)

    panda_rgb = (data0['ground_truth_source_robot']['rgb']*255).astype(np.uint8)
    panda_rgb = cv2.cvtColor(panda_rgb,cv2.COLOR_BGR2RGB)
    cv2.imwrite(panda_folder_path+'/rgb.png',panda_rgb)
    panda_joints = data0['ground_truth_source_robot']['joint_angles']
    panda_gripper_joints = data0['ground_truth_source_robot']['robot0_gripper_qpos']
    with open(panda_folder_path+'/joints.txt','w') as f:
        f.write(str(panda_joints))
        f.write(str(panda_gripper_joints))
    panda_eef_pos = data0['ground_truth_source_robot']['robot_eef_pos']
    panda_eef_quat = data0['ground_truth_source_robot']['robot_eef_quat']
    with open(panda_folder_path+'/panda_end_effector.txt','w') as f:
        f.write(str(panda_eef_pos))
        f.write(str(panda_eef_quat))

