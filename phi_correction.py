import math
import cv2 as cv
import numpy as np

def get_correction(img): #input is the y-corrected image
	print np.unique(img)
	height = img.shape[0]
	width = img.shape[1]

	vscanline1 = 11
	vscanline2 = 5310

	ivalue = img[1,vscanline1]

	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0

	#scanline1
	for x in range(2,height):
		if img[x,vscanline1]!=ivalue:
			x1 = vscanline1
			y1 = x
			break

	ivalue = img[1,vscanline1]

	# scanline2
	for x in range(2,height):
		if img[x,vscanline2]!=ivalue:
			x2 = vscanline2
			y2 = x
			break

	print x1,",",y1
	print x2,",",y2

	slope = 1.0*(y2-y1)/(x2-x1)
	print slope
	dev = math.degrees(math.atan(slope))
	print dev

	print 100.0*(0.05-dev)/0.05

	# cv.imshow('edges',edges)
	cv.imshow('image_original',img)
	cv.waitKey(0)
	cv.destroyAllWindows()

	# cv.imwrite('thresholding.bmp',thresh1)