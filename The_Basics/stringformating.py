#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:00:24 2020

@author: jovillal

Basic string formating, greet("Pepe") would return "Hi Pepe"
"""


def greet(name):
    return "Hi %s" % name.capitalize()

#The following exemplifies how to format with multiple variables
name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))