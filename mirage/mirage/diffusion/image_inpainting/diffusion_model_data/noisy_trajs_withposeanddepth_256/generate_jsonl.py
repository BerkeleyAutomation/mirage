import os
import json

# ur5e_folder = '/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/diffusion_model_data/success_trajs_withposeanddepth_256/ur5e_rgb'
franka_folder = '/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/diffusion_model_data/noisy_trajs_withposeanddepth_256/franka_rgb'
# ur5e_folder = '/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/diffusion_model_data/noisy_trajs_withposeanddepth_256/masked_images'
ur5e_folder = '/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/diffusion_model_data/noisy_trajs_withposeanddepth_256/franka_analytic_inpainted'

jsonl_data = []

# text = "replace the UR5 robot and its gripper with a Franka Panda robot and gripper at the exact same position and orientation"
# text = "inpaint the masked region with a Franka Panda robot"
text = "remove artifacts in the image"

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
                    "image": franka_img, #'/'.join(franka_img.split('/')[-2:]),  # Path to Franka Panda image
                    "conditioning_image": ur5e_img, #'/'.join(ur5e_img.split('/')[-2:])  # Path to UR5 image
                }
                jsonl_data.append(data_entry)
        else:
            print(f"Folder {ur5e_subfolder} has {len(ur5e_images)} UR5 images and {len(franka_images)} Franka images")
            for ur5e_img in ur5e_images:
                data_entry = {
                    "text": text,
                    "image": ur5e_img.replace('franka_analytic_inpainted', 'franka_rgb'), #'/'.join(ur5e_img.split('/')[-2:]),  # Path to Franka Panda image
                    "conditioning_image": ur5e_img, #'/'.join(ur5e_img.split('/')[-2:])  # Path to UR5 image
                }
                jsonl_data.append(data_entry)
                
# Write data to a JSONL file
with open('paired_images_analytic_improve.jsonl', 'w') as outfile:
    for entry in jsonl_data:
        json.dump(entry, outfile)
        outfile.write('\n')
