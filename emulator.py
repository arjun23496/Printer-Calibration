import cv2 as cv
import numpy as np

def create_image(dimension, n_head=1, phi_error=None, filename="custom.bmp"):
	if phi_error == None:
		phi_error = np.zeros(n_head)

	head_width = dimension[1]/n_head

	line_width = 20
	line_gap = 40

	lg = line_gap
	lw = line_width

	img = np.zeros(dimension)

	for x in range(0,dimension[0]):
		if lg > 0:
			lg-=1
		elif lw > 0:
			lw-=1
			img[x] = 255
		else:
			lw=line_width
			lg=line_gap

	for x in range(0, n_head):
		if phi_error[x] != 0:
			widthi = x*head_width
			widthj = (x+1)*head_width
			subimg = img[:,widthi:widthj]
			rows = subimg.shape[0]
			cols = subimg.shape[1]
			M = cv.getRotationMatrix2D((rows/2,cols/2),phi_error[x],1)
			subimg = cv.warpAffine(subimg,M,(cols,rows))
			img[:, widthi:widthj] = subimg

	print img.shape
	print dimension

	cv.imwrite(filename,img)	