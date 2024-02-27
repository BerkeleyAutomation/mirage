import numpy as np

world_to_usd = np.array([[-0.7071102, -0.4082502,  0.5773447],[0.7071034, -0.4082502,  0.5773531],[-0.0000034,  0.8164946,  0.5773531]])
usd_to_ros = np.array([[1,0,0],[0,-1,0],[0,0,-1]])
ros_to_cam = np.array([[0,-1,0],[0,0,-1],[1,0,0]])
world_to_cam = world_to_usd @ usd_to_ros @ ros_to_cam
print(world_to_cam)
print(world_to_usd @ usd_to_ros)