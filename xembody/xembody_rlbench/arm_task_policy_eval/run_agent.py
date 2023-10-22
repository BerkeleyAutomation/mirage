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

import sys
import os
sys.path.append("/home/lawrence/xembody/ARM")
from arm import c2farm, qte, lpr
from arm.custom_rlbench_env import CustomRLBenchEnv
from arm.lpr.trajectory_action_mode import TrajectoryActionMode
from launch import _create_obs_config
from tools.utils import RLBenchCinematic

FREEZE_DURATION = 2
FPS = 20

flags.DEFINE_string('logdir', '/home/lawrence/xembody/ARM/logs', 'weight dir.')
flags.DEFINE_string('method', 'C2FARM', 'The method to run.')
# flags.DEFINE_string('method', 'C2FARM+QTE', 'The method to run.')
# flags.DEFINE_string('task', 'take_lid_off_saucepan', 'The task to run.')
# flags.DEFINE_string('task', 'open_door', 'The task to run.')
# flags.DEFINE_string('task', 'put_books_on_bookshelf', 'The task to run.')
# flags.DEFINE_string('task', 'take_umbrella_out_of_umbrella_stand', 'The task to run.')
# flags.DEFINE_string('task', 'stack_wine', 'The task to run.')
# flags.DEFINE_string('task', 'pick_up_cup', 'The task to run.')
# flags.DEFINE_string('task', 'phone_on_base', 'The task to run.')
# flags.DEFINE_string('task', 'put_rubbish_in_bin', 'The task to run.')
# flags.DEFINE_string('task', 'pick_and_lift', 'The task to run.')
# flags.DEFINE_string('task', 'lamp_on', 'The task to run.')
# flags.DEFINE_string('task', 'screw_nail', 'The task to run.')
# flags.DEFINE_string('task', 'insert_onto_square_peg', 'The task to run.')
# flags.DEFINE_string('task', 'put_toilet_roll_on_stand', 'The task to run.')
flags.DEFINE_string('task', 'toilet_seat_up', 'The task to run.')
flags.DEFINE_integer('episodes', 1, 'The number of episodes to run.')

FLAGS = flags.FLAGS


# action_data = np.array([[ 0.48437503, -0.121875,    1.20937502,  0.70105738,  0.09229596,  0.43045933,
#   0.56098553,  0.        ],
# [ 0.55937499, -0.14687499,  1.22187495,  0.72485998,  0.11098448,  0.42602374,
#   0.5298719,   0.        ],
# [ 0.59687495, -0.16562499,  1.22187495,  0.72485998,  0.11098448,  0.42602374,
#   0.5298719,   0.        ],
# [ 0.62187493, -0.171875,    1.22187495,  0.72485998,  0.11098448,  0.42602374,
#   0.5298719,   0.        ],
# [ 0.62187493, -0.18437499,  1.22187495,  0.72485998,  0.11098448,  0.42602374,
#   0.5298719,   0.        ]])


# action_data = np.array([
#     [0.49062499, -0.128125, 1.22812498, 0.56098553, 0.43045933, 0.47771442, 0.5213338, 0.0],
#     [0.49062499, -0.128125, 1.22187495, 0.40557979, 0.57922797, 0.61237244, 0.35355339, 0.0],
#     [0.55937499, -0.159375, 1.20937502, 0.59636781, 0.3799282, 0.62721138, 0.32650558, 0.0],
#     [0.484375, -0.128125, 1.22187495, 0.61004217, 0.40692517, 0.61004217, 0.30018162, 0.0],
#     [0.578125, -0.16562499, 1.22187495, 0.61004217, 0.40692517, 0.61004217, 0.30018162, 0.0],
#     [0.52812493, -0.171875, 1.22187495, 0.61004217, 0.40692517, 0.61004217, 0.30018162, 0.0],
#     [0.62187493, -0.190625, 1.22187495, 0.61004217, 0.40692517, 0.61004217, 0.30018162, 0.0],
#     [0.62187493, -0.190625, 1.22187495, 0.61004217, 0.40692517, 0.61004217, 0.30018162, 0.0]
# ])

# action_data = np.array([[-9.06250104e-02, -3.71874988e-01,  1.00312507e+00, -8.87010833e-01,
#  -4.61748613e-01,  2.82739481e-17,  5.43137489e-17,  0.00000000e+00],
# [-9.06250104e-02, -3.71874988e-01,  1.19062507e+00, -8.87010833e-01,
#  -4.61748613e-01,  2.82739481e-17,  5.43137489e-17,  0.00000000e+00],
# [-9.06250104e-02, -3.71874988e-01,  1.33437502e+00, -8.87010833e-01,
#  -4.61748613e-01,  2.82739481e-17,  5.43137489e-17,  0.00000000e+00]])


