import numpy as np
import cv2 as cv
import phi_correction
import emulator

img = cv.imread('imgs/custom0.bmp',0)
# img = cv.imread('imgs/WrongImage.bmp',0)

# print type(img)

n = 6
i = 1

# phi_error = np.random.randint(0,20,n)
# phi_error = 1.0*phi_error/100
phi_error = [ 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.12, 0.13, 0.14, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0 ]
phi_error = [0.0, -0.05, 0.0]
# phi_error = [ 0.0, 0.05, 0.0 ]

height = img.shape[0]
width = img.shape[1]

width1 = width/3
width_offset = 60

offset_h = height-250
init_h = 25

# phi_correction.get_correction(img[height-500:height,width1*(i):width1*(i+1)])

##Image Creation
# print phi_error

# for x in range(0,n,3):
# 	if x+3 <= n:
# 		print "creating"
# 		emulator.create_image(img.shape, 3, phi_error=phi_error[x:x+3], filename='imgs/custom'+str(x)+'.bmp')

##Custom image manipulation



for x in range(0, n, 3):
	if x+3 >= n:
		break
	print "custom",x
	img = cv.imread('imgs/WrongImage.bmp',0)
	for i in range(0,3):
		print "--------Print head: ",(i+1)
		print "Target error ",phi_error[x+i]
		# phi_correction.get_correction(img[:, width1*(i):width1*(i+1)], max_edges=20, phi_error=phi_error[x+i])
		phi_correction.get_correction(img[offset_h:height-init_h, width1*(i):width1*(i+1)], max_edges=5, phi_error=phi_error[x+i])
		print "\n\n"

# subimg = img[offset_h:height-init_h,width1*i:(width1*i)+width_offset]

# cv.imshow('image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()