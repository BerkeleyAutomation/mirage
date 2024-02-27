import cv2
import numpy as np

# Load the world image and the mask (replace with your image and mask paths)
world_image = cv2.imread('inpainted_result_image.jpg')
franka_mask = cv2.imread('gazebo_mask.jpg',0)
_, franka_mask = cv2.threshold(franka_mask, 128, 255, cv2.THRESH_BINARY)
inverted_mask = cv2.bitwise_not(franka_mask)
result_image = cv2.bitwise_and(world_image, world_image, mask=inverted_mask)
mask = cv2.imread('gazebo_mask.jpg', 0)  # Load the mask in grayscale
#_, mask = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)
# Invert the mask
#inverted_mask = cv2.bitwise_not(mask)

# Create a new image that includes all parts of the world image except for the mask
#result_image = cv2.bitwise_and(world_image, world_image, mask=inverted_mask)
ur5_image = cv2.imread('gazebo_robot_only.jpg')
merge = ur5_image + result_image
# Save or display the result
cv2.imwrite('result_image.jpg', merge)  # Optionally, save the result image
cv2.imshow('Result Image', merge)  # Optionally, display the result image
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close the window
