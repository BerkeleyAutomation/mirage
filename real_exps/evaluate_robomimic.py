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
        "model":"real_exps/models/01-12-tiger/cams_20120598_left_ldkeys_proprio_backbone_ResNet18Conv_visdim_64_langcond_False/20240112150236/models/model_epoch_140.pth",
    },
    
}





def main():
    env = RobotEnv(blocking_gripper=False, cam_ids=[22008760, 18026681])
    index = 0

    model_name = "tiger"
    saving_directory = "real_exps/rollout_data/test"
    
    import json
    
    ckpt_path = model_config_mapping[model_name]['model']

    device = TorchUtils.get_torch_device(try_to_use_cuda=True)
    ckpt_dict = FileUtils.maybe_dict_from_checkpoint(ckpt_path=ckpt_path)
    config = json.loads(ckpt_dict["config"])

    ### infer image size ###
    imsize = 128

    ckpt_dict["config"] = json.dumps(config)
    policy, _ = FileUtils.policy_from_checkpoint(ckpt_dict=ckpt_dict, device=device, verbose=True)

    


    while True:
        print("Starting index {}".format(index))
        # Ask the user whether to continue or not
        if input("Continue? (y/n): ") == "n":
            break

        policy.start_episode()

        env.evaluate_robomimic_model_trajectory(policy, traj_index=index, saving_directory=saving_directory, gripper_history_window=(3, 0.5, 2.0))
        
        index += 1


if __name__=="__main__":
    main()