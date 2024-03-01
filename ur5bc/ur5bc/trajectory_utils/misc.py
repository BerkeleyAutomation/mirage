import time
from collections import defaultdict
from copy import deepcopy

import cv2
import numpy as np
from PIL import Image


from ur5_bc.trajectory_utils.trajectory_reader import TrajectoryReader
from ur5_bc.trajectory_utils.trajectory_writer import TrajectoryWriter




def time_ms():
    return time.time_ns() // 1_000_000

def collect_trajectory(
    env,
    controller=None,
    policy=None,
    horizon=None,
    save_filepath=None,
    metadata=None,
    wait_for_controller=False,
    obs_pointer=None,
    save_images=False,
    recording_folderpath=False,
    randomize_reset=False,
    reset_robot=True,
):
    """
    Collects a robot trajectory.
    - If policy is None, actions will come from the controller
    - If a horizon is given, we will step the environment accordingly
    - Otherwise, we will end the trajectory when the controller tells us to
    - If you need a pointer to the current observation, pass a dictionary in for obs_pointer
    """

    # Check Parameters #
    assert (controller is not None) or (policy is not None)
    assert (controller is not None) or (horizon is not None)
    if wait_for_controller:
        assert controller is not None
    if obs_pointer is not None:
        assert isinstance(obs_pointer, dict)
    if save_images:
        assert save_filepath is not None

    # Reset States #
    if controller is not None:
        controller.reset_state()
    env.camera_reader.set_trajectory_mode()

    # Prepare Data Writers If Necesary #
    if save_filepath:
        traj_writer = TrajectoryWriter(save_filepath, metadata=metadata, save_images=save_images)
    if recording_folderpath:
        env.camera_reader.start_recording(recording_folderpath)

    # Prepare For Trajectory #
    num_steps = 0
    if reset_robot:
        env.reset(randomize=randomize_reset)

    # Begin! #
    while True:
        # Collect Miscellaneous Info #
        controller_info = {} if (controller is None) else controller.get_info()
        skip_action = wait_for_controller and (not controller_info["movement_enabled"])
        control_timestamps = {"step_start": time_ms()}

        # Get Observation #
        obs = env.get_observation()
        if obs_pointer is not None:
            obs_pointer.update(obs)
        obs["controller_info"] = controller_info
        obs["timestamp"]["skip_action"] = skip_action

        # Get Action #
        control_timestamps["policy_start"] = time_ms()
        if policy is None:
            action, controller_action_info = controller.forward(obs, include_info=True)
        else:
            action = policy.forward(obs)
            controller_action_info = {}

        # Regularize Control Frequency #
        control_timestamps["sleep_start"] = time_ms()
        comp_time = time_ms() - control_timestamps["step_start"]
        sleep_left = (1 / env.control_hz) - (comp_time / 1000)
        if sleep_left > 0:
            time.sleep(sleep_left)

        # Moniter Control Frequency #
        # moniter_control_frequency = True
        # if moniter_control_frequency:
        # 	print('Sleep Left: ', sleep_left)
        # 	print('Feasible Hz: ', (1000 / comp_time))

        # Step Environment #
        control_timestamps["control_start"] = time_ms()
        if skip_action:
            action_info = env.create_action_dict(np.zeros_like(action))
        else:
            action_info = env.step(action)
        action_info.update(controller_action_info)

        # Save Data #
        control_timestamps["step_end"] = time_ms()
        obs["timestamp"]["control"] = control_timestamps
        timestep = {"observation": obs, "action": action_info}
        if save_filepath:
            traj_writer.write_timestep(timestep)

        # Check Termination #
        num_steps += 1
        if horizon is not None:
            end_traj = horizon == num_steps
        else:
            end_traj = controller_info["success"] or controller_info["failure"]

        # Close Files And Return #
        if end_traj:
            if recording_folderpath:
                env.camera_reader.stop_recording()
            if save_filepath:
                traj_writer.close(metadata=controller_info)
            return controller_info




