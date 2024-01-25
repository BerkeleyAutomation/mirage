import cv2

gazebo_rgb_real = cv2.imread('gazebo_rgb_real.png')
rgb = cv2.imread('rgb.png')
cv2.imwrite('test.png',abs(gazebo_rgb_real-rgb))