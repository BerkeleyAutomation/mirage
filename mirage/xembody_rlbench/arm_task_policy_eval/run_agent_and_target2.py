import numpy as np
import torch
from absl import app, flags
from hydra.experimental import initialize, compose
from moviepy.editor import *
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from omegaconf import OmegaConf, ListConfig
from rlbench.action_modes.action_mode import MoveArmThenGripper
from rlbench.action_modes.arm_action_modes import EndEffectorPoseViaPlanning
from rlbench.action_modes.gripper_action_modes import Discrete
from rlbench.backend.utils import task_file_to_task_class
from rlbench.backend.exceptions import TaskEnvironmentError

import sys
import os
sys.path.append("/home/lawrence/xembody/ARM")
from arm import c2farm, qte, lpr
from arm.custom_rlbench_env import CustomRLBenchEnv, ActResult
from arm.lpr.trajectory_action_mode import TrajectoryActionMode
from launch import _create_obs_config
from tools.utils import RLBenchCinematic

FREEZE_DURATION = 2
FPS = 20

flags.DEFINE_string('logdir', '/home/lawrence/xembody/ARM/logs', 'weight dir.')
flags.DEFINE_integer('episodes', 1, 'The number of episodes to run.')
flags.DEFINE_string('method', 'C2FARM', 'The method to run.')
# flags.DEFINE_string('method', 'C2FARM+QTE', 'The method to run.')

# easy
flags.DEFINE_string('task', 'take_lid_off_saucepan', 'The task to run.') # work for both robots
# flags.DEFINE_string('task', 'open_door', 'The task to run.') # Sometimes out of reach for sawyer

# medium
# flags.DEFINE_string('task', 'lamp_on', 'The task to run.') # panda alright, sawyer really good
# flags.DEFINE_string('task', 'take_umbrella_out_of_umbrella_stand', 'The task to run.') # panda really good, sawyer alright
# flags.DEFINE_string('task', 'toilet_seat_up', 'The task to run.') # panda alright, sawyer alright
# flags.DEFINE_string('task', 'pick_up_cup', 'The task to run.') # panda alright, ur5 alright

# hard/no hope
# flags.DEFINE_string('task', 'insert_onto_square_peg', 'The task to run.')
# flags.DEFINE_string('task', 'put_toilet_roll_on_stand', 'The task to run.')
# flags.DEFINE_string('task', 'screw_nail', 'The task to run.')
# flags.DEFINE_string('task', 'pick_and_lift', 'The task to run.')
# flags.DEFINE_string('task', 'phone_on_base', 'The task to run.')
# flags.DEFINE_string('task', 'stack_wine', 'The task to run.')
# flags.DEFINE_string('task', 'put_books_on_bookshelf', 'The task to run.') # the task is bad. V-REP error
# flags.DEFINE_string('task', 'put_rubbish_in_bin', 'The task to run.') # the task is bad. The rubbish position is random and the task success fails to detect correctly for other robots


flags.DEFINE_string('target_robot', 'sawyer', 'Target robot.') # work for both robots

FLAGS = flags.FLAGS




def _save_clips(clips, name, robot_name):
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(f'eval_data/systematic_allow_target_exception/{name}_{robot_name}_{FLAGS.episodes}_trajs.mp4')
    # final_clip.write_videofile('%s_sawyer_replay_panda_seed2.mp4' % name)


