#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from api_pdi_opencv_python import ImageProcessor
import numpy as np
import cv2
from image import Image
from math import sqrt

image_processor = ImageProcessor()
object_image = image_processor.read_image("blur.jpg")
#image_processor.show_image(object_image)
#object_image = image_processor.rbg_to_cinza(object_image)
#image_processor.show_image(object_image)
#image_processor.save_image("tucanu_gray.jpg", object_image)
#image.generate_histogram(object_image)
#aa = image_processor.color_extraction("blue", object_image)
#image = image_processor.crop(object_image, 100, 400, 100, 600)
##aa = image_processor.binarization(image, 120)
#aa = image_processor.resize(object_image)
aa = image_processor.low_pass(object_image)
cv2.imshow("Imageasd2", aa )
cv2.waitKey(0)
cv2.destroyAllWindows()
