import cv2
image=cv2.imread('C:/Users/Admin/OneDrive/Desktop/SNAPS/img.png')
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 200, 200)
cv2.imshow('Loaded Image', image)
key=cv2.waitKey(0)
if key==ord('s'):
    cv2.imwrite('input_image_small.jpg', image)
    print("Image saved as input_image_small.jpg")
else:
    print("Image not saved")
cv2.resizeWindow('Loaded Image', 400, 400)
cv2.imshow('Loaded Image', image)
key=cv2.waitKey(0)
if key==ord('s'):
    cv2.imwrite('input_image_medium.jpg', image)
    print("Image saved as input_image_medium.jpg")
else:
    print("Image not saved")
cv2.resizeWindow('Loaded Image', 600, 600)
cv2.imshow('Loaded Image', image)
key=cv2.waitKey(0)
if key==ord('s'):
    cv2.imwrite('input_image_large.jpg', image)
    print("Image saved as input_image_large.jpg")
else:
    print("Image not saved")