import cv2
import numpy as np

temp = "YesCube1.JPG"
img = cv2.imread(temp)
new_img = cv2.resize(img, (320, 240), interpolation = cv2.INTER_AREA)
cv2.imwrite("YesCube_1.jpg", new_img)
