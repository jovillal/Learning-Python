#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 08:58:41 2023

@author: jovillal
"""
print("Hello World")

#here is how to define a class
class Person:
    def __init__(self, nm, ag):
        self.name = nm
        self.age = ag
    
    def getName(self):
        print("Your name is " + self.name)
        
    def getAge(self):
        print("Your age is " + str(self.age))
        
p1 = Person("Jorge", 47)
p1.getName()
p1.getAge()

