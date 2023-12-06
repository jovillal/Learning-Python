#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:46:32 2023

Generators are things that spit out stuff one by one (or by a pre-defined step)
A generator does not accupy memory as a data structure
A generator is iterable

Generators use 'yield' to sort of return the next value, yield pauses execution.

@author: jovillal
"""

#range is a generator

#this is a generator
def generator_function(num):
    for i in range(num):
        yield i
        
for item in generator_function(10):
    print(item)
    
#g is a generator object
g = generator_function(10)
print(g)    #this gives the memory address
next(g)     #this advances the generator
next(g)
next(g)
print(next(g))
print(next(g))

print('++++++')

#this takes an iterable and multiplies every item by 5
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator)*5)
        except StopIteration:
            break
        
special_for([1,2,3])

print('++++++')

#this is the way range works
class my_Gen():

    def __init__(self,first,last):
        self.first = first
        self.last = last
        
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.first < self.last:
            num = self.first
            self.first+=1
            return num
        raise StopIteration
    
gen = my_Gen(0,10)

for i in gen:
    print(i)
    
#Fibonacci implementation

print('++++++')
print('Fibo using recursion:')
def Fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fibo(num-1)+Fibo(num-2)

print(Fibo(20))

print('++++++')
print('Fibo using generators:')
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        tmp = a
        a = b
        b = tmp + b

for n in fib(21):
    print(n)