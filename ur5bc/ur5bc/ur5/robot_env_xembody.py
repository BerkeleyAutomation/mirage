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
from xembody.src.general.ros_inpaint_publisher_real import ROSInpaintPublisherReal, ROSInpaintRealData
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
        # rgb_image_cropped = rgb_image[:, 480:-80, :]  # Crop to 720x720 by selecting columns up to index 720
        # rgb_image_cropped = rgb_image[:, 160:-40, :]  # Crop to 720x720 by selecting columns up to index 720
        # rgb_image_resized = ColorImage(rgb_image_cropped).resize((128, 128))._data
        # Convert the numpy array back to an image
        # rgb_image_cropped = Image.fromarray(rgb_image_cropped.astype('uint8'), 'RGB')
        # rgb_image_resized = rgb_image_cropped.resize((128, 128)) # Resize the image to 128x128
        # rgb_image_resized = np.array(rgb_image_resized)
        # perform bgr_to_rgb operation
        rgb_image = rgb_image[:,:,::-1]


        depth_image = deepcopy(self.depth.get_data())
        # depth_array_resized = DepthImage(depth_image).resize((128, 128))._data
        # depth_array_cropped = depth_image[:, 480:-80]  # Crop to 720x720 by selecting columns up to index 720
        # depth_array_cropped = depth_image[:, 160:-40]  # Crop to 720x720 by selecting columns up to index 720
        # nan_mask = np.isnan(depth_array_cropped) # Create a mask for NaN values in the depth array
        # Replace NaN values with a placeholder (e.g., -1)
        # depth_array_cropped[nan_mask] = -1  # Or any other suitable placeholder
        # depth_array_cropped = depth_image
        # Resize the depth image to 128x128 using OpenCV, ignoring the placeholder
        # depth_array_resized = cv2.resize(depth_array_cropped, (128, 128), interpolation=cv2.INTER_LINEAR)
        # Replace the placeholder with NaN values in the resized depth array
        # depth_array_resized[depth_array_resized == -1] = np.nan

        # return rgb_image_resized, depth_array_resized, None
        # return deepcopy(self.image.get_data())[:,:,:3], deepcopy(self.depth.get_data()), deepcopy(self.point_cloud.get_data())
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
        # self.reset_joints = np.array([-np.pi, -105/180*np.pi, 105/180*np.pi, -np.pi/2, -np.pi/2, np.pi])
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
        # tiger, higher table
        # self._robot.set_tcp(RigidTransform(translation=[0.0, 0.0,0.], rotation=RigidTransform.z_axis_rotation(0))) # Test for no state alignment. The initial pose need to be added whatever is usually the argument of RigidTransform.z_axis_rotation
        # self._robot.set_tcp(RigidTransform(translation=[0.0, 0.0,0.015], rotation=RigidTransform.z_axis_rotation(np.pi/2))) # Robotiq gripper
        # self._robot.set_tcp(RigidTransform(translation=[0.03,-0.05,0.015], rotation=RigidTransform.z_axis_rotation(np.pi/2))) # Robotiq gripper
        # self._robot.set_tcp(RigidTransform(translation=[0,0.0,-0.03], rotation=RigidTransform.z_axis_rotation(np.pi/2))) # Robotiq gripper
        self._robot.set_tcp(RigidTransform(translation=[0,0.0,0.0], rotation=RigidTransform.z_axis_rotation(3*np.pi/4))) # Franka gripper
        # self._robot.set_tcp(RigidTransform(translation=[0,0.0,0.1], rotation=RigidTransform.z_axis_rotation(3*np.pi/4))) # Franka gripper
        
        # self._robot.set_tcp(RigidTransform(translation=[0,0.0,0.075], rotation=RigidTransform.z_axis_rotation(np.pi/2 - np.pi/4))) # Robotiq gripper
        
        
        
        self.source_franka_target_robotiq = True
        self.diffusion = False
        
        
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
        
        if self.diffusion:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            DIFFUSION_SERVER_PORT = 32003
            self.client_socket.connect(('localhost', DIFFUSION_SERVER_PORT))
            print("Connected to the diffusion server")
            self.prompt = "" #black background
            self.prompt = "create a high quality image with a Franka Panda robot, a green table with a stuffed animal tiger and black bowl, and a portrait painting in the background"

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

        # array([0.48647344, 0.02501339, 0.36250338, 3.09887758, 0.11696749, 0.09257838]) # toaster
        # array([ 0.48894271, -0.04181265,  0.2861726 ,  3.02394863, -0.03902772, -0.57621836])
        pose = np.array([ 0.56641978, -0.03237182,  0.38089544,  3.01054432,  0.03306557, -0.67646613]) # cup
        # pose = np.array([0.56343067,  0.00338203,  0.25930977,  3.13144658,  0.01786906, -0.00901092]) # tiger
        # pose = np.array([0.48894271,  -0.02338203,  0.23930977,  3.01054432,  0.03306557, -0.67646613]) # tiger
        # pose = np.array([0.56343067,  0.00338203,  0.25930977 + 0.07,  3.13144658,  0.01786906, -0.00901092])
        # pose = np.array([ 0.48894271, -0.04181265,  0.2861726 ,  3.02394863, -0.03902772, -0.57621836]) # drawer
        # pose = np.array([ 0.48979601, -0.06316637,  0.29236969,  3.17587143,  0.1426779 , 0.09521442])
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



    def record_teleop_trajectory(self, task_string, traj_index=0, saving_directory="/home/lawrence/robotlerf/ur5bc/data/raw/teleop/"):
        # Listen to the state from space mouse
        # Convert the state to ur5 action at 10 Hz
        # Execute the action
        # Record the action and state

        input("enter to start recording traj")

        gripper_is_being_blocked = False
        def trigger_gripper():
            print("Enter into trigger gripper at time {}".format(time_ms() - self.trajectory_start_time))
            nonlocal gripper_is_being_blocked
            def update_gripper_status():
                time.sleep(1.3)
                print("Start")
                self._gripper_is_closed = not self._gripper_is_closed
                print("End")
                    
            gripper_is_closed = self._gripper_is_closed
            t = threading.Thread(target=update_gripper_status) # start a child thread
            t.daemon = True
            t.start()
            gripper_is_being_blocked = True
            print("Start blocking gripper at time {}".format(time_ms() - self.trajectory_start_time))
            if gripper_is_closed:
                self._robot.gripper.open()
            else:
                self._robot.gripper.close()
            gripper_is_being_blocked = False
            print("End blocking gripper at time {}".format(time_ms() - self.trajectory_start_time))


        def keep_recording():
            nonlocal state_traj, obs_traj, action_traj, standard_output, gripper_is_being_blocked, last_timestep, i
            gripper_is_being_blocked = True # otherwise it will not enter the loop before trigger_gripper set gripper_is_being_blocked to True
            # if time.time() - last_timestep < 1 / self.control_hz:
            #     time.sleep(last_timestep + 1 / self.control_hz - time.time())
            # else:
            #     print("gripper_is_being_blocked")
            #     print("Warning: Control Loop is running slower than desired frequency")
            #     print(time.time() - last_timestep, " seconds has passed")
            while gripper_is_being_blocked:
                # print("Doing things at time {} ".format(time_ms() - self.trajectory_start_time), "for iteration ", i)

                # continue recording the state and observation at the same frequency
                state_dict, obs_dict = self.get_observation()
                state_traj["poses"].append(state_dict["robot_pose"].matrix)
                state_traj["joints"].append(state_dict["robot_joints"])
                state_traj["timestamp"]["read_start"].append(state_dict["timestamp"]["read_start"])
                state_traj["timestamp"]["read_end"].append(state_dict["timestamp"]["read_end"])
                state_traj["gripper_closed"].append(self._gripper_is_closed)
                state_traj["action_blocked"].append(True)
                obs_traj["hand_image"].append(obs_dict["hand_image"])
                obs_traj["third_person_image"].append(obs_dict["third_person_image"]) 
                obs_traj["timestamp"]["read_start"].append(obs_dict["timestamp"]["read_start"])
                obs_traj["timestamp"]["read_end"].append(obs_dict["timestamp"]["read_end"])
                writer = AsyncWrite(obs_dict["hand_image"], obs_dict["third_person_image"][0], obs_dict["third_person_image"][1], traj_index, saving_directory, i)
                writer.start()

                action_traj.append([0,0,0,0,0,0,0,0]) # do nothing
                
                # for the standardized format:
                pose = list(translation_from_matrix(state_dict["robot_pose"].matrix)) + list(quaternion_from_matrix(state_dict["robot_pose"].matrix)) # [x,y,z, qx,qy,qz,qw]
                robot_state = state_dict["robot_joints"] + pose + [self._gripper_is_closed] + [True] # [joint_angles, x,y,z, qx,qy,qz,qw, gripper_is_closed, action_blocked]
                image = obs_dict["third_person_image"][0]
                task = task_string
                standard_output["robot_state"].append(robot_state)
                standard_output["image"].append(image)
                standard_output["task"].append([task])
                standard_output["other"]["hand_image"].append(obs_dict["hand_image"])
                standard_output["other"]["third_person_image"].append(np.dstack((obs_dict["third_person_image"][0], obs_dict["third_person_image"][1])))
            
                if time.time() - last_timestep < 1 / self.control_hz:
                    time.sleep(last_timestep + 1 / self.control_hz - time.time())
                else:
                    print("Warning: Control Loop is running slower than desired frequency")
                    print(time.time() - last_timestep, " seconds has passed")
                last_timestep = time.time()
                i += 1
            print("Stop doing things at time {} ".format(time_ms() - self.trajectory_start_time), "for iteration ", i)
            return

        

        stop = False
        gripper_action = False
        state_traj = {"poses": [], "joints": [], "gripper_closed": [], "action_blocked": [], "timestamp":{"read_start": [], "read_end":[]}} # "poses": [RigidTransforms], "joints": Array(T, 6); "timestamp"/ "read_start": Array(T,), "read_end": Array(T,)
        obs_traj = {"hand_image": [], "third_person_image": [], "timestamp":{"read_start": [], "read_end":[]}}
        action_traj = []
        standard_output = {"robot_state": [], "action": [], "image": [], "task": [], "other": {"hand_image": [], "third_person_image": []}}
        last_timestep = time.time()
        i = 0
        self.trajectory_start_time = time_ms()

        while True:
            state_dict, obs_dict = self.get_observation()
            state_traj["poses"].append(state_dict["robot_pose"].matrix)
            state_traj["joints"].append(state_dict["robot_joints"])
            state_traj["timestamp"]["read_start"].append(state_dict["timestamp"]["read_start"])
            state_traj["timestamp"]["read_end"].append(state_dict["timestamp"]["read_end"])
            state_traj["gripper_closed"].append(self._gripper_is_closed)
            state_traj["action_blocked"].append(False)
            obs_traj["hand_image"].append(obs_dict["hand_image"])
            obs_traj["third_person_image"].append(obs_dict["third_person_image"]) 
            obs_traj["timestamp"]["read_start"].append(obs_dict["timestamp"]["read_start"])
            obs_traj["timestamp"]["read_end"].append(obs_dict["timestamp"]["read_end"])

            writer = AsyncWrite(obs_dict["hand_image"], obs_dict["third_person_image"][0], obs_dict["third_person_image"][1], traj_index, saving_directory, i)
            writer.start()

            # for the standardized format:
            pose = list(translation_from_matrix(state_dict["robot_pose"].matrix)) + list(quaternion_from_matrix(state_dict["robot_pose"].matrix)) # [x,y,z, qx,qy,qz,qw]
            robot_state = state_dict["robot_joints"] + pose + [self._gripper_is_closed] + [False] # [joint_angles, x,y,z, qx,qy,qz,qw, gripper_is_closed, action_blocked]
            image = obs_dict["third_person_image"][0]
            task = task_string
            standard_output["robot_state"].append(robot_state)
            standard_output["image"].append(image)
            standard_output["task"].append([task])
            standard_output["other"]["hand_image"].append(obs_dict["hand_image"])
            standard_output["other"]["third_person_image"].append(np.dstack((obs_dict["third_person_image"][0], obs_dict["third_person_image"][1])))
            

            if self._controller.button_1_pressed:
                stop = True
                action_traj.append([0,0,0,0,0,0,0,1]) # termination action
                break
            elif self._controller.button_0_pressed:
                last_timestep = time.time()
                # print("Go into the button pressed if statement at time ", time_ms() - self.trajectory_start_time, " milliseconds")
                if self._gripper_is_closed:
                    action_traj.append([0,0,0,0,0,0,-1,0]) # open gripper
                else:
                    action_traj.append([0,0,0,0,0,0,1,0]) # close gripper
                
                if time.time() - last_timestep < 1 / self.control_hz:
                    time.sleep(last_timestep + 1 / self.control_hz - time.time())
                else:
                    print("Warning: Control Loop is running slower than desired frequency")
                    print(time.time() - last_timestep, " seconds has passed")
                last_timestep = time.time()
                i += 1

                threadList = [threading.Thread(target=trigger_gripper), threading.Thread(target=keep_recording)]
                for threads in threadList:
                    threads.start()
                print("All threads started at time ", time_ms() - self.trajectory_start_time, " milliseconds")
                for threads in threadList:
                    threads.join()
                print("All threads ended at time ", time_ms() - self.trajectory_start_time, " milliseconds")
                
            else:    
                # import pdb; pdb.set_trace()
                # TODO: Tune the control gain
                self._controller_state = self._controller.current_action # x,y,z,roll,pitch,yaw
                translation = np.array(self._controller_state[:3]) * 0.02 # 1 will be 2cm
                translation[0] *= -1
                translation[-1] *= -1
                rotation = np.array(self._controller_state[3:]) / 15
                gripper_action = 0
                action = np.array([*translation, *rotation, gripper_action, 0]).tolist()
                action_traj.append(action)
                # q = quaternion_from_euler(action[3], action[4], action[5], 'ryxz')
                
                # print(euler_matrix(action[3], action[4], action[5], axes="syxz")[:3, :3] - euler_matrix(action[3], action[4], action[5], axes="ryxz")[:3, :3])
                delta_pose = RigidTransform(translation=translation, rotation=euler_matrix(action[3], action[4], action[5], axes="ryxz")[:3, :3], from_frame="tcp", to_frame="tcp")

                # Update Robot
                current_pose = self._robot.get_pose()
                current_pose.from_frame = "tcp"
                new_pose = current_pose * delta_pose
                # self._robot.move_pose(new_pose, vel=1, acc=10)
                self._robot.servo_pose(new_pose, 0.01, 0.2, 100)
                # with open('error_log.txt', 'a') as f:
                #     f.write(str(new_pose.translation - self._robot.get_pose().translation) + str(new_pose.rotation - self._robot.get_pose().rotation))
                #     f.write("\n")
            
                if time.time() - last_timestep < 1 / self.control_hz:
                    time.sleep(last_timestep + 1 / self.control_hz - time.time())
                else:
                    print("Warning: Control Loop is running slower than desired frequency")
                    print(time.time() - last_timestep, " seconds has passed")
                last_timestep = time.time()
                i += 1

        # Turn everything into numpy arrays
        standard_output["robot_state"] = np.array(standard_output["robot_state"]) # (T, 15)
        standard_output["image"] = np.stack(standard_output["image"], axis=0) # (T, 480, 640, 3)
        standard_output["action"] = np.array(action_traj) # (T, 8)
        standard_output["task"] = np.array(standard_output["task"]) # (T, 1)
        standard_output["other"]["hand_image"] = np.stack(standard_output["other"]["hand_image"], axis=0) # (T, 480, 640, 3)
        standard_output["other"]["third_person_image"] = np.stack(standard_output["other"]["third_person_image"], axis=0) # (T, 480, 640, 4)
        
        return standard_output, action_traj, state_traj, obs_traj


    def robot_trigger_gripper(self, command="close"):
        def update_gripper_status():
            time.sleep(1.3)
            print("Start")
            self._gripper_is_closed = not self._gripper_is_closed
            print("End")
        
        if command == "open" and self._gripper_is_closed:
            t = threading.Thread(target=update_gripper_status) # start a child thread
            t.daemon = True
            t.start()
            self._gripper_being_blocked = True
            self._robot.gripper.open()
            self._gripper_being_blocked = False
        elif command == "close" and not self._gripper_is_closed:
            t = threading.Thread(target=update_gripper_status) # start a child thread
            t.daemon = True
            t.start()
            self._gripper_being_blocked = True
            self._robot.gripper.close()
            self._gripper_being_blocked = False


    def step(self, action):
        """
        Execute the action
        """
        if self._gripper_being_blocked:
            print("Gripper is being blocked, cannot execute action")
            return 
        else:
            if action[-2] == 0:
                delta_pose = RigidTransform(translation=np.array([action[0], action[1], action[2]]), rotation=euler_matrix(action[3], action[4], action[5], axes="ryxz")[:3, :3], from_frame="tcp", to_frame="tcp")

                # Update Robot
                current_pose = self._robot.get_pose()
                current_pose.from_frame = "tcp"
                new_pose =  current_pose * delta_pose
                # self._robot.servo_pose(new_pose, 0.002, 0.1, 100) # 10 Hz
                self._robot.servo_pose(new_pose, 0.01, 0.2, 100) # 5 Hz
            elif action[-2] == 1:
                t = threading.Thread(target=self.trigger_gripper, args=("close",))
            elif action[-2] == -1:
                t = threading.Thread(target=self.trigger_gripper, args=("open",))
                
                t.daemon = True
                t.start()


    def play_franka_trajectory(self, state_traj, gripper_open_traj):
        """
        Execute the teleop trajectory from the starting state
        state_traj: np.array of shape (T, 7): trans + quat
        gripper_open_traj: np.array of shape (T,)
        """
        def trigger_gripper():
            def update_gripper_status():
                time.sleep(1.3)
                print("Start")
                self._gripper_is_closed = not self._gripper_is_closed
                print("End")
                    
            gripper_is_closed = self._gripper_is_closed
            t = threading.Thread(target=update_gripper_status) # start a child thread
            t.daemon = True
            t.start()
            if gripper_is_closed:
                self._robot.gripper.open()
            else:
                self._robot.gripper.close()


        input("enter to play trajectory")
        # go to the first pose first
        pose = state_traj[0]
        new_pose = convert_pose_to_rig(pose)
        self._robot.move_pose(new_pose, vel=0.8, acc=5)
        self._gripper_is_closed = False


        last_timestep = time.time()
        for i in range(len(state_traj)):
            pose = state_traj[i]
            gripper_open = gripper_open_traj[i]
            if self._gripper_is_closed and gripper_open == True:
                print("Open gripper")
                self._robot.gripper.open()
                self._gripper_is_closed = False
            elif not self._gripper_is_closed and gripper_open == False:
                print("Close gripper")
                self._robot.gripper.close()
                self._gripper_is_closed = True
            else:
                new_pose = convert_pose_to_rig(pose)
                # delta_pose = RigidTransform(translation=np.array([action[0], action[1], action[2]]), rotation=euler_matrix(action[3], action[4], action[5], axes="ryxz")[:3, :3], from_frame="tcp", to_frame="tcp")

                # # Update Robot
                # current_pose = self._robot.get_pose()
                # current_pose.from_frame = "tcp"
                # new_pose =  current_pose * delta_pose
                # self._robot.move_pose(new_pose, vel=1, acc=10)
                # self._robot.servo_pose(new_pose, 0.002, 0.1, 100) # 10 Hz
                self._robot.servo_pose(new_pose, 0.01, 0.2, 100) # 5 Hz

                if time.time() - last_timestep < 1 / self.control_hz:
                    time.sleep(last_timestep + 1 / self.control_hz - time.time())
                else:
                    print("Warning: Control Loop is running slower than desired frequency")
                    print(time.time() - last_timestep, " seconds has passed")
                last_timestep = time.time()
    
    def play_franka_trajectory_delta(self, traj):
        """
        Execute the teleop trajectory from the starting state
        """
        def trigger_gripper():
            def update_gripper_status():
                time.sleep(1.3)
                print("Start")
                self._gripper_is_closed = not self._gripper_is_closed
                print("End")
                    
            gripper_is_closed = self._gripper_is_closed
            t = threading.Thread(target=update_gripper_status) # start a child thread
            t.daemon = True
            t.start()
            if gripper_is_closed:
                self._robot.gripper.open()
            else:
                self._robot.gripper.close()


        input("enter to play trajectory")


        robot_actual_position_history = []
        desired_position_history = []
        accumulated_error = np.array([0.,0.,0.,0.,0.,0.])
        gripper_position_history = []
        
        action_cartesian_position = traj['action']['cartesian_position'][()]
        state_cartesian_position = traj['observation']['robot_state']['cartesian_position'][()]
        recorded_gripper_position = traj['observation']['robot_state']['gripper_position'][()]
        recorded_gripper_action = traj['action']['gripper_position'][()]
        for i in range(len(action_cartesian_position)):
            for j in range(3, 6):
                if action_cartesian_position[i, j] < -np.pi/2:
                    action_cartesian_position[i, j] += np.pi * 2
                if state_cartesian_position[i, j] < -np.pi/2:
                    state_cartesian_position[i, j] += np.pi * 2
        

        # go to the first pose first
        cartesian_pos_euler = state_cartesian_position[0]
        cartesian_pose = convert_euler_to_rig(cartesian_pos_euler)        
        self._robot.move_pose(cartesian_pose, vel=0.8, acc=5)
        self._gripper_is_closed = False
        breakpoint()
        self.trajectory_start_time = time_ms()
        last_timestep = time.time()
        for i in range(len(action_cartesian_position)+5):
            print(i)
            # get robot joints
            print(self._robot.get_joints())
            # if i == len(action_cartesian_position) - 1:
            #     self._robot.gripper.open()
            
            # state_dict, obs_dict = self.get_observation()
            # traj_index = 4
            # saving_directory = "/home/lawrence/xembody/ur5bc/rollout_data/tiger_background"
            # # execute the inpainting
            # side_image = deepcopy(obs_dict["third_person_image"][0])
            # front_image = deepcopy(obs_dict["third_person_image2"][0])
            
            # from PIL import Image
            # side_image_pil = Image.fromarray(side_image.astype(np.uint8))
            # side_image_pil.save(os.path.join(saving_directory, "inpaintng_input_side.png"))
            # front_image_pil2 = Image.fromarray(front_image.astype(np.uint8))
            # front_image_pil2.save(os.path.join(saving_directory, "inpaintng_input_front.png"))
            
            # # """
            # depth_image = deepcopy(obs_dict["third_person_image"][1])
            # joints = state_dict["robot_joints"]
            
            # if self.blocking_gripper:
            #     gripper_position = np.array([int(self._gripper_is_closed)])
            # else:
            #     gripper_position = np.array([self._robot.gripper.get_current_position_normalized()])
            
            
            # inpaint_publisher_input_data = ROSInpaintRealData(side_image, depth_image, np.concatenate([joints, gripper_position]))
            
            
            
            # depth_image2 = deepcopy(obs_dict["third_person_image2"][1])
            # joints = state_dict["robot_joints"]
            
            
            # inpaint_publisher_input_data2 = ROSInpaintRealData(front_image[::-1, ::-1, :], depth_image2[::-1, ::-1], np.concatenate([joints, gripper_position]))
            
            
            # print("Send to inpaint publisher")
            # sending_time = time.time()
            # self.ros_inpaint_publisher.publish_to_ros_node([inpaint_publisher_input_data, inpaint_publisher_input_data2])
            # inpainted_side_image, inpainted_front_image, inpainted_side_image_mask, inpainted_front_image_mask = self.ros_inpaint_publisher.get_inpainted_image(True)
            # print("Received inpainted image, took ", time.time() - sending_time, " seconds")
            
            # inpainted_front_image = inpainted_front_image[::-1, ::-1, :]
            # inpainted_front_image_mask = inpainted_front_image_mask[::-1, ::-1, :]
            
            # # inpainted_side_image_pil = Image.fromarray(cv2.resize(inpainted_side_image, (imsize, imsize)).astype(np.uint8))
            # inpainted_side_image_pil = Image.fromarray(inpainted_side_image.astype(np.uint8))
            # inpainted_side_image_pil.save(os.path.join(saving_directory, "inpaintng_output.png"))
            
            # # inpainted_front_image_pil = Image.fromarray(cv2.resize(inpainted_front_image, (imsize, imsize)).astype(np.uint8))
            # inpainted_front_image_pil = Image.fromarray(inpainted_front_image.astype(np.uint8))
            # inpainted_front_image_pil.save(os.path.join(saving_directory, "inpaintng_output_front.png"))
            
            # # """
            # # inpainted_side_image = side_image
            # # inpainted_front_image = front_image
            
            # writer = AsyncWrite(inpainted_side_image, obs_dict["third_person_image"][0], obs_dict["third_person_image"][1], traj_index, saving_directory, i, front=False)
            # writer.start()
            
            # writer2 = AsyncWrite(inpainted_front_image, obs_dict["third_person_image2"][0], obs_dict["third_person_image2"][1][::-1, ::-1], traj_index, saving_directory, i, front=True)
            # writer2.start()
            
            
            # inpainted_side_image_256 = cv2.resize(inpainted_side_image, (256, 256))
            
            # if self.diffusion:
            #     # make control_image a PIL image
            #     from PIL import Image
            #     control_image = Image.fromarray(inpainted_side_image_256)
            #     # control_image.save(os.path.join(saving_directory, f"traj{traj_index}", "images", f"diffusion_input_{i}.png"))
            #     control_image.save(os.path.join(saving_directory, f"diffusion_input.png"))
                
            #     sent_data = {
            #         "prompt": self.prompt,
            #         "control_image": control_image
            #     }
            #     serialized_data = pickle.dumps(sent_data)
            #     payload_size = len(serialized_data)
            #     byte_count = struct.pack("!I", payload_size)
            #     self.client_socket.send(byte_count)
            #     self.client_socket.send(serialized_data)

            #     received_payload_size = self.receive_all_bytes(4)
            #     received_payload_size = struct.unpack("!I", received_payload_size)[0]
            #     received_img_data = self.receive_all_bytes(received_payload_size)

            #     print("Diffusion Client has received image")

            #     cam_1_inpainted_image_diffusion = pickle.loads(received_img_data)
            #     # cam_1_inpainted_image_diffusion_copy = cam_1_inpainted_image_diffusion.clone()
            #     # # convert the tensor into a PIL image and resize it into 1280x720 and save it
            #     # breakpoint()
            #     # cam_1_inpainted_image_diffusion = cam_1_inpainted_image_diffusion.permute(1, 2, 0).cpu().numpy()
            #     # cam_1_inpainted_image_diffusion = cv2.resize(cam_1_inpainted_image_diffusion.astype(np.float32), (1280, 720))
            #     # cv2.imwrite(f"/home/r2d2/R2D2/scripts/evaluation/rollout_images/{self.iterstep}_diffusion.png", cv2.cvtColor((cam_1_inpainted_image_diffusion * 255).astype(np.uint8), cv2.COLOR_RGB2BGR))
            #     # resize the PIl image to 1280x720
            #     cam_1_inpainted_image_diffusion.resize((256, 256)).save(os.path.join(saving_directory, f"diffusion_output.png"))
            #     cam_1_inpainted_image_diffusion = cam_1_inpainted_image_diffusion.resize((1280, 720))
            #     cam_1_inpainted_image_diffusion.save(os.path.join(saving_directory, f"traj{traj_index}", "images", f"diffusion_output_{i}.png"))
            #     cam_1_inpainted_image_diffusion = np.array(cam_1_inpainted_image_diffusion)
            
            try:
            
                desired_pose = convert_euler_to_rig(state_cartesian_position[i])
                # Method 1: Velocity action. There are two sources of errors
                delta_action = traj['action']['cartesian_velocity'][()][i] * 0.075
                # Method 2: Position action. There is error from the groundtruth
                delta_action = (action_cartesian_position[i] - state_cartesian_position[i]) * 0.075
                # Method 3: Groundtruth action. No error if using move_pose
                delta_action = (state_cartesian_position[i+1] - state_cartesian_position[i])
                print("Diff: ", delta_action - (action_cartesian_position[i] - state_cartesian_position[i]) * 0.075)
                # print("Check", delta_action + state_cartesian_position[i] - state_cartesian_position[i+1])
                
                current_position = convert_rig_to_euler(self._robot.get_pose())
                desired_position = current_position + delta_action 
                desired_pose = convert_euler_to_rig(desired_position)
                
                if not self.blocking_gripper:
                    
                    # traj['action']['gripper_velocity'][()][i] * 0.25 * 0.25 = traj['action']['gripper_position'][()][i] - traj['observation']['robot_state']['gripper_position'][()][i] * 0.25 \approx= traj['action']['gripper_position'][()][i] - traj['observation']['robot_state']['gripper_position'][()][i]
                    
                    # Method 1: Velocity action. There are two sources of errors
                    delta_gripper_position = traj['action']['gripper_velocity'][()][i]
                    # print("Delta gripper position:", delta_gripper_position)
                    # Method 2: Position action. There is error from the groundtruth
                    delta_gripper_position = traj['action']['gripper_position'][()][i] - traj['observation']['robot_state']['gripper_position'][()][i]
                    # print("Delta gripper position:", delta_gripper_position)
                    
                    
                    current_gripper_position = self._robot.gripper.get_current_position_normalized()
                    desired_gripper_position = current_gripper_position + delta_gripper_position 
                    # print("Current and Desired gripper position:", current_gripper_position, desired_gripper_position)
                    # What the gripper actually reaches depends on the control frequency. If frequency is high, it will not reach the desired position (but closer to the groundtruth since groundtruth also is not reached, but 0.25 * delta_gripper_position).
                    self._robot.gripper.set_pos(desired_gripper_position)
                    new_pose = desired_pose
                    new_pose.from_frame = "tcp"
                    
                    self._robot.move_pose(new_pose, vel=0.2, acc=1)
                    # self._robot.servo_pose(new_pose, 0.002, 0.1, 100) # 10 Hz
                    # self._robot.servo_pose(new_pose, 0.005, 0.1, 600) # 5 Hz
                    
                else:
                    gripper_open = (traj['action']['gripper_position'][()][i] == 0)
                    if self._gripper_is_closed and gripper_open == True:
                        print("Open gripper")
                        self._robot.gripper.open()
                        self._gripper_is_closed = False
                    elif not self._gripper_is_closed and gripper_open == False:
                        print("Close gripper")
                        self._robot.gripper.close()
                        self._gripper_is_closed = True
                    
                    new_pose = desired_pose
                    new_pose.from_frame = "tcp"
                    self._robot.move_pose(new_pose, vel=0.2, acc=1)
                    # self._robot.servo_pose(new_pose, 0.002, 0.1, 100) # 10 Hz
                    # self._robot.servo_pose(new_pose, 0.005, 0.1, 600) # 5 Hz
            except:
                pass
            
            
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
            # print("Error from recorded traj:", state_cartesian_position[i+1] - robot_actual_position)
            if not self.blocking_gripper:
                gripper_position = self._robot.gripper.get_current_position_normalized()
            else:
                gripper_position = int(self._gripper_is_closed)
            gripper_position_history.append(gripper_position)
        
        robot_actual_position_history = np.array(robot_actual_position_history)
        desired_position_history = np.array(desired_position_history)
        plt.plot(recorded_gripper_position[1:], label="recorded gripper position")
        plt.plot(gripper_position_history, label="actual gripper position")
        plt.plot(recorded_gripper_action[1:], label="recorded gripper action")
        plt.legend()
        plt.show()
        
        for i in range(6):
            plt.plot(state_cartesian_position[1:, i], label=f"recorded position {i}")
            plt.plot(robot_actual_position_history[:, i], label=f"actual position {i}")
            # plt.plot(desired_position_history[:, i], label=f"desired position {i}")
            # plt.plot(traj['observation']['robot_state']['cartesian_position'][()][:, i] - robot_actual_position_history[:, i], label=f"position {i}")
            plt.legend()
            plt.show()
            

    def evaluate_robomimic_model_trajectory(self, model, traj_index=0, saving_directory="/home/lawrence/xembody/ur5bc/rollout_data/", gripper_history_window = (1, 0.5, 0.5)):
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
            
            # drawer
            # if self.source_franka_target_robotiq:
            #     current_position[0] -= 0.03
            #     current_position[1] += 0.04
            #     current_position[2] -= 0.04
                
            # cup
            if self.source_franka_target_robotiq:
                current_position[0] -= 0.015
                current_position[1] += 0.04
                current_position[2] -= 0.02
                
            else:
                pass
                # print("Current position: ", current_position)
                # current_position[0] -= 0.02
                # current_position[1] -= 0.01
                # current_position[2] += 0.03
                # current_position[-1] -= np.pi / 2
            
            
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
            
            if self.diffusion:
                # make control_image a PIL image
                from PIL import Image
                control_image = Image.fromarray(inpainted_side_image_256)
                # control_image.save(os.path.join(saving_directory, f"traj{traj_index}", "images", f"diffusion_input_{i}.png"))
                control_image.save(os.path.join(saving_directory, f"diffusion_input.png"))
                
                sent_data = {
                    "prompt": self.prompt,
                    "control_image": control_image
                }
                serialized_data = pickle.dumps(sent_data)
                payload_size = len(serialized_data)
                byte_count = struct.pack("!I", payload_size)
                self.client_socket.send(byte_count)
                self.client_socket.send(serialized_data)

                received_payload_size = self.receive_all_bytes(4)
                received_payload_size = struct.unpack("!I", received_payload_size)[0]
                received_img_data = self.receive_all_bytes(received_payload_size)

                print("Diffusion Client has received image")

                cam_1_inpainted_image_diffusion = pickle.loads(received_img_data)
                # cam_1_inpainted_image_diffusion_copy = cam_1_inpainted_image_diffusion.clone()
                # # convert the tensor into a PIL image and resize it into 1280x720 and save it
                # breakpoint()
                # cam_1_inpainted_image_diffusion = cam_1_inpainted_image_diffusion.permute(1, 2, 0).cpu().numpy()
                # cam_1_inpainted_image_diffusion = cv2.resize(cam_1_inpainted_image_diffusion.astype(np.float32), (1280, 720))
                # cv2.imwrite(f"/home/r2d2/R2D2/scripts/evaluation/rollout_images/{self.iterstep}_diffusion.png", cv2.cvtColor((cam_1_inpainted_image_diffusion * 255).astype(np.uint8), cv2.COLOR_RGB2BGR))
                # resize the PIl image to 1280x720
                cam_1_inpainted_image_diffusion.resize((256, 256)).save(os.path.join(saving_directory, f"diffusion_output.png"))
                cam_1_inpainted_image_diffusion = cam_1_inpainted_image_diffusion.resize((1280, 720))
                cam_1_inpainted_image_diffusion.save(os.path.join(saving_directory, f"traj{traj_index}", "images", f"diffusion_output_{i}.png"))
                cam_1_inpainted_image_diffusion = np.array(cam_1_inpainted_image_diffusion)
                inpainted_side_image = cv2.resize(cam_1_inpainted_image_diffusion, (imsize, imsize))
            
            
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
            # action[-2] += 3*np.pi/4
            # print("corrected action:", action)
            # action = np.array([0,0,0,0,0,0,0])
            
            # drawer
            # if self.source_franka_target_robotiq:
            #     action[0] += 0.03
            #     action[1] -= 0.04
            #     action[2] += 0.04
                
            # cup
            if self.source_franka_target_robotiq:
                action[0] += 0.015
                action[1] -= 0.04
                action[2] += 0.02
            else:
                action[0] += 0.02
                action[1] += 0.01
                action[2] -= 0.03

            
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
                
                # self._robot.move_pose(new_pose, vel=0.2, acc=1)
                self._robot.servo_pose(new_pose, 0.002, 0.1, 100) # 10 Hz
                # self._robot.servo_pose(new_pose, 0.005, 0.1, 100) # 5 Hz
                
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
                # self._robot.servo_pose(new_pose, 0.002, 0.1, 100) # 10 Hz
                # self._robot.servo_pose(new_pose, 0.005, 0.1, 600) # 5 Hz
            
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
    
    def evaluate_octo_model_trajectory(self, traj_index=0, saving_directory="/home/lawrence/xembody/ur5bc/rollout_data/", gripper_history_window = (1, 0.5, 0.5)):
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
            
            # drawer
            # if self.source_franka_target_robotiq:
            #     current_position[0] -= 0.015
            #     current_position[1] += 0.04
            #     current_position[2] -= 0.04
                
            # cup
            if self.source_franka_target_robotiq:
                current_position[0] -= 0.015
                # current_position[1] += 0.04
                # current_position[2] -= 0.02
                
            else:
                # current_position[0] -= 0.02
                current_position[1] -= 0.03
                current_position[2] += 0.03
            
            
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
            # import pdb; pdb.set_trace()
            
            proprio_state = np.concatenate([current_position, gripper_position])
            # import pdb; pdb.set_trace()
            
            ext_1_left = Image.fromarray(side_image)
            ext_1_left.save(f"ext_1_finetune2.png")
            # import pdb; pdb.set_trace()
            obs = {
                "proprio": proprio_state[None],
                "image_primary": side_image[None],
                "timestep_pad_mask": np.array([True]),
                "timestep": np.array([i]),
            }
            # breakpoint()
            # fs_wrapper.add_obs(obs)
            # obs_history = fs_wrapper.get_obs_history()
            
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
            # action = np.array([0,0,0,0,0,0,0])
            
            # drawer
            # if self.source_franka_target_robotiq:
            #     received_action[0] += 0.015
            #     received_action[1] -= 0.04
            #     received_action[2] += 0.04
                
            # cup
            if self.source_franka_target_robotiq:
                received_action[0] += 0.015
                received_action[1] -= 0.04
                # received_action[2] += 0.05
            else:
                # action[0] += 0.02
                # received_action[1] += 0.03
                received_action[2] -= 0.03

            
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
                # self._robot.servo_pose(new_pose, 0.002, 0.1, 100) # 10 Hz
                # self._robot.servo_pose(new_pose, 0.005, 0.1, 600) # 5 Hz
            
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
                '/home/lawrence/xembody/orca-r2d2_eval/orca-r2d2_eval/outputs_fixed_1_base/octo_finetune/experiment_20240202_223502',
                100000,
            )
            # with open('/home/lawrence/xembody/orca-r2d2_eval/orca-r2d2_eval/outputs/dataset_statistics.json') as f:
            #     self.dataset_statistics = json.load(f) 
        else:
            self.octo_model = OctoModel.load_pretrained(
                '/home/lawrence/xembody/orca-r2d2_eval/orca-r2d2_eval/outputs_fixed_1_small/octo_finetune/experiment_20240202_225655',
                100000
                )
            # with open('/home/lawrence/xembody/orca-r2d2_eval/orca-r2d2_eval/outputs_small/dataset_statistics.json') as f:
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
    
    
    
    def play_teleop_trajectory(self, action_traj, action_blocked, starting_state=None):
        """
        Execute the teleop trajectory from the starting state
        action_traj: np.array of shape (T, 8)
        action_blocked: np.array of shape (T,)
        """
        def trigger_gripper(command):
            print("triggering gripper")
            if command == "open":
                self._robot.gripper.open()
            elif command == "close":
                self._robot.gripper.close()
            print("gripper triggered")

        input("enter to play trajectory")
        if starting_state is not None:
            self._robot.move_joint(starting_state)
        
        last_timestep = time.time()
        for i in range(len(action_traj)):
            action = action_traj[i]
            if action_blocked[i]:
                time.sleep(1 / self.control_hz)
                last_timestep = time.time()
                continue
            if action[-1] == 1:
                break
            elif action[-2] == 0:
                delta_pose = RigidTransform(translation=np.array([action[0], action[1], action[2]]), rotation=euler_matrix(action[3], action[4], action[5], axes="ryxz")[:3, :3], from_frame="tcp", to_frame="tcp")

                # Update Robot
                current_pose = self._robot.get_pose()
                current_pose.from_frame = "tcp"
                new_pose =  current_pose * delta_pose
                # self._robot.move_pose(new_pose, vel=1, acc=10)
                # self._robot.servo_pose(new_pose, 0.002, 0.1, 100) # 10 Hz
                self._robot.servo_pose(new_pose, 0.01, 0.2, 100) # 5 Hz

                if time.time() - last_timestep < 1 / self.control_hz:
                    time.sleep(last_timestep + 1 / self.control_hz - time.time())
                else:
                    print("Warning: Control Loop is running slower than desired frequency")
                    print(time.time() - last_timestep, " seconds has passed")
                last_timestep = time.time()
            else:
                
                if action[-2] == 1:
                    t = threading.Thread(target=trigger_gripper, args=("close",))
                else:
                    t = threading.Thread(target=trigger_gripper, args=("open",))
                
                t.daemon = True
                t.start()
                time.sleep(1 / self.control_hz)
                last_timestep = time.time()



