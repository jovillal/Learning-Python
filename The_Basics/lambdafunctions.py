#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:25:15 2023

lambda expressions are like pure functions in Wolfram Language

lambda param1, param2, ...: transformation(param1, param2, ...)

@author: jovillal
"""

#Squares
my_list = [5,4,3]

print(list(map(lambda x: x**2, my_list)))

#List sorting a list of tuples based on the second value

a = [(0,2),(4,3),(9,9),(10,-1)] 
a.sort(key=lambda x:x[1])
print(a)


