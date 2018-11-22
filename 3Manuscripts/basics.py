#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:31:54 2018

@author: jovillal 
From the 3 manuscripts in one book, around page 60 about strings, tuples, lists, loops and dictionaries
"""

#about strings

s='hi' #a string (either between "" or '')
s[1] #this is 'i'
len(s) #gives 2
s+ ' a string' #concatenates strings (no automatic conversion)
pi=3.14
s+pi #doesn't work
s+" " + str(pi) #works (force conversion)

s = "  This is a weird string,.  "
s.lower() #no caps
s.upper() #all caps
s.strip() #removes ' ' from beggining and end
s.isalpha() #True if s is composed exclusively of alphabetic chars (no '.', etc)
s.isdigit() #True if s is composed exclusively of digits (numbers, no "." etc)
s.find("t") #Returns the first index where "t" is found
s.replace(" ","1") #replaces all occurrences of " " with "1"
s.split("n") #returns a list of substring from s, splitted at the occurences of "n"
s.join(list) #joins the elements in list using s as the middle man

#lists, lists are enclosed inside square brackets, apparently one can have nested lists
colors=['blue',3,'red',1,'green',2]
len(colors) #number of elements
colors+colors #concatenates strings (no automatic conversion)

#tuples are like lists without delimiters ---( and ) may be used--- and are inmutable, a one element tuple can be written as 'a',
t='a','b','c','d'
('A',)+t #does not modify, it creates

#dictionaries are pairs of values (key:value) enclosed between {}
eng2esp={}
eng2esp["three"]="tres"
eng2esp["two"]="dos"
eng2esp["one"]="uno"
del eng2esp['one'] #deletes a key:value pair
eng2esp['two']=2 #changes de value
eng2esp['four'] #returns an error
eng2esp.get('four', 0) #returs 0 if 'four' is not a key
sorted(eng2esp) #returns keys, sorted
























