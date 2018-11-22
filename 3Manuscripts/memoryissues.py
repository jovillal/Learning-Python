#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:42:35 2018

3 manuscripts from page 140

@author: jovillal
"""
from copy import deepcopy

colours1=["red","green"] #this works as expected
colours2=colours1
colours2 =["yellow","magenta"]
colours1 #this is still the original, so python made a real copy

colours2=colours1
colours2[1]="blip"
colours1 #now colours1[1] has been also modified @.o

list1 = ["a", "b", ["ab", "ba"]] #shit is even weirder when using sublists
list2 = deepcopy(list1) #use deepcopy (from copy) to avoid modifying originals
