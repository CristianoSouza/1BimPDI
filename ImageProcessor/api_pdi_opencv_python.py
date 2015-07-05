#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import numpy as np
import cv2
from image import Image 

class ImageProcessor:

    @staticmethod
    def read_image(path):
        image_aux = cv2.imread(path,1)
	height = image_aux.shape[0]  
	width = image_aux.shape[1]        
	image = Image( image_aux, path, height, width)
        return image

    @staticmethod
    def save_image(path, image):
	try:
	    cv2.imwrite(path,image.image)
	except (RuntimeError, TypeError, NameError):
	    print "Oops!  That was no valid number.  Try again..."

    @staticmethod
    def show_image(image):
	cv2.imshow("Image", image.image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

    @staticmethod
    def rbg_to_cinza(image):
	gray_image = cv2.cvtColor( image.image, cv2.COLOR_BGR2GRAY);
	image.image = gray_image
	return image
