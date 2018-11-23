#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:36:14 2018

about images and arrays, around page 24

@author: jovillal
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy

img = mpimg.imread('/home/jovillal/git/Learning-Python/LearningScipy/lena.jpg')
imgplot = plt.imshow(img) 

plt.gray() #does not work
plt.imshow(img)
plt.show()

img.dtype, img.shape, img.size

A = numpy.array([11,13,15,17,19,18,16,14,12,10])
A.argsort(kind='mergesort') #this gives the aguments of the array, where it to be sorted
A.sort() #sorts the array overwriting the original
B =numpy.array([[1,1,1],[2,2,2],[3,3,3]])
B.mean()
B.mean(axis=0) #mean through colums
B.mean(axis=1) #mean through rows