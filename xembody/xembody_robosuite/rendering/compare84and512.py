from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the original 512x512 image
original_image = Image.open("/home/lawrence/xembody/xembody/xembody_robosuite/rendering/output/Panda_output_1img_agentview_rgb_512.png")

# Resize the image to 84x84
resized_image = original_image.resize((84, 84))

# Load another 84x84 image for comparison
comparison_image = Image.open("/home/lawrence/xembody/xembody/xembody_robosuite/rendering/output/Panda_output_1img_agentview_rgb.png")

# Convert images to numpy arrays for comparison
resized_np = np.array(resized_image)
comparison_np = np.array(comparison_image)

# Calculate the absolute difference between the images
difference = np.abs(resized_np.astype(np.float32) - comparison_np.astype(np.float32))

# Visualize the difference
plt.figure(figsize=(8, 4))

# Show the original 84x84 image
plt.subplot(1, 3, 1)
plt.title("Resized Image")
plt.imshow(resized_image)
plt.axis('off')

# Show the other 84x84 image for comparison
plt.subplot(1, 3, 2)
plt.title("Comparison Image")
plt.imshow(comparison_image)
plt.axis('off')

# Show the difference
plt.subplot(1, 3, 3)
plt.title("Difference")
plt.imshow(difference.astype(np.uint8))
plt.axis('off')

plt.tight_layout()
plt.show()
