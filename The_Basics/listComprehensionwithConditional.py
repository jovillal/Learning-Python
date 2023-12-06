#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:52:44 2020

@author: jovillal
Comprehensions are a way to generate iterables through other iterables
lists and sets follow the same logic and syntaxis
dictionaries follow something like
    
    {k:transformation(v) for k,v in dictionary.items() if contdition(k,v) }

A function that takes a list and returns only the numbers
Another function that only returns positives
Another that replaces strings for 0
A fourth one that takes a list of numbers as strings and returns their sum
"""
def only_numbers(input):
    return [var for var in input if isinstance(var, (int, float))]

def only_positives(input):
    return [var for var in input if var >= 0]

def strings_to_0(input):
    return [var if isinstance(var, (int, float)) else 0 for var in input]

def sum_strings(input):
    numbers = [float(x) for x in input]
    sum = 0
    for x in numbers:
        sum += x
        
    return sum



print("Given [99, \'whatever\', 9.5, 0.94, \'a string\'] as input")
print("only_number outputs: ", only_numbers([99, 'whatever', 9.5, 0.94, "a string"]))

print("strings_to_0 outputs: ", strings_to_0([99, 'whatever', 9.5, 0.94, "a string"]))

print("Given [99, 0, -9.5, 0.94] as input")
print("only_positives outputs: ", only_positives([99, 0, -9.5, 0.94]))

print("Given [\'99\', \'0\', \'-9.5\', \'0.94\'] as input")
print("sum_strings outputs: ", sum_strings(['99', '0', '-9.5', '0.94']))

#list splicing returns a copy of the list (while methods modify the list)
tst = list(range(10))
tst[::-1]
print(tst)
tst.reverse()
print(tst)

#list unpacking is a way to get some elements, not sure if it is useful.

a, b, c, *other, d = tst
print(a)
print(b)
print(c)
print(other)
print(d)