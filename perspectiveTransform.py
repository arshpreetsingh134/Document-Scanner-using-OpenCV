# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2

#  This function takes a single argument, pts , which is a list of four points 
#  specifying the (x, y) coordinates of each point of the rectangle.

def order_points(pts):
    rect = np.zeros((4,2), dtype= "float32")
    
    # We will specify our points in top-left, top-right, bottom-right, bottom-left 
    # order in the numpy array. This ordering will be consistent throughout our
    # implementation.
    
    s = pts.sum(axis=1)
    
    rect[0]= pts[np.argmin(s)]
    rect[2]= pts[np.argmax(s)]
    
    diff= np.diff(pts, axis=1)
    
    rect[1]= pts[np.argmin(diff)]
    rect[3]= pts[np.argmax(diff)]
    
    # Return the ordered coordinates.
    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    
    # Calculating the width of new image.
    
    widthA = np.sqrt(((tl[0] - tr[0]) ** 2) + ((tl[1] - tr[1]) ** 2))
    widthB = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    width = max(int(widthA), int(widthB))
    
    # Calculating the height of new image.
    
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    height = max(int(heightA), int(heightB))
    
    # Constructing a set of destination points to obtain a "Bird's-eye view",
    # i.e., top-down view.
    
    dp = np.array([[0,0], [width-1, 0], [width-1, height-1], [0, height-1]], dtype="float32")
    
    transform_matrix = cv2.getPerspectiveTransform(rect, dp)
    warped = cv2.warpPerspective(image, transform_matrix, (width, height))
    
    return warped