# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:34:19 2020

@author: ARSHPREET SINGH
"""

# python scan_doc.py --image test_image.jpg

from perspectiveTransform import four_point_transform
from skimage.filters import threshold_local
import cv2
import argparse
import imutils
import numpy as np

ap= argparse.ArgumentParser()

ap.add_argument("-i", "--image", help= "specify the path of image to be scanned")
args= vars(ap.parse_args())

image= cv2.imread(args["image"])

# First, we will retain the original image.
orig = image.copy()

# Resizing the image whose contours are to be calculated.
ratio = image.shape[0]/ 500.0
image = imutils.resize(image, height=500)



### ------------- STEP 1: Edge Detection ------------- ###

# Converting the image to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying Gaussian Blur to reduce high-freq noise.
gray = cv2.GaussianBlur(gray, (5,5), 0)

# Detecting edges of the document using Canny Algorithm.
edges = cv2.Canny(gray, 75, 200)

cv2.imshow("Original", image)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()



### ------------- STEP 2: Plotting Contours ------------- ###

# Finding and grabbing contours from the edged image
cnts = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Sorting the contours by area and keeping only the largest ones 
cnts = sorted(cnts, key= cv2.contourArea, reverse= True)[:5]

for c in cnts:
    # Approximating the no. of points in each contour
    arcs = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02*arcs, True)
    
    # If our contour has 4 points, it means we have found our document
    # in the image
    if len(approx) == 4:
        screenCount = approx
        break
    
cv2.drawContours(image, [screenCount], -1, (255, 0, 0), 2)     
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



### ------------- STEP 3: Applying a Bird's eye view and Threshold ------------- ###

# Here, we will use our four_point_transform function to apply  Perspective 
# Transform (bird's eye view) on the original image, and we will use the contour 
# points calculated for resized image above

perspect = four_point_transform(orig, screenCount.reshape(4,2) * ratio)

# Converting to Grayscale
gray1 = cv2.cvtColor(perspect, cv2.COLOR_BGR2GRAY)

# Applying Threshold to give a 'Black & White' Paper Effect
T = threshold_local(gray1, 11, offset = 10, method = "gaussian")
warped = (gray1 > T).astype("uint8") * 255

# Show the Original vs Scanned Image
cv2.imshow("Original", imutils.resize(orig, height= 650))
cv2.imshow("Scanned Document", imutils.resize(warped, height= 650))
cv2.waitKey(0)