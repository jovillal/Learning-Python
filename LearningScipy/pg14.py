#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 14:19:05 2018

@author: jovillal
"""

import numpy
import scipy
from scipy import stats
import matplotlib.pyplot as plt

##statistic example
scores = numpy.array([114, 100, 104, 89, 102, 91, 114, 114, 103, 105, 108, 130,
                      120, 132, 111, 128, 118, 119, 86, 72, 111, 103, 74, 112,
                      107, 103, 98, 96, 112, 112, 93])
xmean = scipy.mean(scores)
sigma = scipy.std(scores)
n = scipy.size(scores)
xmean, xmean - 2.576 * sigma/scipy.sqrt(n), xmean + 2.576 * sigma/scipy.sqrt(n)
results = scipy.stats.bayes_mvs(scores)
results[0]

##a plot
x = numpy.linspace(0, 2*numpy.pi, 32)
fig = plt.figure()
plt.plot(x, numpy.sin(x))
plt.show()
#this doesn't work
fig.savefig('sine.png')
