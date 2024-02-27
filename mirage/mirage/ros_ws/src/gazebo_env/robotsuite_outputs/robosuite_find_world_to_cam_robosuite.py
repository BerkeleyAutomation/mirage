import numpy as np

world_to_image = np.array(
    [
        [0, 0.70614724 , -0.70806503,0.5],
        [1, 0, 0,0],
        [0, -0.70806503, -0.70614724,1.35],
        [0,0,0,1]
    ]
)
image_to_cam = np.array(
    [
        [0,-1,0,0],
        [0,0,-1,0],
        [1,0,0,0],
        [0,0,0,1]
    ]
)
world_to_cam = world_to_image @ image_to_cam
cam_to_world = np.linalg.inv(world_to_cam)
print(cam_to_world)