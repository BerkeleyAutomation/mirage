import cv2
import numpy as np

# Load the two binary masks (white object on black background)
mask1 = cv2.imread('gazebo_mask.jpg', cv2.IMREAD_GRAYSCALE)
mask2 = cv2.imread('seg.jpg', cv2.IMREAD_GRAYSCALE)

# Find contours in the thresholded image
contours, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# Merge all individual contours into a single contour
# Merge all individual contours into a single contour
combined_contour = np.concatenate(contours)
# Create an image with the combined contour
image_with_combined_contour = cv2.cvtColor(mask1, cv2.COLOR_GRAY2BGR)
cv2.drawContours(image_with_combined_contour, [combined_contour], -1, (0, 0, 255), 2)

# Display the image with the combined contour
cv2.imshow('Image with Combined Contour', image_with_combined_contour)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Find the binary difference between the two masks
diff_mask = cv2.absdiff(mask1, mask2)
cv2.imwrite('diff_mask.png',diff_mask)
# Use contour detection to find the object in the difference mask
contours, _ = cv2.findContours(diff_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assuming only one object is detected, calculate its centroid
if len(contours) == 1:
    M = cv2.moments(contours[0])
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    # Calculate translation to align mask2 with mask1
    translation_matrix = np.array([[1, 0, mask1.shape[1] // 2 - cx], [0, 1, mask1.shape[0] // 2 - cy]], dtype=np.float32)

    # Calculate rotation angle using Hough Line Transform
    lines = cv2.HoughLines(diff_mask, 1, np.pi / 180, 200)
    if lines is not None:
        for rho, theta in lines[0]:
            rotation_angle = (theta - np.pi / 2) * 180 / np.pi  # Convert to degrees
            break
    else:
        rotation_angle = 0  # Default to no rotation

    # Calculate scaling factor based on object sizes
    object1_size = cv2.countNonZero(mask1)
    object2_size = cv2.countNonZero(mask2)
    scaling_factor = object1_size / object2_size

    # Apply similarity transformation to align mask2 with mask1
    similarity_matrix = cv2.getRotationMatrix2D((mask2.shape[1] // 2, mask2.shape[0] // 2), rotation_angle, scaling_factor)
    aligned_mask2 = cv2.warpAffine(mask2, similarity_matrix, (mask2.shape[1], mask2.shape[0]))
    aligned_mask2 = cv2.warpAffine(aligned_mask2, translation_matrix, (mask1.shape[1], mask1.shape[0]))

    # Save or display the aligned mask2
    cv2.imwrite('aligned_mask2.png', aligned_mask2)
else:
    print("Multiple or no objects detected in the difference mask.")
