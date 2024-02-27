import h5py
import cv2
import numpy as np
input = '/home/benchturtle/cross_embodiment_ws/src/gazebo_env/franka_to_franka/image_v141_copy.hdf5'
output = '/home/benchturtle/cross_embodiment_ws/src/gazebo_env/franka_to_franka/image_v141_inpaint.hdf5'

with h5py.File(input, 'r+') as file:
    for i in range(len(file['data'].keys())):
        demo_str = 'demo_'+str(i)
        obs = file['data'][demo_str]['obs']
        obs_agentview_image_inpainted = None
        next_obs_agentview_image_inpainted = None
        for j in range(obs['agentview_image'].shape[0]):
            inpaint_file_path = '/home/benchturtle/cross_embodiment_ws/franka_to_franka/demo_' + str(i) + '/inpaint' + str(j) + '.png'
            next_inpaint_file_path = '/home/benchturtle/cross_embodiment_ws/franka_to_franka/demo_' + str(i) + '/inpaint' + str(j+1) + '.png'
            if(j+1 == obs['agentview_image'].shape[0]):
                next_inpaint_file_path = inpaint_file_path
            inpaint_obs_image = cv2.imread(inpaint_file_path)
            inpaint_next_obs_image = cv2.imread(inpaint_file_path)
            inpaint_obs_image = inpaint_obs_image[np.newaxis,:]
            inpaint_next_obs_image = inpaint_next_obs_image[np.newaxis,:]
            if(obs_agentview_image_inpainted is None):
                obs_agentview_image_inpainted = inpaint_obs_image
                next_obs_agentview_image_inpainted = inpaint_next_obs_image
            else:
                obs_agentview_image_inpainted = np.concatenate((obs_agentview_image_inpainted,inpaint_obs_image))
                next_obs_agentview_image_inpainted = np.concatenate((next_obs_agentview_image_inpainted,inpaint_next_obs_image))
        file['data'][demo_str]['obs']['agentview_image_inpainted'] = obs_agentview_image_inpainted
        file['data'][demo_str]['next_obs']['agentview_image_inpainted'] = next_obs_agentview_image_inpainted
