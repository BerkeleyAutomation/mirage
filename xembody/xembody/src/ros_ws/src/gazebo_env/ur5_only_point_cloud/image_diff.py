import cv2

image1 = cv2.imread('gazebo_img.jpg')
image2 = cv2.imread('img.jpg')
image_difference = cv2.absdiff(image1, image2)

    # Save the difference image
cv2.imwrite('image_difference.png', image_difference)

# import cv2
# import numpy as np

# # Load the two black and white images (replace with your image paths)
# image1 = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE)
# image2 = cv2.imread('image2.png', cv2.IMREAD_GRAYSCALE)

# # Create a blank blue channel (all zeros)
# blue_channel = np.zeros_like(image1)

# # Create an RGB image by combining the two images on the red and green channels
# composite_image = cv2.merge((image2, image1, blue_channel))

# # Save or display the composite image
# cv2.imwrite('composite_image.png', composite_image)

# # Display the composite image
# cv2.imshow('Composite Image', composite_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
