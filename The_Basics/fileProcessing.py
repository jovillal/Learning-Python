#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:41:08 2020

@author: jovillal

About file processing
"""

#opening and closing

with open("bear.txt", "w") as to_write:
    to_write.write("The American black bear (Ursus americanus) is a medium-sized bear native to North America. It is the continent's smallest and most widely distributed bear species. American black bears are omnivores, with their diets varying greatly depending on season and location. They typically live in largely forested areas, but do leave forests in search of food. Sometimes they become attracted to human communities because of the immediate availability of food. The American black bear is the world's most common bear species.")

print("File written")

with open("bear.txt") as a_fyle:
    theBear = a_fyle.read()
    
print("File placed on a variable") 

print(theBear[:90]) 

#a function that gets a filepath and a character and return the number of ocurrences
def count_char(path, char):
    with open(path) as a_fyle:
        string = a_fyle.read()
    
    return string.count(char)

print("For the bear.txt file, the letter \'a\' occurs", count_char("bear.txt",'a'), "times")

filename = 'new.csv'
try:
    with open(filename, 'a') as f:
        f.write("whateverx2")
        print("Text appended to file " + filename + " successfully.")
except IOError:
    print("Error: could not append to file " + filename)
    
with open('a'+filename, 'r') as f:
        f.write("whateverx2")
    