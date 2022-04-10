#Jeremy Lynch
#11346967 
#Utilizes OpenCV-Python to read in and show images.
import cv2

#Read image into 2D-array (matrix)
img = cv2.imread('noisy-elliptical-object.png')


#Center +50 starting at top img[rows/2+50][cols/2]
rows = int(len(img)/2 - 1)
cols = int(len(img[0])/2 - 1)
center = (rows, cols)

#Utilize OpenCV to create a '0' circle in open image, with a radius of 50.
cv2.circle(img, center, 50, 0, -1)

#My attempt at creating a method myself for a circle, but I could only figure out how to make a square. Sad times.
#for i in range(rows-50, rows+50):
#	for j in range(cols-50, cols+50):
#			img[i][j] = 0
#Show image, and wait for user interaction before closing

cv2.imshow('image', img)
cv2.imwrite('DiscJML.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()