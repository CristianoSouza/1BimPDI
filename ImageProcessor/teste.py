#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from api_pdi_opencv_python import ImageProcessor

image = ImageProcessor()
object_image = image.read_image("../tucanu.jpg")
image.show_image(object_image)
object_image = image.rbg_to_cinza(object_image)
image.show_image(object_image)
image.save_image("tucanu_gray.jpg", object_image)

