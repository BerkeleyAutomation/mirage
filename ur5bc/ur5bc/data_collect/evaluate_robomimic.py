import numpy as np
from ur5py.ur5 import UR5Robot
import subprocess
import cv2
import os
from autolab_core import CameraIntrinsics,RigidTransform
import time
import threading
import queue
import pickle
from PIL import Image
from ur5.robot_env_xembody import RobotEnv





import robomimic.utils.file_utils as FileUtils
import robomimic.utils.torch_utils as TorchUtils
import robomimic.utils.tensor_utils as TensorUtils
import robomimic.utils.train_utils as TrainUtils

model_config_mapping = {
    "tiger_in_bowl_left": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-12-tiger/ds_xembody-test_cams_20120598_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240112150236/models/model_epoch_140.pth",
        "config_path": "/home/zehan/tmp/autogen_configs/ril/diffusion_policy/r2d2/im/01-12-None/01-12-24-15-01-32/json/ds_xembody-test_cams_20120598_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False.json"
    },
    "tiger_in_bowl_stereo": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-12-tiger/ds_xembody-test_cams_20120598_stereo_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240112150432/models/model_epoch_140.pth",
        "config_path": "/home/zehan/tmp/autogen_configs/ril/diffusion_policy/r2d2/im/01-12-None/01-12-24-15-01-32/json/ds_xembody-test_cams_20120598_stereo_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False.json"
    },
    
    
    "drawer_left": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-18-drawer/ds_xembody-open-drawer_cams_20120598_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240118184224/models/model_epoch_400.pth",
    },
    "drawer_stereo": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-18-drawer/ds_xembody-open-drawer_cams_20120598_stereo_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240118103211/models/model_epoch_400.pth",
    },
    
    "toaster_left": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-20-toaster/ds_xembody-toaster_cams_20120598_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240120235632/models/model_epoch_400.pth",
    },
    "toaster_front": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-20-toaster/ds_xembody-toaster_cams_24400334_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240120235839/models/model_epoch_400.pth",
    },
    "toaster_left_front": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-20-toaster/ds_xembody-toaster_cams_20120598_left_24400334_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240121192329/models/model_epoch_400.pth",
    },
    
    
    "tiger_background_left": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-25-tiger-background/ds_xembody-tiger-background_cams_20120598_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240125013700/models/model_epoch_400.pth",
    },
    "tiger_background_front": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-25-tiger-background/ds_xembody-tiger-background_cams_24400334_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240125013745/models/model_epoch_400.pth",
    },
    "tiger_background_left_front": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-25-tiger-background/ds_xembody-tiger-background_cams_20120598_left_24400334_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240125013804/models/model_epoch_400.pth",
    },
    
    
    "cup_background_left": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-28-cup-background/ds_xembody-cup-background_cams_20120598_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240129014350/models/model_epoch_400.pth",
    },
    "cup_background_front": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-28-cup-background/ds_xembody-cup-background_cams_24400334_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240129014446/models/model_epoch_400.pth",
    },
    "cup_background_left_front": {
        "model":"/home/lawrence/xembody/ur5bc/models/01-28-cup-background/ds_xembody-cup-background_cams_20120598_left_24400334_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240129223940/models/model_epoch_400.pth",
    },
    
    
}





def main():
    # env = RobotEnv(blocking_gripper=False, cam_ids=[22008760])
    env = RobotEnv(blocking_gripper=False, cam_ids=[22008760, 32474776])
    # env = RobotEnv(blocking_gripper=True, cam_ids=[22008760, 32474776])
    index = 0

    model_name = "tiger_background_left"
    saving_directory = "/home/lawrence/xembody/ur5bc/rollout_data/test"
    
    import json
    
    ckpt_path = model_config_mapping[model_name]['model']
    # config_path = model_config_mapping[model_name]['config_path']

    device = TorchUtils.get_torch_device(try_to_use_cuda=True)
    ckpt_dict = FileUtils.maybe_dict_from_checkpoint(ckpt_path=ckpt_path)
    config = json.loads(ckpt_dict["config"])

    ### infer image size ###
    imsize = 128

    ckpt_dict["config"] = json.dumps(config)
    policy, _ = FileUtils.policy_from_checkpoint(ckpt_dict=ckpt_dict, device=device, verbose=True)

    # policy, _ = FileUtils.policy_from_checkpoint(ckpt_path=ckpt_path, device=device, verbose=True)

    # # Prepare Policy Wrapper #
    # data_processing_kwargs = dict(
    #     timestep_filtering_kwargs=dict(
    #         action_space=action_space,
    #         gripper_action_space=gripper_action_space,
    #         robot_state_keys=["cartesian_position", "gripper_position", "joint_positions"],
    #         # robot_state_keys = variant['robot_state_keys'],
    #         # camera_extrinsics=[],
    #     ),
    #     image_transform_kwargs=dict(
    #         remove_alpha=True,
    #         bgr_to_rgb=True,
    #         to_tensor=True,
    #         augment=False,
    #     ),
    # )
    # timestep_filtering_kwargs = data_processing_kwargs.get("timestep_filtering_kwargs", {})
    # image_transform_kwargs = data_processing_kwargs.get("image_transform_kwargs", {})

    # policy_data_processing_kwargs = {}
    # policy_timestep_filtering_kwargs = policy_data_processing_kwargs.get("timestep_filtering_kwargs", {})
    # policy_image_transform_kwargs = policy_data_processing_kwargs.get("image_transform_kwargs", {})

    # policy_timestep_filtering_kwargs.update(timestep_filtering_kwargs)
    # policy_image_transform_kwargs.update(image_transform_kwargs)

    # wrapped_policy = PolicyWrapperRobomimic(
    #     policy=policy,
    #     timestep_filtering_kwargs=policy_timestep_filtering_kwargs,
    #     image_transform_kwargs=policy_image_transform_kwargs,
    #     frame_stack=config['train']['frame_stack'],
    #     eval_mode=True,
    # )


    while True:
        print("Starting index {}".format(index))
        # Ask the user whether to continue or not
        if input("Continue? (y/n): ") == "n":
            break

        # env.reset(randomize=False, noise_type="cartesian")
        policy.start_episode()

        env.evaluate_robomimic_model_trajectory(policy, traj_index=index, saving_directory=saving_directory, gripper_history_window=(3, 0.5, 2.0))
        
        index += 1


if __name__=="__main__":
    main()