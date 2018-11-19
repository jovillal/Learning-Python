#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:02:14 2018

@author: jovillal
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure() #empty figure
fig.suptitle('No axes on this figure') #Add a title
#fig, ax_lst = plt.subplots(2,2) #This adds four subplots, I don't get it

x = np.linspace(0,2,100) #This is like Table[i,{i,0,2,2/100}]
plt.plot(x, x, label="Linear") #plots x vs x
plt.plot(x, x**2, label='quadratic') #plots x vs x^2
plt.plot(x, x**3, label='quadratic') #plots x vs x^3
plt.xlabel('x label') #puts the horizontal label
plt.ylabel('y label') #puts the verticallabel
plt.title("Simple Plot") #puts the title
plt.legend() #puts the legend?
plt.show() #Supposed to show the plot, it doesn't in spyder, it does on the console.... fuck. Also, in the console it draws on the lower right subplot... 
 