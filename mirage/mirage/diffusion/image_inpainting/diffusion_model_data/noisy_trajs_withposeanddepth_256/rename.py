import os
from PIL import Image
# Path to the directory containing folders
directory_path = '/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/diffusion_model_data/noisy_trajs_withposeanddepth_256/franka_analytic_inpainted'

# # Iterate through folders and rename them
# for i in range(1000):
#     old_folder_name = os.path.join(directory_path, f'demo_{i}')
#     new_folder_name = os.path.join(directory_path, str(i))

#     # Check if the folder exists before renaming
#     if os.path.exists(old_folder_name):
#         os.rename(old_folder_name, new_folder_name)
#         print(f"Renamed {old_folder_name} to {new_folder_name}")
#     else:
#         print(f"Folder {old_folder_name} not found")

# print("Folder renaming complete!")


for i in range(125):
    folder_path = os.path.join(directory_path, str(i))

    # Check if the folder exists
    if os.path.exists(folder_path):
        # List files in the folder
        files = os.listdir(folder_path)

        # Filter files with 'inpaint' prefix and '.png' extension
        inpaint_files = [file for file in files if file.startswith('inpaint') and file.endswith('.png')]

        # Rename and convert files in the folder
        for idx, old_name in enumerate(inpaint_files):
            file_extension = os.path.splitext(old_name)[1]  # Extract file extension
            new_name = old_name[7:-4] + ".jpg"  # New file name with JPG extension

            old_file_path = os.path.join(folder_path, old_name)
            new_file_path = os.path.join(folder_path, new_name)

            # Open the PNG file using PIL and convert to JPG
            img = Image.open(old_file_path)
            img = img.convert('RGB')  # Convert PNG with transparency to JPG

            # Save as JPG
            img.save(new_file_path)
            print(f"Converted {old_file_path} to {new_file_path}")

            # Remove the old PNG file
            os.remove(old_file_path)
            print(f"Removed {old_file_path}")

    else:
        print(f"Folder {folder_path} not found")

print("Conversion and renaming complete!")