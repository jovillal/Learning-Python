#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 18:58:21 2023

A GUI simulation

@author: jovillal
"""
picture = [
    [1,0,0,0,0,1,1],
    [0,1,1,1,0,1,1],
    [1,0,1,0,0,0,0],
    [1,1,0,1,0,1,0],
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0],
    [1,0,1,1,0,1,1]    
    ]

for row in picture:
    line = ''
    for col in row:
        if col == 0:
            line = line + ' '
        else:
            line = line + '*'
    print(line)
    
for row in picture:
    print('\n')
    for col in row:
        if col == 0:
            print(' ', end = '')
        else:
            print('*', end = '')