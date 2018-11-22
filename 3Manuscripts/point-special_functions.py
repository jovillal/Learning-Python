#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:55:34 2018

Overloading operators. This is done via special functions (the ones that start with __)

@author: jovillal
"""

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    def __str__(self):  #this overloads the behavior of string related functions
        return "({0},{1})".format(self.x,self.y)
    
    def __add__(self, other): #this overloads addition
        return Point(self.x + other.x, self.y + other.y)
    
    def magnitude(self): #a proper method for the magnitude squared
        return self.x**2 + self.y**2
    
    def __lt__(self, other): #this overloads < (lt)
        return self.magnitude() < other.magnitude()

        
p1 = Point(-5,3.3)
print(p1)
str(p1)
format(p1)

p2=Point(2,-10)

print(p1+p2)

print(p1.magnitude())

print(Point(1,1)<Point(1,2))
print(Point(1,1)<Point(-2,-3))
print(Point(1,1)<Point(1,1))