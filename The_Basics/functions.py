#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:52:44 2020

@author: jovillal

Function exercises

"""
#A function that takes a list and returns only the numbers
def only_numbers(input):
    return [var for var in input if isinstance(var, (int, float))]

#Another function that only returns positives
def only_positives(input):
    return [var for var in input if var >= 0]

#Another that replaces strings for 0
def strings_to_0(input):
    return [var if isinstance(var, (int, float)) else 0 for var in input]


#A fourth one that takes a list of numbers as strings and returns their sum
def sum_strings(input):
    numbers = [float(x) for x in input]
    sum = 0
    for x in numbers:
        sum += x
        
    return sum

#This ones takes two strings and concatenates them
def addStrings(s1, s2):
    return s1 + s2

#*args passes whatever is given a a tuple
def testargs(*args):
    print(args)
    
testargs(1,2,3)

#**kwargs passes whatever is given a a dictionary

def testkwargs(**kwargs):
    print(kwargs)
    
testkwargs(one=1,two=2,three=3)


#Calculate the mean of an indeterminate number of elements
def mean(*args):
    return(sum(args)/len(args))

#This takes an indeterminate number of strings and returs a sorted list of said strings in uppercase    
def capAndSort(*args):
    return sorted([st.upper() for st in args])


print("Given [99, \'whatever\', 9.5, 0.94, \'a string\'] as input")
print("only_number outputs: ", only_numbers([99, 'whatever', 9.5, 0.94, "a string"]))

print("strings_to_0 outputs: ", strings_to_0([99, 'whatever', 9.5, 0.94, "a string"]))

print("Given [99, 0, -9.5, 0.94] as input")
print("only_positives outputs: ", only_positives([99, 0, -9.5, 0.94]))

print("Given [\'99\', \'0\', \'-9.5\', \'0.94\'] as input")
print("sum_strings outputs: ", sum_strings(['99', '0', '-9.5', '0.94']))

print("Given \'hello\' and \'world\' as input")
print("addString outputs: ", addStrings("hello", "world"))

print("Given 10, 20, 30, and 40 as input")
print("mean outputs: ", mean(10, 20, 30, 40))

print("Given \'Bogota\', \'Cundinamarca\', and \'Medellin\' as input")
print("capAndSort outputs: ", capAndSort('Bogota', 'Cundinamarca', 'and', 'Medellin'))


