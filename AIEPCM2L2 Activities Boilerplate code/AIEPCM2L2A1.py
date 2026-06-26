# Color Conversions and Cropping
import cv2

import numpy as np

import matplotlib.pyplot as plt
image = cv2.imread('example.jpg')
# Convert BGR to RGB
#image_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Cropping the image
cropped_image = image[100:300, 200:400]
# Assume we know the region we want: rows 100 to 300, columns 200 to 400
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 200, 200)
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.imshow('gray_image', gray_image)
cv2.waitKey(0)
cv2.imshow('cropped_image', cropped_image)
cv2.waitKey(0)