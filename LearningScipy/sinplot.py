#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 09:55:28 2018

A x Vs sin(x) plot

@author: jovillal
"""

import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(0, 2*numpy.pi, 32)
fig = plt.figure()
plt.plot(x,numpy.sin(x)) 
plt.show()
fig.savefig('sine.png')