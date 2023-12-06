#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 17:10:46 2023

Important functional programing functions:
    map
    filter
    zip
    reduce

@author: jovillal
"""

#map returns a map object
def times2(num):
    return 2*num

m=map(times2, [1,2,3])
print(m)
print(list(m))

#filter checks for boolean values
def is_odd(num):
    return num % 2 != 0

f=filter(is_odd,range(10))
print(f)
print(list(f))

#zip returns an object of made of tuples that gathers the first element of every iterable, then the second, etc
z = zip([1,2,3],[10,20,30],[100,200,300])
print(z)
print(list(z))

#reduce is like a nest, it needs a function that takes two parameters and operates over them, then it needs an iterable and finally a starting value
from functools import reduce

l=[10,20,30,40]

def accumulator(i0,i1):
    return i0*i1

print(reduce(accumulator,l,1))

#Exercices
print('++++Exercices++++')
#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def caps(st):
    return st.capitalize()
print(list(map(caps,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()

print(list(zip(my_strings,my_numbers)))

#3 Filter the scores that pass over 50
scores = [73, 20, 65, 19, 76, 100, 88]
def above50(num):
    return num > 50

print(list(filter(above50,scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
from functools import reduce

my_numbers.extend(scores)
print(my_numbers)

def accumulator(i0,i1):
    return i0+i1

print(reduce(accumulator,my_numbers,0))
print(reduce(accumulator,my_numbers,0)==sum(my_numbers))