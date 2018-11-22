#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:10:59 2018

An attempt at classes

@author: jovillal
"""

class MyClass:
    """An early attempt at a class"""
    
    a=10
    def func(self):
        print("hello")
        
print(MyClass.a) #Should print 10
print(MyClass.func) #this is busted... how can one implement methods?
print(MyClass.__doc__) #should print the docstring

ob=MyClass() #this defines an object of type MyClass
ob.func() #this works
print(ob.a) #also works

class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.real = r
        self.imag = i
        
    def getData(self):
        print('{0}+{1}i'.format(self.real,self.imag))
        
c1 = ComplexNumber(5,2)
c1.getData() #should print 5+2i
c2 = ComplexNumber(3)
c2.attr=10 #why is this even allowed?
print((c2.real,c2.imag,c2.attr))
c1.attr #c1 has no attr attached