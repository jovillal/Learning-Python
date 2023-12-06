#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:32:42 2020

@author: jovillal
"""

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    print(color)
    #print(isinstance(color, int))
    
print("--------------------")
    
for color in colors:
    if color > 50:
        print(color)
        
print("--------------------")
    
for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)
        
print("--------------------")

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, value in phone_numbers.items():
    print("%s1: %s2"% (key, value))
    
print("--------------------")
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for numbers in phone_numbers.values():
    print(numbers.replace('+','00',1))
        
        