if __name__=="__main__":
    # path = "/home/lawrence/xembody/ur5bc/example_data/Thu_Jan_11_21:30:17_2024/trajectory_im128.h5" # tiger
    # path = "/home/lawrence/xembody/ur5bc/example_data/Wed_Jan_17_17:27:40_2024/trajectory_im128.h5" # drawer
    # path = "/home/lawrence/xembody/ur5bc/example_data/Sat_Jan_20_11:20:10_2024/trajectory_im128.h5" # toaster
    # path = "/home/lawrence/xembody/ur5bc/example_data/Sat_Jan_20_11:36:20_2024/trajectory_im128.h5" # toaster
    # path = "/home/lawrence/xembody/ur5bc/example_data/Wed_Jan_24_19:54:51_2024/trajectory_im128.h5" # tiger
    # path = "/home/lawrence/xembody/ur5bc/example_data/Wed_Jan_24_20:05:28_2024/trajectory_im128.h5" # tiger
    # path = "/home/lawrence/xembody/ur5bc/example_data/Wed_Jan_24_20:00:48_2024/trajectory_im128.h5" # tiger
    # path = "/home/lawrence/xembody/ur5bc/example_data/Sun_Jan_28_14:56:06_2024/trajectory_im128.h5" # cup
    # path = "/home/lawrence/xembody/ur5bc/example_data/Sun_Jan_28_15:23:12_2024/trajectory_im128.h5" # cup
    # path = "/home/lawrence/xembody/ur5bc/example_data/Sun_Jan_28_16:26:28_2024/trajectory_im128.h5" # cup
    # traj = h5py.File(path, 'r')
        


    env = RobotEnv(blocking_gripper=False)
    env.load_octo_model('base')
    env.evaluate_octo_model_trajectory(traj_index=0, saving_directory="/home/lawrence/xembody/ur5bc/rollout_data/octo", gripper_history_window = (1, 0.5, 0.5))

    # env.play_franka_trajectory(traj["ee_poses"], traj["gripper_open"])

    # env.play_franka_trajectory_delta(traj)
    # env.evaluate_robomimic_model_trajectory(None, traj_index=0, saving_directory="/home/lawrence/robotlerf/ur5bc/data/robomimic/", gripper_history_window = (1, 0.5, 0.5))
    