# action_data = np.array([[ 7.18749836e-02,  2.09375009e-01,  8.59375000e-01, -9.76296007e-01,
#   2.16439614e-01, -1.32531040e-17,  5.97808890e-17,  0.00000000e+00],
# [ 7.18749836e-02,  2.09375009e-01,  1.08437502e+00, -9.76296007e-01,
#   2.16439614e-01, -1.32531040e-17,  5.97808890e-17,  0.00000000e+00],
# [ 7.81249851e-02,  2.65625000e-01,  1.00937498e+00, -9.76296007e-01,
#   2.16439614e-01, -1.32531040e-17,  5.97808890e-17,  0.00000000e+00]])


# # seed 1
# [ 0.15312499 -0.171875    0.77187502 -0.99809735 -0.04357787  0.04357787
#  -0.00190265  0.        ]
# [ 0.17812499 -0.171875    0.99687499 -0.99809735 -0.04357787  0.04357787
#  -0.00190265  0.        ]
# [ 0.19687499 -0.171875    1.20937502 -0.99809735 -0.04357787  0.04357787
#  -0.00190265  1.        ]
# [ 0.11562499 -0.22812499  0.77187502 -0.99809735 -0.04357787  0.04357787
#  -0.00190265  0.        ]
# [ 0.13437499 -0.22812499  1.015625   -0.99809735 -0.04357787  0.04357787
#  -0.00190265  0.        ]
# [ 0.15312499 -0.22812499  1.24687505 -0.99809735 -0.04357787  0.04357787
#  -0.00190265  0.        ]
# [ 1.40625000e-01  2.03125000e-01  1.01562500e+00 -9.99048222e-01
#  -4.36193874e-02  2.67091716e-18  6.11740603e-17  1.00000000e+00]
# [ 0.25312498  0.24062501  0.86562502  0.14383848 -0.91187636 -0.36951306
#   0.10607586  1.        ]

# # seed 2
action_data = np.array([
[ 0.19687499, -0.040625,    0.77187502, -0.99809735, -0.04357787,  0.04357787,
 -0.00190265,  0.        ],
[ 0.21562499, -0.040625,    0.99687499, -0.99809735, -0.04357787,  0.04357787,
 -0.00190265,  0.        ],
[ 0.159375  , -0.30937499,  1.015625,   -0.99809735, -0.04357787,  0.04357787,
 -0.00190265,  1.        ],
[ 0.09062498,  0.071875,    0.77187502, -0.99809735, -0.04357787,  0.04357787,
 -0.00190265,  0.        ]])

def _save_clips(clips, name):
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile('%s_panda_seed2.mp4' % name)
    # final_clip.write_videofile('%s_sawyer_replay_panda_seed2.mp4' % name)


def visualise(logdir, task, method):
    np.random.seed(2)
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

    env = CustomRLBenchEnv(
        task_class=task_class, observation_config=obs_config,
        action_mode=action_mode, dataset_root=cfg.rlbench.demo_path,
        episode_length=cfg.rlbench.episode_length, headless=True,
        time_in_state=True)
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
    for ep in range(FLAGS.episodes):
        obs = env.reset()
        agent.reset()
        obs_history = {
            k: [np.array(v, dtype=_get_type(v))] * cfg.replay.timesteps for
            k, v in obs.items()}
        clips = []
        last = False
        for step in range(cfg.rlbench.episode_length):
            prepped_data = {k: torch.FloatTensor([v]) for k, v in obs_history.items()}
            # breakpoint()
            act_result = agent.act(step, prepped_data, deterministic=True)
            # from arm.custom_rlbench_env import ActResult
            # act_result = ActResult(action=action_data[step])
            print(act_result.action)
            transition = env.step(act_result)
            # print("Gripper pose: ", transition.observation['gripper_pose']) 
            # print("Gripper open: ", transition.observation['gripper_open'])

            trajectory_frames = cinemtaic_cam.frames
            if len(trajectory_frames) > 0:
                cinemtaic_cam.empty()
                clips.append(ImageSequenceClip(trajectory_frames, fps=FPS))
            if transition.reward > 0:
                print("Success!")
            if last:
                break
            if transition.terminal:
                last = True
                # break
            # if step == len(action_data) - 1:
            #     print("Failed!")
            #     break
            for k in obs_history.keys():
                obs_history[k].append(transition.observation[k])
                obs_history[k].pop(0)
        _save_clips(clips, '%s_%s' % (method, task))

    print('Shutting down env...')
    env.shutdown()


def _get_type(x):
    if x.dtype == np.float64:
        return np.float32
    return x.dtype


def main(argv):
    del argv
    visualise(FLAGS.logdir, FLAGS.task, FLAGS.method)


if __name__ == '__main__':
    app.run(main)
