#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 12:12:17 2023

set is another data type
A set is an unordered collection of unique items between {}
They aren't subsciptable (can't do set[1])

@author: jovillal
"""
my_set = {1,2,3,4,5}
bad_set = {1,1}
print(type(my_set))
print(bad_set)     #only one element
my_set.add(100)
my_set.add(2)
print(my_set)    #2 wasn't added

#sets can be used to remove duplicates from other collections
my_list = [1,1,1,1,2,11,1,1,2,5]
print(set(my_list))
my_set[1]