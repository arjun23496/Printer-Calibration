from __future__ import division
import math
import cv2 as cv
import numpy as np

# def get_correlation(img, max_edges=4, phi_error=0, n_lines=20, debug=True):
# 	width = img.shape[1]
# 	height = img.shape[0]
# 	xaccept = False
# 	yaccept = False	

# 	for x in range(0,height):
# 		if yaccept and img[x,1] != 0:
# 			break
# 		if img[x,1] != 0:
# 			continue
# 		ctr += 1
# 		if ctr < 1:
			# continue

def get_correction(img, max_edges=4, offset_set=1, phi_error=0, n_lines=20, padding=4, debug=True):
	img = img[:,padding:img.shape[1]-padding]

	# ret,thresh1 = cv.threshold(img,200,255,cv.THRESH_BINARY)
	# img = thresh1

	print img.shape
	# print np.unique(img)

	cv.imshow('image_original',img)
	cv.waitKey(0)
	cv.destroyAllWindows()

	width = img.shape[1]
	height = img.shape[0]
	xaccept = False
	yaccept = False

	tot = 0
	avg = 0

	for x in range(0,10):
		offset_set += 1
		xi=0
		yi=0
		x1=0
		y1=-1
		x2=width
		y2=-1
		ctr = 0

		yfactor = 1
		xfactor = 0

		while True:
			xi=xi+xfactor
			yi=yi+yfactor

			# print yi,",",xi
			# print img[yi,xi]

			# print img[xi,yi]

			if ctr<offset_set:
				if img[yi+1,xi]!=255 and img[yi,xi]==255:
					ctr+=1
				continue

			if y1 == -1:
				print "1 Top ",yi
				y1 = yi

			if img[yi+yfactor,xi] == 255:
				if yfactor == 1:
					print "1 bottom ",yi
					# y1 = (y1+yi)/2
					print "x1 y1 found"
					print x1,",",y1
					yfactor = -1
					# break
				else:
					if xi<width-1:
						xfactor = 1
						yfactor = 0
					else:
						y2 = yi
						break

			if (xi+xfactor==width or img[yi,xi+xfactor]==255) and xfactor!=255:
				xfactor = 0
				yfactor = -1

		yi = y2
		print "2 Top ",y2

		while True:
			yi = yi+1
			if img[yi+1,width-1]==255:
				print "2 Bottom ",yi
				# y2 = (y2+yi)/2
				break

		# n_size = len(xi)

		# slope = (yi[n_size-1] - yi[0])/(xi[n_size-1] - xi[0])
		print x1,",",y1
		print x2,",",y2
		# divisor = (y2-y1)/math.tan(phi_error)
		slope = (y2-y1)/(x2-x1)
		tot+=slope
		# print slope
		# print "divisor ",divisor

	avg = -tot/10
	dev = avg
	dev = math.atan(dev) 

	print "Deviation ",dev
	print "Original deviation ", phi_error
	if phi_error!=0:
		print "Percent ",(abs(phi_error-dev)/phi_error)*100

def get_correction1(img, min_edge_index=3, max_edges=5, phi_error=0, padding=40, debug=True): #input is the y-corrected image
	print img.shape
	height = img.shape[0]
	width = img.shape[1]

	vscanline1 = padding
	vscanline2 = width - padding

	x1 = []
	x2 = []
	y1 = []
	y2 = []

	ivalue = 255
	ctr = 0

	#scanline1
	for x in range(2,height):
		print img[x,vscanline1]
		if img[x,vscanline1]!=ivalue:
			ctr+=1
			if ctr < min_edge_index:
				continue
			x1.append(vscanline1)
			y1.append(x)
			i_value = img[x,vscanline1]
			if len(x1) >= max_edges:
				break

	ivalue = 255
	ctr = 0
	# scanline2
	for x in range(2,height):
		if img[x,vscanline2]!=ivalue:
			ctr+=1
			if ctr < min_edge_index:
				continue
			x2.append(vscanline2)
			y2.append(x)
			i_value = img[x,vscanline2]
			if len(x2) >= max_edges:
				break

	print y1
	print y2

	size = min(len(x1),len(x2))
	tot = 0

	print max_edges
	for x in range(0, min(size,max_edges)):
		print x1[x],",",y1[x]
		print x2[x],",",y2[x]
		slope = -1.0*(y2[x]-y1[x])/(x2[x]-x1[x])
		tot = tot+slope

	slope = tot/size

	# slope = 1.0*(y2-y1)/(x2-x1)
	print "Slope: "
	print slope
	dev = math.degrees(math.atan(slope))
	print "Deviation: "
	print dev

	if debug:
		print "Actual Deviation"
		print phi_error
		if phi_error != 0:
			print "Percent Error"
			print abs(100.0*(phi_error-dev)/phi_error)

	# cv.imshow('edges',edges)
	# cv.imshow('image_original',img)
	# cv.waitKey(0)
	# cv.destroyAllWindows()

	# cv.imwrite('thresholding.bmp',thresh1)