#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:11:47 2020

@author: jovillal

Error handling with except 
"""

#Use try and except to catch run time errors (exceptions)

while True:
    try:
        age = int(input('Enter age:'))
        10/age
    except ValueError: 
        print('Enter a number.')
    except ZeroDivisionError: 
        print('Age must be greater than 0.')
    #The else statement happens if no error is detected
    else:
        print('All good')
        break
    #finally does something after checking everything, even after break statements
    finally:
        print("I'm done")
        
#errors can be auto-produced using raise Exception('error text')

    
