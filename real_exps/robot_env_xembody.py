from copy import deepcopy
import os
import subprocess
from PIL import Image
import gym
import numpy as np
import cv2
import pickle
import h5py
import time
import threading
import queue
import torchvision.transforms as transforms
from autolab_core import RigidTransform
from autolab_core.transformations import quaternion_from_euler, quaternion_matrix, euler_matrix, quaternion_from_matrix, translation_from_matrix
from ur5py.ur5 import UR5Robot
from misc.time import time_ms
from matplotlib import pyplot as plt
from utils.async_writer import AsyncWrite, AsyncWriteStandardizedFormat
from ur5.spacemouse import SpaceMouseRobotController
from misc.policy_wrapper import FrameStackWrapper
import pyzed.sl as sl
from copy import deepcopy
from utils.transformations import convert_euler_to_rig, convert_rig_to_euler
from mirage.mirage.infra.ros_inpaint_publisher_real import ROSInpaintPublisherReal, ROSInpaintRealData
from scipy.spatial.transform import Rotation as R
import json
import socket
import struct
from functools import partial

class ZedSensor:
    """
    A Zed sensor that supports multithreading 
    """
    def __init__(self, cam_id=22008760, freq=1/60, max_buffer_len=10, lefteye=True) -> None:
        """
        cam_id: serial number, one of {20120598, 22008760, 18026681, 24400334}
        cam_res: (width, height)
        set_fps: set the fps of the camera
        max_buffer_len: the maximum number of frames to store in the buffer
        """
        # Create a Camera object
        self.cam_id = cam_id
        self.cam = sl.Camera()
        self.lefteye = lefteye
        
        # Create a InitParameters object and set configuration parameters
        init_params = sl.InitParameters()
        init_params.depth_mode = sl.DEPTH_MODE.NEURAL  # https://www.stereolabs.com/docs/depth-sensing/depth-settings {NEURAL, ULTRA, QUALITY, PERFORMANCE}
        init_params.coordinate_units = sl.UNIT.METER  # Use meter units (for depth measurements)
        init_params.depth_minimum_distance = 0.15 # Set the minimum depth perception distance to 15cm
        init_params.camera_resolution = sl.RESOLUTION.HD720
        init_params.camera_image_flip = sl.FLIP_MODE.OFF
        init_params.set_from_serial_number(self.cam_id) 
        
        status = self.cam.open(init_params)
        if status != sl.ERROR_CODE.SUCCESS:
            raise RuntimeError(f"Camera Failed To Open: {status}")
        
        self.runtime_parameters = sl.RuntimeParameters()
        self.runtime_parameters.enable_fill_mode = True
        # runtime_parameters.sensing_mode = sl.SENSING_MODE.SENSING_MODE_FILL
        
        self.image = sl.Mat()
        self.point_cloud = sl.Mat()
        self.depth = sl.Mat()


        self.active = False
        self.freq = freq
        self.buffer = []
        self.timestamp = []
        self.index_last = [0]
        self.max_buffer_len = max_buffer_len
        self.lock = threading.Lock()

    def start_read(self):
        self.flush()
        self.active = True
        while self.active:
            if self.freq is not None:
                time.sleep(self.freq)
            data = self.read()
            self.buffer.append(data)
            self.timestamp.append(time.time())
            if self.lock.acquire(blocking=False):
                if len(self.buffer) > self.max_buffer_len:
                    del self.buffer[:-self.max_buffer_len], self.timestamp[:-self.max_buffer_len]
                self.index_last[0] = len(self.buffer) - 1
                self.lock.release()

    def end_read(self):
        self.active = False 
        self.buffer = []
        self.timestamp = []

    def flush(self, num_ims=5):
        for i in range(num_ims):
            _ = self.read()

    def read(self):
        if self.cam.grab(self.runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            if self.lefteye:
                self.cam.retrieve_image(self.image, sl.VIEW.LEFT)
            else:
                self.cam.retrieve_image(self.image, sl.VIEW.RIGHT)
            self.cam.retrieve_measure(self.point_cloud, sl.MEASURE.XYZRGBA)
            self.cam.retrieve_measure(self.depth, sl.MEASURE.DEPTH)
        
        rgb_image = deepcopy(self.image.get_data())[:,:,:3]
        # perform bgr_to_rgb operation
        rgb_image = rgb_image[:,:,::-1]


        depth_image = deepcopy(self.depth.get_data())
        return rgb_image, depth_image

def convert_pose_to_rig(pose):
    # assume pose is xyz + q_xyzw
    # convert to rigid transform
    trans = pose[:3]
    angles_quat = pose[3:] # q_xyzw

    #Flip quat to wxyz
    angles_quat_wxyz = np.concatenate((angles_quat[[-1]], angles_quat[:-1]))
    #Get rotation matrix (3x3)
    rot = RigidTransform.rotation_from_quaternion(angles_quat_wxyz)
    rigid = RigidTransform(
            rotation=rot,
            translation=trans,
            from_frame="tcp",
            to_frame="tcp",
        )
    return rigid



class RobotEnv(gym.Env):
    def __init__(self, blocking_gripper=False, cam_ids=[22008760, 32474776]):
        # Initialize Gym Environment
        super().__init__()        
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(480, 640, 3), dtype=np.uint8)
        
        self.ros_inpaint_publisher = ROSInpaintPublisherReal()

        # Robot Configuration
        self.reset_joints = np.array([-190/180*np.pi, -102/180*np.pi, 141/180*np.pi, -130/180*np.pi, -np.pi/2, 168/180*np.pi])
        self.joint_randomize_low = -np.array([1, 1, 0.6, 1, 1, 1]) * 10 / 180 * np.pi
        self.joint_randomize_high = np.array([1, 1, 0.3, 1, 1, 1]) * 10 / 180 * np.pi
        self.cartesian_randomize_low = np.array([-0.05, -0.05, -0.05, -0.1, -0.1, -0.1])
        self.cartesian_randomize_high = np.array([0.05, 0.05, 0.05, 0.1, 0.1, 0.1])
        self.control_hz = 15

        print("Initializing gripper...")
        self.blocking_gripper = blocking_gripper
        if self.blocking_gripper:
            self._robot = UR5Robot(gripper=1)
        else:
            self._robot = UR5Robot(gripper=3)
            # self._robot.gripper.activate()
        self._robot.set_tcp(RigidTransform(translation=[0,0.0,-0.03], rotation=RigidTransform.z_axis_rotation(np.pi/2))) # Robotiq gripper
        # self._robot.set_tcp(RigidTransform(translation=[0,0.0,0.0], rotation=RigidTransform.z_axis_rotation(3*np.pi/4))) # Franka gripper    
        
        self.source_franka_target_robotiq = True
        
        
        # self._robot.gripper.set_speed(100) # from 0 to 100 %
        
        self._gripper_is_closed = None
        self._gripper_being_blocked = False

        # Create Cameras
        print("Initializing cameras...")
        self.cam_ids = cam_ids
        self.zedcam = ZedSensor(self.cam_ids[0])
        if len(self.cam_ids) >= 2:
            self.zedcam2 = ZedSensor(self.cam_ids[1], lefteye=False)
        else:
            self.zedcam2 = None

        # Initialize the space mouse
        # self._controller = SpaceMouseRobotController()
        time.sleep(0.1)
        
        
        # Reset Robot
        self.reset()
        
        self.task = None
        self.actions = None
        
    def receive_all_bytes(self, num_bytes: int):
        """
        Receives all the bytes.
        """
        data = bytearray(num_bytes)
        pos = 0
        while pos < num_bytes:
            cr = self.client_socket.recv_into(memoryview(data)[pos:])
            if cr == 0:
                raise EOFError("Socket closed")
            pos += cr
        return data


    def reset(self, randomize=False, noise_type="joint"):
        self._robot.gripper.open()
        self._gripper_is_closed = False

        pose = np.array([0.56343067,  0.00338203,  0.25930977,  3.13144658,  0.01786906, -0.00901092]) # tiger
        new_pose = convert_euler_to_rig(pose) # rotation matrix is [[1,0,0], [0,-1,0], [0,0,-1]]
        print(new_pose)
        self._robot.move_pose(new_pose, vel=1, acc=5)
        self.iterstep = 0
        
        # reset_joints = self.reset_joints.copy()
        # self._robot.move_joint(reset_joints)
        if randomize:
            if noise_type == "joint":
                noise = np.random.uniform(low=self.joint_randomize_low, high=self.joint_randomize_high)
                reset_joints += noise
                self._robot.move_joint(reset_joints)
            elif noise_type == "cartesian":
                current_pose = self._robot.get_pose()
                current_pose.from_frame = "tcp"
                
                pos_noise = np.random.uniform(low=self.cartesian_randomize_low[:3], high=self.cartesian_randomize_high[:3])
                rot_noise = np.random.uniform(low=self.cartesian_randomize_low[3:], high=self.cartesian_randomize_high[3:])

                noisy_rotation = R.from_euler("xyz", rot_noise, degrees=False).as_matrix()
                delta_pose = RigidTransform(
                    rotation=noisy_rotation, 
                    translation=pos_noise, 
                    from_frame="tcp",
                    to_frame="tcp",
                )
                noisy_pose = current_pose * delta_pose
                self._robot.move_pose(noisy_pose, vel=0.2, acc=1)

    def read_cameras(self):
        timestamp_dict = {}
        timestamp_dict["read_start"] = time_ms() - self.trajectory_start_time
        third_person_img = self.zedcam.read()
        if self.zedcam2 is not None:
            third_person_img2 = self.zedcam2.read()
            third_person_img2 = third_person_img2[0][::-1, ::-1, :], third_person_img2[1][::-1, ::-1]
        else:
            import copy
            third_person_img2 = copy.deepcopy(third_person_img)
        timestamp_dict["read_end"] = time_ms() - self.trajectory_start_time
        return third_person_img, third_person_img2, timestamp_dict

    def get_state(self):
        timestamp_dict = {}
        timestamp_dict["read_start"] = time_ms() - self.trajectory_start_time
        robot_pose = self._robot.get_pose()
        robot_joints = self._robot.get_joints()
        timestamp_dict["read_end"] = time_ms() - self.trajectory_start_time
        return robot_pose, robot_joints, timestamp_dict

    def get_camera_extrinsics(self, state_dict):
        # Adjust gripper camere by current pose
        pass

    def get_observation(self):
        state_dict = {}
        obs_dict = {}

        # Robot State #
        robot_pose, robot_joints, robot_timestamp_dict = self.get_state()
        state_dict["robot_pose"] = robot_pose
        state_dict["robot_joints"] = robot_joints
        state_dict["timestamp"] = robot_timestamp_dict

        # Camera Readings #
        third_person_img, third_person_img2, camera_timestamp_dict = self.read_cameras()
        obs_dict["third_person_image"] = third_person_img
        obs_dict["third_person_image2"] = third_person_img2
        obs_dict["timestamp"] = camera_timestamp_dict


        return state_dict, obs_dict

    def infer_action_from_observation(self, previous_pose:RigidTransform, new_pose:RigidTransform, previous_gripper_is_closed:bool, new_gripper_is_closed:bool):
        '''
        converts from rigidtransform pose to the UR format pose (x,y,z,rx,ry,rz)
        # gripper_action = 1 if gripper_is_closed changes from False to True, i.e., closing the gripper
        # gripper_action = -1 if gripper_is_closed changes from True to False, i.e., opening the gripper
        # no change = 0 if gripper_is_closed does not change
        '''
        previous_state = previous_pose.translation.tolist() + previous_pose.axis_angle.tolist()
        new_state = new_pose.translation.tolist() + new_pose.axis_angle.tolist()
        delta_state = list(np.array(new_state) - np.array(previous_state))

        gripper_action = int(new_gripper_is_closed) - int(previous_gripper_is_closed)
        return delta_state + [gripper_action] + [0] # 0 is the termination action

       

    def evaluate_robomimic_model_trajectory(self, model, traj_index=0, saving_directory="real_exps/rollout_data/", gripper_history_window = (1, 0.5, 0.5)):
        """
        gripper_history_window = (window_length, prediction_sum_threshold_close, prediction_sum_threshold_open): the last `window_length` frames of gripper prediction history will be used. 
        If the sum of the last `window_length` frames is greater than `prediction_sum_threshold_close`, then the gripper will be closed. 
        If the sum of the last `window_length` frames is less than `prediction_sum_threshold_open`, then the gripper will be opened. 
        """
        gripper_is_being_blocked = False
        fs_wrapper = FrameStackWrapper(num_frames=2)
        fs_wrapper.reset()
        imsize = 128

        gripper_action_history = queue.Queue()
        # populate the queue with zeros
        for i in range(gripper_history_window[0]):
            gripper_action_history.put(0)


        
        self.trajectory_start_time = time_ms()
        last_timestep = time.time()
        i = 0

        robot_actual_position_history = []
        desired_position_history = []
        gripper_position_history = []
        accumulated_error = np.array([0.,0.,0.,0.,0.,0.])
        while True:
            print(i)
            state_dict, obs_dict = self.get_observation()


            # for the standardized format:
            current_position = convert_rig_to_euler(state_dict["robot_pose"]) # 6D Euler
            
            
            if self.blocking_gripper:
                gripper_position = np.array([int(self._gripper_is_closed)])
            else:
                gripper_position = np.array([self._robot.gripper.get_current_position_normalized()])
            
            
            # execute the inpainting
            side_image = deepcopy(obs_dict["third_person_image"][0])
            front_image = deepcopy(obs_dict["third_person_image2"][0])
            
            from PIL import Image
            side_image_pil = Image.fromarray(side_image.astype(np.uint8))
            side_image_pil.save(os.path.join(saving_directory, "inpaintng_input_side.png"))
            front_image_pil2 = Image.fromarray(front_image.astype(np.uint8))
            front_image_pil2.save(os.path.join(saving_directory, "inpaintng_input_front.png"))
            
            # """
            depth_image = deepcopy(obs_dict["third_person_image"][1])
            joints = state_dict["robot_joints"]
            
            inpaint_publisher_input_data = ROSInpaintRealData(side_image, depth_image, np.concatenate([joints, gripper_position]))
            
            
            
            depth_image2 = deepcopy(obs_dict["third_person_image2"][1])
            joints = state_dict["robot_joints"]
            
            inpaint_publisher_input_data2 = ROSInpaintRealData(front_image[::-1, ::-1, :], depth_image2[::-1, ::-1], np.concatenate([joints, gripper_position]))
            
            
            print("Send to inpaint publisher")
            sending_time = time.time()
            self.ros_inpaint_publisher.publish_to_ros_node([inpaint_publisher_input_data, inpaint_publisher_input_data2])
            inpainted_side_image, inpainted_front_image, inpainted_side_image_mask, inpainted_front_image_mask = self.ros_inpaint_publisher.get_inpainted_image(True)
            print("Received inpainted image, took ", time.time() - sending_time, " seconds")
            
            inpainted_front_image = inpainted_front_image[::-1, ::-1, :]
            inpainted_front_image_mask = inpainted_front_image_mask[::-1, ::-1, :]
            
            # inpainted_side_image_pil = Image.fromarray(cv2.resize(inpainted_side_image, (imsize, imsize)).astype(np.uint8))
            inpainted_side_image_pil = Image.fromarray(inpainted_side_image.astype(np.uint8))
            inpainted_side_image_pil.save(os.path.join(saving_directory, "inpaintng_output.png"))
            
            # inpainted_front_image_pil = Image.fromarray(cv2.resize(inpainted_front_image, (imsize, imsize)).astype(np.uint8))
            inpainted_front_image_pil = Image.fromarray(inpainted_front_image.astype(np.uint8))
            inpainted_front_image_pil.save(os.path.join(saving_directory, "inpaintng_output_front.png"))
            
            # """
            # inpainted_side_image = side_image
            # inpainted_front_image = front_image
            
            writer = AsyncWrite(inpainted_side_image, obs_dict["third_person_image"][0], obs_dict["third_person_image"][1], traj_index, saving_directory, i, front=False)
            writer.start()
            
            # writer2 = AsyncWrite(inpainted_front_image, obs_dict["third_person_image2"][0], obs_dict["third_person_image2"][1][::-1, ::-1], traj_index, saving_directory, i, front=True)
            # writer2.start()
            
            
            inpainted_side_image_256 = cv2.resize(inpainted_side_image, (256, 256))
            

            
            
            to_tensor = transforms.ToTensor()
            side_image = to_tensor(cv2.resize(inpainted_side_image, (imsize, imsize)))
            front_image = to_tensor(cv2.resize(inpainted_front_image, (imsize, imsize)))
            obs = {
                "robot_state/cartesian_position": current_position,
                "robot_state/gripper_position": gripper_position,
                "camera/image/varied_camera_1_left_image": side_image,
                "camera/image/varied_camera_2_left_image": front_image
            }
            # breakpoint()
            fs_wrapper.add_obs(obs)
            obs_history = fs_wrapper.get_obs_history()
            
            action = model(obs_history)
            
            for j in range(3, 6):
                if action[j] < -np.pi/2:
                    action[j] += np.pi * 2
        
            print(action)

            
            gripper_action_history.get()
            gripper_action_history.put(action[-1])
            gripper_last_actions = gripper_action_history.queue # a deque object that is a copy of the queue
            

            
            
            absolute_position_action = action[:6]
            current_position = convert_rig_to_euler(self._robot.get_pose())
            for j in range(3, 6):
                if current_position[j] < -np.pi/2:
                    current_position[j] += np.pi * 2
            desired_position = current_position + (absolute_position_action - current_position) * 0.075
            desired_pose = convert_euler_to_rig(desired_position)
            
            
            
            if not self.blocking_gripper:
                current_gripper_position = self._robot.gripper.get_current_position_normalized()
                desired_gripper_position = current_gripper_position + action[-1] - current_gripper_position
                
                self._robot.gripper.set_pos(desired_gripper_position)
                new_pose = desired_pose
                new_pose.from_frame = "tcp"
                
                self._robot.servo_pose(new_pose, 0.002, 0.1, 100) # 10 Hz
                
            else:
                gripper_open = (action[-1] <= 0.05)
                if (self._gripper_is_closed and np.sum(gripper_last_actions) < gripper_history_window[2]):
                    print("Open gripper")
                    self._robot.gripper.open()
                    self._gripper_is_closed = False
                elif not self._gripper_is_closed and np.sum(gripper_last_actions) > gripper_history_window[1]:
                    print("Close gripper")
                    self._robot.gripper.close()
                    self._gripper_is_closed = True
                
                new_pose = desired_pose
                new_pose.from_frame = "tcp"
                self._robot.move_pose(new_pose, vel=0.2, acc=1)
            
            print(time.time() - last_timestep, " seconds has passed")
            # time.sleep(1 / self.control_hz)
            if time.time() - last_timestep < 1 / self.control_hz:
                time.sleep(last_timestep + 1 / self.control_hz - time.time())
            else:
                print("Warning: Control Loop is running slower than desired frequency")
                print(time.time() - last_timestep, " seconds has passed")
            last_timestep = time.time()

            robot_actual_position = convert_rig_to_euler(self._robot.get_pose())
            robot_actual_position_history.append(robot_actual_position)
            desired_position_history.append(desired_position)
            error = desired_position - robot_actual_position
            accumulated_error += error
            # print("Accumulated error:", accumulated_error)
            if not self.blocking_gripper:
                gripper_position = self._robot.gripper.get_current_position_normalized()
            else:
                gripper_position = int(self._gripper_is_closed)
            gripper_position_history.append(gripper_position)

            i += 1
            
    
    def evaluate_octo_model_trajectory(self, traj_index=0, saving_directory="real_exps/rollout_data/", gripper_history_window = (1, 0.5, 0.5)):
        """
        gripper_history_window = (window_length, prediction_sum_threshold_close, prediction_sum_threshold_open): the last `window_length` frames of gripper prediction history will be used. 
        If the sum of the last `window_length` frames is greater than `prediction_sum_threshold_close`, then the gripper will be closed. 
        If the sum of the last `window_length` frames is less than `prediction_sum_threshold_open`, then the gripper will be opened. 
        """
        gripper_is_being_blocked = False
        fs_wrapper = FrameStackWrapper(num_frames=1)
        fs_wrapper.reset()
        imsize = 256

        gripper_action_history = queue.Queue()
        # populate the queue with zeros
        for i in range(gripper_history_window[0]):
            gripper_action_history.put(0)


        
        self.trajectory_start_time = time_ms()
        last_timestep = time.time()
        i = 0

        robot_actual_position_history = []
        desired_position_history = []
        gripper_position_history = []
        accumulated_error = np.array([0.,0.,0.,0.,0.,0.])
        while True:
            print(i)
            state_dict, obs_dict = self.get_observation()


            # for the standardized format:
            current_position = convert_rig_to_euler(state_dict["robot_pose"]) # 6D Euler
            
            
            if self.blocking_gripper:
                gripper_position = np.array([int(self._gripper_is_closed)])
            else:
                gripper_position = np.array([self._robot.gripper.get_current_position_normalized()])
            
            
            # execute the inpainting
            side_image = deepcopy(obs_dict["third_person_image"][0])
            front_image = deepcopy(obs_dict["third_person_image2"][0])
            
            from PIL import Image
            side_image_pil = Image.fromarray(side_image.astype(np.uint8))
            side_image_pil.save(os.path.join(saving_directory, "inpaintng_input_side.png"))
            front_image_pil2 = Image.fromarray(front_image.astype(np.uint8))
            front_image_pil2.save(os.path.join(saving_directory, "inpaintng_input_front.png"))
            
            joints = state_dict["robot_joints"]                        
            inpainted_side_image = side_image
            inpainted_front_image = front_image
            
            writer = AsyncWrite(inpainted_side_image, obs_dict["third_person_image"][0], obs_dict["third_person_image"][1], traj_index, saving_directory, i, front=False)
            writer.start()
            
            writer2 = AsyncWrite(inpainted_front_image, obs_dict["third_person_image2"][0], obs_dict["third_person_image2"][1][::-1, ::-1], traj_index, saving_directory, i, front=True)
            writer2.start()            
            
            # to_tensor = transforms.ToTensor()
            side_image = cv2.resize(inpainted_side_image, (imsize, imsize))
            # import pdb; pdb.set_trace()
            cv2.imwrite(os.path.join(saving_directory, "test_side_image.png"), side_image)
            front_image = cv2.resize(inpainted_front_image, (imsize, imsize))
            
            proprio_state = np.concatenate([current_position, gripper_position])
            
            ext_1_left = Image.fromarray(side_image)
            ext_1_left.save(f"ext_1_finetune2.png")
            obs = {
                "proprio": proprio_state[None],
                "image_primary": side_image[None],
                "timestep_pad_mask": np.array([True]),
                "timestep": np.array([i]),
            }
            
            
            pred_actions = self.get_octo_action("", obs)
            if self.actions is None:
                self.actions = np.zeros_like(pred_actions)
                self.weights = 1 / (np.arange(len(pred_actions)) + 1)
            else:
                self.actions = np.concatenate([self.actions[1:], np.zeros_like(self.actions[-1:])])
                self.weights = np.concatenate([self.weights[1:], [1 / len(self.weights)]])
            self.actions += pred_actions * self.weights[:, None]

            # Take first action for now
            received_action = np.array(self.actions[0])

            for j in range(3, 6):
                if received_action[j] < -np.pi/2:
                    received_action[j] += np.pi * 2
        
            print(received_action)
            
            
            gripper_action_history.get()
            gripper_action_history.put(received_action[-1])
            gripper_last_actions = gripper_action_history.queue # a deque object that is a copy of the queue
            

            
            
            delta_action = received_action[:6]
            absolute_position_action = received_action[:6]
            current_position = convert_rig_to_euler(self._robot.get_pose())
            for j in range(3, 6):
                if current_position[j] < -np.pi/2:
                    current_position[j] += np.pi * 2
            # desired_position = current_position + delta_action * 0.075
            desired_position = current_position + (absolute_position_action - current_position) * 0.075
            desired_pose = convert_euler_to_rig(desired_position)
            
            
            
            if not self.blocking_gripper:
                current_gripper_position = self._robot.gripper.get_current_position_normalized()
                desired_gripper_position = current_gripper_position + received_action[-1] - current_gripper_position
                
                self._robot.gripper.set_pos(desired_gripper_position)
                new_pose = desired_pose
                new_pose.from_frame = "tcp"
                
                # self._robot.move_pose(new_pose, vel=0.2, acc=1)
                self._robot.servo_pose(new_pose, 0.002, 0.1, 100) # 10 Hz
                # self._robot.servo_pose(new_pose, 0.005, 0.1, 100) # 5 Hz
                
            else:
                gripper_open = (received_action[-1] <= 0.05)
                if (self._gripper_is_closed and np.sum(gripper_last_actions) < gripper_history_window[2]):
                    print("Open gripper")
                    self._robot.gripper.open()
                    self._gripper_is_closed = False
                elif not self._gripper_is_closed and np.sum(gripper_last_actions) > gripper_history_window[1]:
                    print("Close gripper")
                    self._robot.gripper.close()
                    self._gripper_is_closed = True
                
                new_pose = desired_pose
                new_pose.from_frame = "tcp"
                self._robot.move_pose(new_pose, vel=0.2, acc=1)
            
            print(time.time() - last_timestep, " seconds has passed")
            # time.sleep(1 / self.control_hz)
            if time.time() - last_timestep < 1 / self.control_hz:
                time.sleep(last_timestep + 1 / self.control_hz - time.time())
            else:
                print("Warning: Control Loop is running slower than desired frequency")
                print(time.time() - last_timestep, " seconds has passed")
            last_timestep = time.time()

            robot_actual_position = convert_rig_to_euler(self._robot.get_pose())
            robot_actual_position_history.append(robot_actual_position)
            desired_position_history.append(desired_position)
            error = desired_position - robot_actual_position
            accumulated_error += error
            # print("Accumulated error:", accumulated_error)
            if not self.blocking_gripper:
                gripper_position = self._robot.gripper.get_current_position_normalized()
            else:
                gripper_position = int(self._gripper_is_closed)
            gripper_position_history.append(gripper_position)

            i += 1
        robot_actual_position_history = np.array(robot_actual_position_history)
        desired_position_history = np.array(desired_position_history)
        
        return standard_output, action_traj, state_traj, obs_traj
    
    
    def load_octo_model(self, type="base"):
        '''
        Loads the octo model, taking in base if using octo base or small if using the small version
        '''
        from octo.model.octo_model import OctoModel
        if type == "base":
            self.octo_model = OctoModel.load_pretrained(
                '~/mirage/orca-r2d2_eval/orca-r2d2_eval/outputs_fixed_1_base/octo_finetune/experiment_20240202_223502',
                100000,
            )
            # with open('~/mirage/orca-r2d2_eval/orca-r2d2_eval/outputs/dataset_statistics.json') as f:
            #     self.dataset_statistics = json.load(f) 
        else:
            self.octo_model = OctoModel.load_pretrained(
                '~/mirage/orca-r2d2_eval/orca-r2d2_eval/outputs_fixed_1_small/octo_finetune/experiment_20240202_225655',
                100000
                )
            # with open('~/mirage/orca-r2d2_eval/orca-r2d2_eval/outputs_small/dataset_statistics.json') as f:
            #     self.dataset_statistics = json.load(f) 
    
        
    def get_octo_action(self, task_description, observations):
        '''
        Observation needs to consist of a "proprio" key, which is the concatenation of 
        cartesian position and gripper angle. It also needs a ""
        '''
        import jax
        import jax.numpy as jnp
        import logging
        import flax
        
        @partial(jax.jit, static_argnames="argmax")
        def sample_actions(
            pretrained_model,
            observations,
            tasks,
            rng,
            argmax=False,
            temperature=1.0,
        ):
            # add batch dim to observations
            observations = jax.tree_map(lambda x: x[None], observations)
            # tasks = jax.tree_map(lambda x: x[None], tasks)
            # logging.warning(
            #     "observations: %s", flax.core.pretty_repr(jax.tree_map(jnp.shape, observations))
            # )
            # logging.warning("tasks: %s", flax.core.pretty_repr(jax.tree_map(jnp.shape, tasks)))
            actions = pretrained_model.sample_actions(
                observations,
                tasks,
                rng=rng,
                argmax=argmax,
                temperature=temperature,
                unnormalization_statistics=pretrained_model.dataset_statistics["action"]
            )

            # unbatch the actions and return
            return actions[0]

        if not self.task:
            self.task = self.octo_model.create_tasks(texts=[task_description])
        actions = sample_actions(
            self.octo_model,
            observations,
            self.task,
            rng=jax.random.PRNGKey(0)
        )
        return actions
    
    
    

if __name__=="__main__":
        


    env = RobotEnv(blocking_gripper=False)
    env.load_octo_model('base')


    env.evaluate_robomimic_model_trajectory(None, traj_index=0, saving_directory="real_exps/rollout_data/robomimic", gripper_history_window = (1, 0.5, 0.5))
    # env.evaluate_octo_model_trajectory(traj_index=0, saving_directory="real_exps/rollout_data/octo", gripper_history_window = (1, 0.5, 0.5))
    