def replay_trajectory(
    env, filepath=None, assert_replayable_keys=["cartesian_position", "gripper_position", "joint_positions"]
):
    print("WARNING: STATE 'CLOSENESS' FOR REPLAYABILITY HAS NOT BEEN CALIBRATED")
    gripper_key = "gripper_velocity" if "velocity" in env.action_space else "gripper_position"

    # Prepare Trajectory Reader #
    traj_reader = TrajectoryReader(filepath, read_images=False)
    horizon = traj_reader.length()

    for i in range(horizon):
        # Get HDF5 Data #
        timestep = traj_reader.read_timestep()

        # Move To Initial Position #
        if i == 0:
            init_joint_position = timestep["observation"]["robot_state"]["joint_positions"]
            init_gripper_position = timestep["observation"]["robot_state"]["gripper_position"]
            action = np.concatenate([init_joint_position, [init_gripper_position]])
            env.update_robot(action, action_space="joint_position", blocking=True)

        # TODO: Assert Replayability #
        # robot_state = env.get_state()[0]
        # for key in assert_replayable_keys:
        # 	desired = timestep['observation']['robot_state'][key]
        # 	current = robot_state[key]
        # 	assert np.allclose(desired, current)

        # Regularize Control Frequency #
        time.sleep(1 / env.control_hz)

        # Get Action In Desired Action Space #
        arm_action = timestep["action"][env.action_space]
        gripper_action = timestep["action"][gripper_key]
        action = np.concatenate([arm_action, [gripper_action]])
        controller_info = timestep["observation"]["controller_info"]
        movement_enabled = controller_info.get("movement_enabled", True)

        # Follow Trajectory #
        if movement_enabled:
            env.step(action)


def load_trajectory(
    filepath=None,
    read_cameras=True,
    recording_folderpath=None,
    camera_kwargs={},
    remove_skipped_steps=False,
    num_samples_per_traj=None,
    num_samples_per_traj_coeff=1.5,
):
    read_hdf5_images = read_cameras and (recording_folderpath is None)
    read_recording_folderpath = read_cameras and (recording_folderpath is not None)

    traj_reader = TrajectoryReader(filepath, read_images=read_hdf5_images)
    if read_recording_folderpath:
        camera_reader = RecordedMultiCameraWrapper(recording_folderpath, camera_kwargs)

    horizon = traj_reader.length()
    timestep_list = []

    # Choose Timesteps To Save #
    if num_samples_per_traj:
        num_to_save = num_samples_per_traj
        if remove_skipped_steps:
            num_to_save = int(num_to_save * num_samples_per_traj_coeff)
        max_size = min(num_to_save, horizon)
        indices_to_save = np.sort(np.random.choice(horizon, size=max_size, replace=False))
    else:
        indices_to_save = np.arange(horizon)

    # Iterate Over Trajectory #
    for i in indices_to_save:
        # Get HDF5 Data #
        timestep = traj_reader.read_timestep(index=i)

        # If Applicable, Get Recorded Data #
        if read_recording_folderpath:
            timestamp_dict = timestep["observation"]["timestamp"]["cameras"]
            camera_type_dict = {
                k: camera_type_to_string_dict[v] for k, v in timestep["observation"]["camera_type"].items()
            }
            camera_obs = camera_reader.read_cameras(
                index=i, camera_type_dict=camera_type_dict, timestamp_dict=timestamp_dict
            )
            camera_failed = camera_obs is None

            # Add Data To Timestep If Successful #
            if camera_failed:
                break
            else:
                timestep["observation"].update(camera_obs)

        # Filter Steps #
        step_skipped = not timestep["observation"]["controller_info"].get("movement_enabled", True)
        delete_skipped_step = step_skipped and remove_skipped_steps

        # Save Filtered Timesteps #
        if delete_skipped_step:
            del timestep
        else:
            timestep_list.append(timestep)

    # Remove Extra Transitions #
    timestep_list = np.array(timestep_list)
    if (num_samples_per_traj is not None) and (len(timestep_list) > num_samples_per_traj):
        ind_to_keep = np.random.choice(len(timestep_list), size=num_samples_per_traj, replace=False)
        timestep_list = timestep_list[ind_to_keep]

    # Close Readers #
    traj_reader.close()
    if read_recording_folderpath:
        camera_reader.disable_cameras()

    # Return Data #
    return timestep_list


