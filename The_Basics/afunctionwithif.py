#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:08:02 2020

@author: jovillal
"""

def tempgauge(T):
    if isinstance(T,(int,float)):
        if T > 25:
            return('Hot')
        elif T < 15:
            return('Cold')
        else:
            return('Warm')
    else:
        print(T, 'Not a number')
        
#Ternary operator
is_friend = True


result = "Is my friend!" if is_friend else "Not the man"

print(result)
is_friend = False

result = "Is my friend!" if is_friend else "Not the man"
print(result)