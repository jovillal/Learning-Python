#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:00:40 2023

A simple guessing game
@author: jovillal
"""
import sys
from random import randint

if(len(sys.argv)==1):
    start = 0
    end = 9
elif(len(sys.argv)==2):
    start = int(sys.argv[1])
    end = start+9
elif(len(sys.argv)==3):
    start = int(sys.argv[1])
    end = int(sys.argv[2])
else:
    start = 0
    end = 9
    print("""Need 0, 1 or 2 parameters.
          0 is default.
          1 changes the lower bound (keesp upper at +9)
          2 changes both bounds
          Will play default""")
target = randint(start,end)      
guess=int(input(f'Write a number between {start} and {end} (inclusive):'))
while guess != target:
    print("Wrong. Guess Again.")
    guess=int(input(f'Write another number between {start} and {end} (inclusive):'))
print("Well done!\nBye")
    
    