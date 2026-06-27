import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread(
    "C:/Users/Admin/OneDrive/Desktop/SNAPS/img.png"
)

if image is None:
    print("Image not found!")
    exit()

# Original
cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded Image",300,400)
cv2.imshow("Loaded Image",image)

# Gray
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

cv2.imshow("Gray",gray)

# Matplotlib
plt.imshow(
    cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
)
plt.title("Original Image")
plt.axis("off")
plt.show()

# Crop
crop = image[100:300,100:300]
cv2.imshow("Crop",crop)

# Rotate
matrix = cv2.getRotationMatrix2D(
    (100,100),
    45,
    1
)

rotated = cv2.warpAffine(
    image,
    matrix,
    (image.shape[1],image.shape[0])
)

cv2.imshow("Rotated",rotated)

# Brightness
bright = cv2.add(
    image,
    np.ones(image.shape,dtype=np.uint8)*50
)

cv2.imshow("Bright",bright)

# Save
cv2.imwrite("output_image.png",rotated)

cv2.waitKey(0)

cv2.destroyAllWindows()