#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import numpy as np
import cv2
from image import Image
from math import sqrt

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
    def color_extraction(color, image):
        color= [0,0,0]
        print color
        _row = image.image.shape[0]
        _column = image.image.shape[1]
        print _row
        print _column
        b,g,r = cv2.split(image.image)
        print image.image[1][1]

        for x in xrange(1,_row):
            for y in xrange(1,_column):
                _distance = sqrt((pow((b[x][y] - color[1]),2))+(pow((g[x][y] - color[0]),2))+(pow((r[x][y] - color[2]),2)))
                if (_distance < 100):
                    image.image[x][y] = 255 
        
        cv2.imshow("Image2", image.image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

    @staticmethod
    def rbg_to_cinza(image):
	gray_image = cv2.cvtColor( image.image, cv2.COLOR_BGR2GRAY);
	image.image = gray_image
	return image

    @staticmethod
    def crop(image, xi, xf, yi, yf):
        image_crop = image.image[xi:xf, yi:yf]
        return image_crop
    
    @staticmethod
    def binarization(image, value):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret,binary_image = cv2.threshold(gray_image, value,255,cv2.THRESH_BINARY)
        return binary_image

    '''@staticmethod
    def resize(image):
        r = 100.0 / image.image.shape[1]
        dim = (500, int(image.image.shape[0] * r * 3 ))
        resized_image = cv2.resize(image.image, dim, interpolation = cv2.INTER_NEAREST )
        return resized_image'''

    @staticmethod
    def low_pass( image ):
        blur = cv2.blur( image.image, (3,3))
        return blur
    
    '''@staticmethod
    def generate_histogram(image):
        hist = cv2.calcHist([image],[0],None,[256],[0,256])
        plt.subplot(221)
        plt.plot(hist)
        plt.show()'''

    
