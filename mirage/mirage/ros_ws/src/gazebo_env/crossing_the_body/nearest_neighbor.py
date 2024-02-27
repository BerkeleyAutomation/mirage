import cv2
import numpy as np

# Load the result image with the masked region
img = cv2.imread('franka.jpg')

# Load the mask (same mask used earlier)
mask = cv2.imread('seg.jpg', 0)
_, mask = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)
inverted_mask = cv2.bitwise_not(mask)
result_image = cv2.bitwise_and(img, img, mask=inverted_mask)
#output = cv2.inpaint(img,mask,100,cv2.INPAINT_NS)
# Save or display the inpainted result
cv2.imwrite('test.jpg', result_image)  # Optionally, save the inpainted result image
cv2.imshow('Inpainted Result', result_image)  # Optionally, display the inpainted result
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close the window