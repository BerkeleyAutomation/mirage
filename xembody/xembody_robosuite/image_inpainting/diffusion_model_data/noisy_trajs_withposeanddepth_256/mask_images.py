

import os
from PIL import Image, ImageChops


# Function to create the masked image
def create_masked_image(rgb_path, mask1_path, mask2_path, output_path):
    rgb_img = Image.open(rgb_path)
    mask1_img = Image.open(mask1_path).convert('1')
    mask2_img = Image.open(mask2_path).convert('1')

    # Ensure masks have the same size as the RGB image
    mask1_img = mask1_img.resize(rgb_img.size)
    mask2_img = mask2_img.resize(rgb_img.size)

    # Ensure masks have the same mode
    if mask1_img.mode != mask2_img.mode:
        mask2_img = mask2_img.convert(mask1_img.mode)

    # Combine masks to get the union
    union_mask = ImageChops.logical_or(mask1_img, mask2_img)

    # Invert the union mask to get the areas to keep
    keep_mask = ImageChops.invert(union_mask)

    # Separate RGB channels
    r, g, b = rgb_img.split()

    # Apply the masks to each RGB channel separately
    r_masked = ImageChops.composite(r, Image.new('L', rgb_img.size, 255), keep_mask)
    g_masked = ImageChops.composite(g, Image.new('L', rgb_img.size, 255), keep_mask)
    b_masked = ImageChops.composite(b, Image.new('L', rgb_img.size, 255), keep_mask)

    # Merge the masked channels back into an RGB image
    masked = Image.merge('RGB', (r_masked, g_masked, b_masked))

    # Save the resulting masked image
    masked.save(output_path)

# Input and output directories
root_dir = '/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/diffusion_model_data/noisy_trajs_withposeanddepth_256'

output_dir = 'masked_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for folder in range(125):
    folder_name = str(folder)
    output_folder = os.path.join(output_dir, folder_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Find the number of images in the RGB directory for this folder
    rgb_dir = os.path.join(root_dir, 'ur5e_rgb', folder_name)
    num_images = len([name for name in os.listdir(rgb_dir) if os.path.isfile(os.path.join(rgb_dir, name))])

    # Process corresponding images in each subdirectory
    for idx in range(num_images):
        rgb_path = os.path.join(root_dir, 'ur5e_rgb', folder_name, f"{idx}.jpg")
        mask1_path = os.path.join(root_dir, 'ur5e_mask', folder_name, f"{idx}.jpg")
        mask2_path = os.path.join(root_dir, 'franka_mask', folder_name, f"{idx}.jpg")
        
        output_path = os.path.join(output_folder, f"{idx}.jpg")
        
        if os.path.exists(rgb_path) and os.path.exists(mask1_path) and os.path.exists(mask2_path):
            create_masked_image(rgb_path, mask1_path, mask2_path, output_path)
        else:
            print(f"Images for folder {folder_name}, index {idx} not found in the directories")

print("Masked images generation complete.")