def visualize_timestep(timestep, max_width=1000, max_height=500, aspect_ratio=1.5, pause_time=15):
    # Process Image Data #
    obs = timestep["observation"]
    if "image" in obs:
        img_obs = obs["image"]
    elif "image" in obs["camera"]:
        img_obs = obs["camera"]["image"]
    else:
        raise ValueError

    camera_ids = sorted(img_obs.keys())
    sorted_image_list = []
    for cam_id in camera_ids:
        data = img_obs[cam_id]
        if type(data) == list:
            sorted_image_list.extend(data)
        else:
            sorted_image_list.append(data)

    # Get Ideal Number Of Rows #
    num_images = len(sorted_image_list)
    max_num_rows = int(num_images**0.5)
    for num_rows in range(max_num_rows, 0, -1):
        num_cols = num_images // num_rows
        if num_images % num_rows == 0:
            break

    # Get Per Image Shape #
    max_img_width, max_img_height = max_width // num_cols, max_height // num_rows
    if max_img_width > aspect_ratio * max_img_height:
        img_width, img_height = max_img_width, int(max_img_width / aspect_ratio)
    else:
        img_width, img_height = int(max_img_height * aspect_ratio), max_img_height

    # Fill Out Image Grid #
    img_grid = [[] for i in range(num_rows)]

    for i in range(len(sorted_image_list)):
        img = Image.fromarray(sorted_image_list[i])
        resized_img = img.resize((img_width, img_height), Image.Resampling.LANCZOS)
        img_grid[i % num_rows].append(np.array(resized_img))

    # Combine Images #
    for i in range(num_rows):
        img_grid[i] = np.hstack(img_grid[i])
    img_grid = np.vstack(img_grid)

    # Visualize Frame #
    cv2.imshow("Image Feed", img_grid)
    cv2.waitKey(pause_time)


def visualize_trajectory(
    filepath,
    recording_folderpath=None,
    remove_skipped_steps=False,
    camera_kwargs={},
    max_width=1000,
    max_height=500,
    aspect_ratio=1.5,
):
    traj_reader = TrajectoryReader(filepath, read_images=True)
    if recording_folderpath:
        if camera_kwargs is {}:
            camera_kwargs = defaultdict(lambda: {"image": True})
        camera_reader = RecordedMultiCameraWrapper(recording_folderpath, camera_kwargs)

    horizon = traj_reader.length()
    camera_failed = False

    for i in range(horizon):
        # Get HDF5 Data #
        timestep = traj_reader.read_timestep()

        # If Applicable, Get Recorded Data #
        if recording_folderpath:
            timestamp_dict = timestep["observation"]["timestamp"]["cameras"]
            camera_type_dict = {
                k: camera_type_to_string_dict[v] for k, v in timestep["observation"]["camera_type"].items()
            }
            camera_obs = camera_reader.read_cameras(
                index=i, camera_type_dict=camera_type_dict, timestamp_dict=timestamp_dict
            )
            camera_failed = camera_obs is None

            # Add Data To Timestep #
            if not camera_failed:
                timestep["observation"].update(camera_obs)

        # Filter Steps #
        step_skipped = not timestep["observation"]["controller_info"].get("movement_enabled", True)
        delete_skipped_step = step_skipped and remove_skipped_steps
        delete_step = delete_skipped_step or camera_failed
        if delete_step:
            continue

        # Get Image Info #
        assert "image" in timestep["observation"]
        img_obs = timestep["observation"]["image"]
        camera_ids = list(img_obs.keys())
        len(camera_ids)
        camera_ids.sort()

        # Visualize Timestep #
        visualize_timestep(
            timestep, max_width=max_width, max_height=max_height, aspect_ratio=aspect_ratio, pause_time=15
        )

    # Close Readers #
    traj_reader.close()
    if recording_folderpath:
        camera_reader.disable_cameras()