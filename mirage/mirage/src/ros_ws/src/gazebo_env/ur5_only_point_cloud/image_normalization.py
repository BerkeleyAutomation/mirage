import cv2
import numpy as np

# This function will return us the image stats
# We input an image in the L*a*b* color space and it returns
# a tuple of mean and std for L*, a* and b* respectively.
def image_stats(image):
    # Compute the mean and standard deviation of each channel
    (l, a, b) = cv2.split(image)
    (l_mean, l_std) = (l.mean(), l.std())
    (a_mean, a_std) = (a.mean(), a.std())
    (b_mean, b_std) = (b.mean(), b.std())

    # return the color statistics
    return (l_mean, l_std, a_mean, a_std, b_mean, b_std)


# This function will perform color transfer from one input image (source)
# onto another input image (destination)
def color_transfer(source, destination):
    # Convert the images from the RGB to L*a*b* color space, being
    # sure to utilizing the floating point data type (note: OpenCV
    # expects floats to be 32-bit, so use that instead of 64-bit)
    source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
    destination = cv2.cvtColor(destination, cv2.COLOR_BGR2LAB).astype("float32")

    # Compute color statistics for the source and destination images
    (l_mean_src, l_std_src, a_mean_src, a_std_src, b_mean_src, b_std_src) = image_stats(source)
    (l_mean_dest, l_std_dest, a_mean_dest, a_std_dest, b_mean_dest, b_std_dest) = image_stats(destination)

    # Subtract the means from the destination image
    (l, a, b) = cv2.split(destination)
    l -= l_mean_dest
    a -= a_mean_dest
    b -= b_mean_dest

    # Scale by the standard deviations
    l = (l_std_dest / l_std_src) * l
    a = (a_std_dest / a_std_src) * a
    b = (b_std_dest / b_std_src) * b

    # Add in the source mean
    l += l_mean_src
    a += a_mean_src
    b += b_mean_src

    # Clip the pixel intensities to [0, 255] if they fall outside this range
    l = np.clip(l, 0, 255)
    a = np.clip(a, 0, 255)
    b = np.clip(b, 0, 255)

    # Merge the channels together and convert back to the RGB color space,
    # being sure to utilize the 8-bit unsigned integer data type.
    transfer = cv2.merge([l, a, b])
    transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)

    # Return the color transferred image
    return transfer

# Load the original image and the segmentation gazebo_mask
gazebo_original_image = cv2.imread('gazebo_img.jpg')
gazebo_mask = cv2.imread('gazebo_mask.jpg', cv2.IMREAD_GRAYSCALE)
_, gazebo_mask = cv2.threshold(gazebo_mask, 128, 255, cv2.THRESH_BINARY)
# import pdb
# pdb.set_trace()
# gazebo_mask = np.expand_dims(gazebo_mask, axis=-1)
# result = gazebo_original_image * gazebo_mask
# result = result.squeeze()
# import pdb
# pdb.set_trace()
# # Ensure both the image and the gazebo_mask have the same dimensions
gazebo_mask = cv2.resize(gazebo_mask, (gazebo_original_image.shape[1], gazebo_original_image.shape[0]))

# Create a new image with the same size as the original image
gazebo_masked_image = np.zeros_like(gazebo_original_image)

# Apply the gazebo_mask to the original image using element-wise multiplication
gazebo_masked_image = cv2.bitwise_and(gazebo_original_image, gazebo_original_image, mask=gazebo_mask)

# Save or display the resulting gazebo_masked image
cv2.imwrite('gazebo_masked_image.jpg', gazebo_masked_image)  # Save the gazebo_masked image

# Load the original image and the segmentation gazebo_mask
isaac_original_image = cv2.imread('img.jpg')
isaac_mask = cv2.imread('seg.jpg', cv2.IMREAD_GRAYSCALE)
_, isaac_mask = cv2.threshold(isaac_mask, 128, 255, cv2.THRESH_BINARY)
# import pdb
# pdb.set_trace()
# gazebo_mask = np.expand_dims(gazebo_mask, axis=-1)
# result = gazebo_original_image * gazebo_mask
# result = result.squeeze()
# import pdb
# pdb.set_trace()
# # Ensure both the image and the gazebo_mask have the same dimensions
isaac_mask = cv2.resize(isaac_mask, (isaac_original_image.shape[1], isaac_original_image.shape[0]))

# Create a new image with the same size as the original image
isaac_masked_image = np.zeros_like(isaac_original_image)

# Apply the gazebo_mask to the original image using element-wise multiplication
isaac_masked_image = cv2.bitwise_and(isaac_original_image, isaac_original_image, mask=isaac_mask)

# Save or display the resulting gazebo_masked image
cv2.imwrite('isaac_masked_image.jpg', isaac_masked_image)  # Save the gazebo_masked image

source_image = isaac_masked_image
target_image = gazebo_masked_image

# Convert source and target images to LAB color space
source_lab = cv2.cvtColor(source_image, cv2.COLOR_BGR2LAB)
target_lab = cv2.cvtColor(target_image, cv2.COLOR_BGR2LAB)

# Extract the luminance channel (L) from LAB color space
source_luminance = source_lab[:,:,0]
target_luminance = target_lab[:,:,0]

# Perform histogram matching on the luminance channel
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
matched_luminance = clahe.apply(source_luminance)

# Replace the luminance channel in the source LAB image with the matched luminance
target_lab[:,:,0] = matched_luminance

# Convert the modified LAB image back to BGR color space
matched_image = cv2.cvtColor(target_lab, cv2.COLOR_LAB2BGR)

cv2.imwrite('output.jpg', cv2.absdiff(isaac_masked_image,gazebo_masked_image))

# Load the original image and the segmentation gazebo_mask
second_gazebo_original_image = cv2.imread('second_image.jpg')
second_gazebo_mask = cv2.imread('second_image_mask.jpg', cv2.IMREAD_GRAYSCALE)
_, second_gazebo_mask = cv2.threshold(second_gazebo_mask, 128, 255, cv2.THRESH_BINARY)
# import pdb
# pdb.set_trace()
# gazebo_mask = np.expand_dims(gazebo_mask, axis=-1)
# result = gazebo_original_image * gazebo_mask
# result = result.squeeze()
# import pdb
# pdb.set_trace()
# # Ensure both the image and the gazebo_mask have the same dimensions
second_gazebo_mask = cv2.resize(second_gazebo_mask, (second_gazebo_original_image.shape[1], second_gazebo_original_image.shape[0]))

# Create a new image with the same size as the original image
second_gazebo_masked_image = np.zeros_like(second_gazebo_original_image)

# Apply the gazebo_mask to the original image using element-wise multiplication
second_gazebo_masked_image = cv2.bitwise_and(second_gazebo_original_image, second_gazebo_original_image, mask=second_gazebo_mask)
cv2.imwrite('second_try.jpg',second_gazebo_masked_image)
target2_image = second_gazebo_masked_image
target2_lab = cv2.cvtColor(target2_image, cv2.COLOR_BGR2LAB)
target2_luminance = target2_lab[:,:,0]
matched2_luminance = clahe.apply(source_luminance)
target2_lab[:,:,0] = matched2_luminance 
matched2_image = cv2.cvtColor(target2_lab, cv2.COLOR_LAB2BGR)

cv2.imwrite('second_try_luminance.jpg', matched2_image)
