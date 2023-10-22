import cv2
import sys

def display_image(file_path):
    # Load the image
    image = cv2.imread(file_path)

    if image is None:
        print("Error: Could not load the image.")
    else:
        # Display the image
        cv2.imshow('Image', image)
        cv2.waitKey(0)  # Wait for a key press
        cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python display_image.py <image_file_path>")
    else:
        file_path = sys.argv[1]
        display_image(file_path)
