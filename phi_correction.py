import math
import cv2 as cv
import numpy as np

def get_correction(img, max_edges=1): #input is the y-corrected image
	print img.shape
	height = img.shape[0]
	width = img.shape[1]

	vscanline1 = 5
	vscanline2 = width - 5

	x1 = []
	x2 = []
	y1 = []
	y2 = []

	ivalue = img[2,vscanline1]

	#scanline1
	for x in range(2,height):
		if img[x,vscanline1]!=ivalue:
			x1.append(vscanline1)
			y1.append(x)
			i_value = img[x,vscanline1]
			if len(x1) >= max_edges:
				break

	ivalue = img[2,vscanline1]

	# scanline2
	for x in range(2,height):
		if img[x,vscanline2]!=ivalue:
			x2.append(vscanline2)
			y2.append(x)
			i_value = img[x,vscanline2]
			if len(x2) >= max_edges:
				break

	size = min(len(x1),len(x2))
	tot = 0

	for x in range(0, size):
		slope = 1.0*(y2[x]-y1[x])/(x2[x]-x1[x])
		tot = tot+slope

	slope = tot/size

	# slope = 1.0*(y2-y1)/(x2-x1)
	print slope
	dev = math.degrees(math.atan(slope))
	print dev

	print 100.0*(0.05-dev)/0.05

	# cv.imshow('edges',edges)
	cv.imshow('image_original',img)
	cv.waitKey(0)
	cv.destroyAllWindows()

	# cv.imwrite('thresholding.bmp',thresh1)