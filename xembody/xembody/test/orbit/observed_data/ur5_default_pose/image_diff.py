import cv2
import numpy as np
import argparse

def save_image_difference(input_image1, input_image2, output_image):
    # Read the input images
    image1 = cv2.imread(input_image1)
    image2 = cv2.imread(input_image2)

    # Ensure the input images have the same dimensions
    if image1.shape != image2.shape:
        raise ValueError("Input images must have the same dimensions.")

    # Calculate the absolute difference between the images
    difference = cv2.absdiff(image1, image2)

    # Save the difference image
    cv2.imwrite(output_image, difference)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Save the difference between two images.")
    parser.add_argument("input_image1", help="Path to the first input image")
    parser.add_argument("input_image2", help="Path to the second input image")
    parser.add_argument("output_image", help="Path to save the difference image")

    args = parser.parse_args()

    try:
        save_image_difference(args.input_image1, args.input_image2, args.output_image)
        print(f"Difference image saved as {args.output_image}")
    except Exception as e:
        print(f"Error: {e}")
