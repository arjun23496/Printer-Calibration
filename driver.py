import numpy as np
import cv2 as cv
import phi_correction

img = cv.imread('imgs/WrongImage.bmp',0)

n = 3
i = 0

height = img.shape[0]
width = img.shape[1]

width1 = width/n
width_offset = 60

offset_h = height-250
init_h = 25

# subimg = img[offset_h:height-init_h,width1*i:(width1*i)+width_offset]

phi_correction.get_correction(img[height-500:height,width1*(i):width1*(i+1)])

# cv.imshow('image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()