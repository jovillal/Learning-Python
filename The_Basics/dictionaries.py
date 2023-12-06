#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:30:45 2023

Dictionaries are made of key:value pairs, it is unordered (can't be indexed)

keys reference the value and must be inmutable (numbers, strings, tuples)

@author: jovillal
"""

dictionary = {'a':1,'b':2}

print(dictionary['a'])

#the get method returns None if there is no key, it can be given a default value to return if there is None

print(dictionary.get('a'))
print(dictionary.get('c'))
print(dictionary.get('c',55))

dictionary = {'a':1,'b':2, 'c':3}
print(dictionary.get('c',55))

#check if a key exists
print('b' in dictionary)
print('s' in dictionary)
print(3 in dictionary)
#.keys(), .values() and .items() return the corresponding objects, items returns tuples
print(3 in dictionary.values())
print(dictionary.items())

#to insert a new key:value pair (or change an existing one) use .update({key:value})
dictionary.update({'d':4})
dictionary.update({'c':-4})
print(dictionary)
