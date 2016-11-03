import numpy as np
import cv2
import time

start = time.time()

image1 = cv2.imread("mike.jpg")
image2 = cv2.imread("mike1.jpg")

difference = cv2.subtract(image1, image2)

result = not np.any(difference)

if result is True:
  print "The images are the same"
else:
  img = cv2.imwrite("result.jpg", difference)
  print "The images are different"

end = time.time()
print end-start