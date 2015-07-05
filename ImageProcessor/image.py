#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

class Image:

    def __init__(self, image, url, height, width ):
        self._width = width
        self._height = height
        self._url = url
        self._image = image

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def width(self):
        return self._width

    @width.setter
    def set_width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def set_height(self, height):
        self._height = height

