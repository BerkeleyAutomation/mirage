import h5py
import matplotlib.pyplot as plt
import cv2
path = "/home/lawrence/xembody/robomimic/datasets/square/ph/image_v141_256.hdf5"
# path = "/home/lawrence/xembody/xembody/xembody_robosuite/target_robot_demonstration_data/lift_ur5e_5.hdf5"
path2 = "/home/lawrence/xembody/xembody/xembody_robosuite/target_robot_demonstration_data/lift_ur5e_delta_action.hdf5"
"""
    data
        demo_0
            'actions', (T, 7)
            'dones', (T,)
            'next_obs', 
            'obs', 
                'agentview_image', (T, 84, 84, 3)
                'object', (T, 10)
                'robot0_eef_pos', (T, 3)
                'robot0_eef_quat', (T, 4)
                'robot0_eef_vel_ang', 
                'robot0_eef_vel_lin', 
                'robot0_eye_in_hand_image', 
                'robot0_gripper_qpos', (T, 2)
                'robot0_gripper_qvel', (T, 2)
                'robot0_joint_pos', (T, 7)
                'robot0_joint_pos_cos', 
                'robot0_joint_pos_sin', 
                'robot0_joint_vel'
            'rewards', (T,)
            'states', (T, 32)
    mask
        '20_percent', (40,)
        '20_percent_train', (36,)
        '20_percent_valid',  (4,)
        '50_percent', 
        '50_percent_train', 
        '50_percent_valid', 
        'train', (180,)
        'valid'
        
        
    data
        demo_0
            'actions' (T, 7)
            'dones' (T,)
            'next_obs'
            'obs'
                'agentview_image' (T, 128, 128, 4)
                'object' (T, 10)
                'robot0_eef_pos' (T, 3)
                'robot0_eef_quat' (T, 4)
                'robot0_gripper_qpos' (T, 2)
        demo_1
            // same as demo_0
        demo_2
        ...
    """
with h5py.File(path, "r") as file:
    breakpoint()
    item = file['data']
    traj = item['demo_1']
    for i in range(7):
        print(traj['actions'][()][:, i].min(), traj['actions'][()][:, i].max())
    print(traj['obs']['agentview_image'][()][0].min(), traj['obs']['agentview_image'][()][0].max())
    plt.imshow(traj['obs']['agentview_image'][()][10])
    plt.show()
    # plt.imshow(traj['obs']['agentview_segmentation_robot_only'][()][0])
    # plt.show()
    

# def list_attributes(file_path):
#     try:
#         with h5py.File(file_path, 'r') as hdf_file:
#             # Iterate through each item in the HDF5 file
#             def print_attrs(name, obj):
#                 print(f"Attributes of {name}:")
#                 for key, val in obj.attrs.items():
#                     print(f"{key}: {val}")
                    
#             hdf_file.visititems(print_attrs)
#     except Exception as e:
#         print(f"Error reading HDF5 file: {e}")

# list_attributes(path)


import json
# import h5py

with h5py.File(path2, "r") as file:
    item = file['data']
    env_args_str = item.attrs['env_args']
    env_args_dict = json.loads(env_args_str)
    controller_configs = env_args_dict['env_kwargs']['controller_configs']
    print(controller_configs)
    
# with h5py.File(path2, "r+") as file:
#     item = file['data']
    
#     # Load the attribute and convert it to a dictionary
#     env_args_str = item.attrs['env_args']
#     env_args_dict = json.loads(env_args_str)
    
#     # Modify the value
#     env_args_dict['env_kwargs']['controller_configs']['control_delta'] = True
    
#     # Convert the dictionary back to a string
#     updated_env_args_str = json.dumps(env_args_dict)
    
#     # Update the attribute value
#     item.attrs['env_args'] = updated_env_args_str

#     # Save the changes
#     file.flush()