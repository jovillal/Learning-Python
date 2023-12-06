#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 08:57:09 2023

A counter

@author: jovillal
"""
from collections import Counter

li = [1,2,3,4,5,6,7,7]
sent = "blah, blah, blah, thinking about stuff"
print(Counter(li))
print(Counter(sent))