def visualise(logdir, task, method):
    source_robot = 'panda'
    target_robot = FLAGS.target_robot

    config_path = os.path.join(logdir, task, method, '.hydra')
    weights_path = os.path.join(logdir, task, method, 'seed0', 'weights')

    if not os.path.exists(config_path):
        raise ValueError('No cofig in: ' + config_path)
    if not os.path.exists(weights_path):
        raise ValueError('No weights in: ' + weights_path)

    with initialize(config_path=os.path.relpath(config_path, os.path.dirname(os.path.abspath(__file__)))):
        cfg = compose(config_name="config")
    print(OmegaConf.to_yaml(cfg))

    cfg.rlbench.cameras = cfg.rlbench.cameras if isinstance(
        cfg.rlbench.cameras, ListConfig) else [cfg.rlbench.cameras]

    obs_config = _create_obs_config(
        cfg.rlbench.cameras, cfg.rlbench.camera_resolution)
    task_class = task_file_to_task_class(task)

    gripper_mode = Discrete()
    if cfg.method.name == 'PathARM':
        arm_action_mode = TrajectoryActionMode(cfg.method.trajectory_points)
    else:
        arm_action_mode = EndEffectorPoseViaPlanning()
    action_mode = MoveArmThenGripper(arm_action_mode, gripper_mode)


    # store result as a list of lists, where each inner list is [seed, active_source_success, active_target_success, passive_target_success]
    result = []

    
    clips1_total = []
    clips2_total = []
    clips3_total = []
    seed = 0
    while len(result) < FLAGS.episodes:
        print(f'Episode {len(result)}')
        current_result = [seed]
        # 1. Active Source robot: record its trajectory and success
        source_action_traj = []
        env = CustomRLBenchEnv(
            task_class=task_class, observation_config=obs_config,
            action_mode=action_mode, dataset_root=cfg.rlbench.demo_path,
            episode_length=cfg.rlbench.episode_length, headless=True,
            time_in_state=True, robot_name=source_robot, random_seed=seed)
        _ = env.observation_elements

        if cfg.method.name == 'C2FARM':
            agent = c2farm.launch_utils.create_agent(
                cfg, env, cfg.rlbench.scene_bounds,
                cfg.rlbench.camera_resolution)
        elif cfg.method.name == 'C2FARM+QTE':
            agent = qte.launch_utils.create_agent(
                cfg, env, cfg.rlbench.scene_bounds,
                cfg.rlbench.camera_resolution)
        elif cfg.method.name == 'LPR':
            agent = lpr.launch_utils.create_agent(
                cfg, env, cfg.rlbench.scene_bounds, cfg.rlbench.camera_resolution,
                cfg.method.trajectory_point_noise, cfg.method.trajectory_points,
                cfg.method.trajectory_mode, cfg.method.trajectory_samples)
        else:
            raise ValueError('Invalid method name.')

        agent.build(training=False, device=torch.device("cpu"))
        weight_folders = sorted(map(int, os.listdir(weights_path)))
        agent.load_weights(os.path.join(weights_path, str(weight_folders[-1])))

        env.launch()
        cinemtaic_cam = RLBenchCinematic()
        env.register_callback(cinemtaic_cam.callback)
        try:
            obs = env.reset()
            agent.reset()
        except TaskEnvironmentError as e:
            env.shutdown()
            seed += 1
            continue
        obs_history = {
            k: [np.array(v, dtype=_get_type(v))] * cfg.replay.timesteps for
            k, v in obs.items()}
        clips1 = []
        source_action_traj.append(np.concatenate((obs['gripper_pose'], [1]), axis=-1)) 
        last = False
        try:
            for step in range(cfg.rlbench.episode_length):
                prepped_data = {k: torch.FloatTensor([v]) for k, v in obs_history.items()}
                act_result = agent.act(step, prepped_data, deterministic=True)
                # act_result = ActResult(action=action_data[step])
                # print(act_result.action)
                source_action_traj.append(act_result.action)
                transition = env.step(act_result)

                trajectory_frames = cinemtaic_cam.frames
                if len(trajectory_frames) > 0:
                    cinemtaic_cam.empty()
                    clips1.append(ImageSequenceClip(trajectory_frames, fps=FPS))
                
                if last:
                    break
                if transition.terminal:
                    last = True
                    if transition.reward > 0:
                        print("Source robot success!")
                        current_result.append(1)
                    else:
                        print("Source robot failed!")
                        current_result.append(0)
                    break
                for k in obs_history.keys():
                    obs_history[k].append(transition.observation[k])
                    obs_history[k].pop(0)
                if step == cfg.rlbench.episode_length - 1:
                    print("Source robot failed!")
                    current_result.append(0)
                    break
        except Exception as e:
            print("Source robot exception happened!", e)
            # current_result.append(0)
            env.shutdown()
            seed += 1
            continue
        # print('Shutting down env...')
        env.shutdown()

        # 2. Active Target robot: record its success
        env = CustomRLBenchEnv(
            task_class=task_class, observation_config=obs_config,
            action_mode=action_mode, dataset_root=cfg.rlbench.demo_path,
            episode_length=cfg.rlbench.episode_length, headless=True,
            time_in_state=True, robot_name=target_robot, random_seed=seed)
        _ = env.observation_elements

        if cfg.method.name == 'C2FARM':
            agent = c2farm.launch_utils.create_agent(
                cfg, env, cfg.rlbench.scene_bounds,
                cfg.rlbench.camera_resolution)
        elif cfg.method.name == 'C2FARM+QTE':
            agent = qte.launch_utils.create_agent(
                cfg, env, cfg.rlbench.scene_bounds,
                cfg.rlbench.camera_resolution)
        elif cfg.method.name == 'LPR':
            agent = lpr.launch_utils.create_agent(
                cfg, env, cfg.rlbench.scene_bounds, cfg.rlbench.camera_resolution,
                cfg.method.trajectory_point_noise, cfg.method.trajectory_points,
                cfg.method.trajectory_mode, cfg.method.trajectory_samples)
        else:
            raise ValueError('Invalid method name.')

        agent.build(training=False, device=torch.device("cpu"))
        weight_folders = sorted(map(int, os.listdir(weights_path)))
        agent.load_weights(os.path.join(weights_path, str(weight_folders[-1])))

        env.launch()
        cinemtaic_cam = RLBenchCinematic()
        env.register_callback(cinemtaic_cam.callback)
        try:
            obs = env.reset()
            agent.reset()
        except Exception as e:
            env.shutdown()
            seed += 1
            continue
        obs_history = {
            k: [np.array(v, dtype=_get_type(v))] * cfg.replay.timesteps for
            k, v in obs.items()}
        clips2 = []
        last = False
        try:
            for step in range(cfg.rlbench.episode_length):
                prepped_data = {k: torch.FloatTensor([v]) for k, v in obs_history.items()}
                act_result = agent.act(step, prepped_data, deterministic=True)
                # act_result = ActResult(action=action_data[step])
                # print(act_result.action)
                transition = env.step(act_result)

                trajectory_frames = cinemtaic_cam.frames
                if len(trajectory_frames) > 0:
                    cinemtaic_cam.empty()
                    clips2.append(ImageSequenceClip(trajectory_frames, fps=FPS))
                if last:
                    break
                if transition.terminal:
                    last = True
                    if transition.reward > 0:
                        print("Target robot success!")
                        current_result.append(1)
                    else:
                        print("Target robot failed!")
                        current_result.append(0)
                    break
                for k in obs_history.keys():
                    obs_history[k].append(transition.observation[k])
                    obs_history[k].pop(0)
                if step == cfg.rlbench.episode_length - 1:
                    print("Target robot failed!")
                    current_result.append(0)
                    break
        except Exception as e:
            print("Target robot exception happened!", e)
            current_result.append(0)
            if len(clips2) == 0:
                # add a dummy frame
                clips2.append(clips1[-1])
            # env.shutdown()
            # seed += 1
            # continue
        env.shutdown()
        

        # 3. Passive Target robot: record its success
        env = CustomRLBenchEnv(
            task_class=task_class, observation_config=obs_config,
            action_mode=action_mode, dataset_root=cfg.rlbench.demo_path,
            episode_length=cfg.rlbench.episode_length, headless=True,
            time_in_state=True, robot_name=target_robot, random_seed=seed)
        _ = env.observation_elements

        if cfg.method.name == 'C2FARM':
            agent = c2farm.launch_utils.create_agent(
                cfg, env, cfg.rlbench.scene_bounds,
                cfg.rlbench.camera_resolution)
        elif cfg.method.name == 'C2FARM+QTE':
            agent = qte.launch_utils.create_agent(
                cfg, env, cfg.rlbench.scene_bounds,
                cfg.rlbench.camera_resolution)
        elif cfg.method.name == 'LPR':
            agent = lpr.launch_utils.create_agent(
                cfg, env, cfg.rlbench.scene_bounds, cfg.rlbench.camera_resolution,
                cfg.method.trajectory_point_noise, cfg.method.trajectory_points,
                cfg.method.trajectory_mode, cfg.method.trajectory_samples)
        else:
            raise ValueError('Invalid method name.')

        agent.build(training=False, device=torch.device("cpu"))
        weight_folders = sorted(map(int, os.listdir(weights_path)))
        agent.load_weights(os.path.join(weights_path, str(weight_folders[-1])))

        env.launch()
        cinemtaic_cam = RLBenchCinematic()
        env.register_callback(cinemtaic_cam.callback)
        try:
            obs = env.reset()
            agent.reset()
        except Exception as e:
            env.shutdown()
            seed += 1
            continue
        obs_history = {
            k: [np.array(v, dtype=_get_type(v))] * cfg.replay.timesteps for
            k, v in obs.items()}
        clips3 = []
        last = False
        try:
            for step in range(cfg.rlbench.episode_length):
                prepped_data = {k: torch.FloatTensor([v]) for k, v in obs_history.items()}
                # act_result = agent.act(step, prepped_data, deterministic=True)
                act_result = ActResult(action=source_action_traj[step])
                # print(act_result.action)
                transition = env.step(act_result)

                trajectory_frames = cinemtaic_cam.frames
                if len(trajectory_frames) > 0:
                    cinemtaic_cam.empty()
                    clips3.append(ImageSequenceClip(trajectory_frames, fps=FPS))
                if transition.reward > 0:
                    print("Target robot replay success!")
                    current_result.append(1)
                    break
                if last:
                    break
                if transition.terminal:
                    last = True
                    # break
                if step == min(len(source_action_traj), cfg.rlbench.episode_length) - 1:
                    print("Target robot replay failed!")
                    current_result.append(0)
                    break
                for k in obs_history.keys():
                    obs_history[k].append(transition.observation[k])
                    obs_history[k].pop(0)
        except Exception as e:
            print("Target robot replay exception happened!", e)
            # current_result.append(0)
            env.shutdown()
            seed += 1
            continue

        env.shutdown()

        result.append(current_result)
        seed += 1
        clips1_total.extend(clips1)
        clips2_total.extend(clips2)
        clips3_total.extend(clips3)

    _save_clips(clips1_total, f'{method}_{task}_{target_robot}', source_robot)
    _save_clips(clips2_total, f'{method}_{task}', target_robot)
    _save_clips(clips3_total, f'{method}_{task}_replay', target_robot)
    print(result)
    np.savetxt(f'eval_data/systematic_allow_target_exception/{method}_{task}_{source_robot}_{target_robot}_{FLAGS.episodes}_trajs.txt', np.array(result), delimiter=',')


def _get_type(x):
    if x.dtype == np.float64:
        return np.float32
    return x.dtype


def main(argv):
    del argv


    visualise(FLAGS.logdir, FLAGS.task, FLAGS.method)


if __name__ == '__main__':
    app.run(main)

    
