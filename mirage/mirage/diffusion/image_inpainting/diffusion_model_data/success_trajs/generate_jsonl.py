import os
import json

ur5e_folder = '/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/diffusion_model_data/success_trajs/ur5e_rgb'
franka_folder = '/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/diffusion_model_data/success_trajs/franka_rgb'

jsonl_data = []

text = "replace the UR5 robot and its gripper with a Franka Panda robot and gripper at the exact same position and orientation"

# Iterate through the folders and pair images with the same indices
for ur5e_subfolder, franka_subfolder in zip(os.listdir(ur5e_folder), os.listdir(franka_folder)):
    ur5e_path = os.path.join(ur5e_folder, ur5e_subfolder)
    franka_path = os.path.join(franka_folder, franka_subfolder)

    # Check if both subfolders exist and are directories
    if os.path.isdir(ur5e_path) and os.path.isdir(franka_path):
        ur5e_images = sorted([os.path.join(ur5e_path, img) for img in os.listdir(ur5e_path)])
        franka_images = sorted([os.path.join(franka_path, img) for img in os.listdir(franka_path)])

        # Ensure both folders have the same number of images
        if len(ur5e_images) == len(franka_images):
            for ur5e_img, franka_img in zip(ur5e_images, franka_images):
                data_entry = {
                    "text": text,
                    "image": franka_img,  # Path to Franka Panda image
                    "conditioning_image": ur5e_img  # Path to UR5 image
                }
                jsonl_data.append(data_entry)

# Write data to a JSONL file
with open('paired_images.jsonl', 'w') as outfile:
    for entry in jsonl_data:
        json.dump(entry, outfile)
        outfile.write('\n')
