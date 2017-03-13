import numpy as np
import cv2 as cv
import phi_correction

img = cv.imread('imgs/WrongImage.bmp',0)

print img.shape
phi_correction.get_correction(img[:,5312:10624])

# cv.imshow('image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()