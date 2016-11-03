import numpy as np
import cv2

image1 = cv2.imread("boat.jpg")
image2 = cv2.imread("boat1.jpg")

difference = cv2.subtract(image1, image2)

result = not np.any(difference)

if result is True:
  print "The images are the same"
else:
  img = cv2.imwrite("result.jpg", difference)
  print "The images are different"