from collections import Counter
import cv2
import argparse
import numpy as np
from matplotlib import pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = True, help = "Path to the test image, based on which calibration is made")
ap.add_argument("-n", "--printheads", required = True, help = "Number of print heads")
args = vars(ap.parse_args())
#base image "single.bmp"

basePath = "./single.bmp"
baseData = cv2.imread(basePath, 0)

def single_printhead_image_create() :
	pass

def phideviation() :
	pass

def get_error(section, baseData, offsetleft=0, offsetright=0):

	fr = Counter()
	n = len(section)
	m = len(section[0])
	e = 0
	if offsetleft != 0:
		e = offsetleft
	elif offsetright !=0:
		e = offsetright

	for i in range(n):
		c = 0
		for j in range(m-e):
			if section[i][j + offsetleft] != baseData[i][j+offsetright]:
				c+=1
		fr[c]+=1
	if e == 0:
		plot(fr)
	error = fr.most_common(1)[0][0]
	return error

def plot(fr):
	lst = fr.items()
	x = []
	y = []
	for i in lst:
		x.append(i[0])
		y.append(i[1])
	plt.scatter(x, y)
	plt.show()

def ydeviation(section) :
	testData = section
	
	value = np.array_equal(baseData,testData)
	if value == True:
		return "No error"

	error = get_error(section, baseData)
	right = get_error(section, baseData, offsetleft=0, offsetright=error)
	left =  get_error(section, baseData, offsetleft=error, offsetright=0)
	direction = ""
	if right == 0:
		direction = "Push to Right"
	else:
		direction = "Push to Left"

	return error, direction
	


#main program control

imagePath = args['input']

inputData = cv2.imread(imagePath, 0)

n = args['printheads']

startX = 0
endX = 5312
for i in range(int(n)) :
	section = inputData[0:1320, startX:endX]
	startX = endX
	endX = startX + 5312
	print ydeviation(section)



#phidev(imagePath)


