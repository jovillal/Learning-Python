#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:54:59 2020

@author: jovillal

This loads a json file as a dictionary and asks for a word, it returns the definition of the word
"""

import json
from difflib import get_close_matches

def print_matches(word):
    defs = dic_data[word]
    print(word+"\n")
    for i in range(len(defs)):
        print("\t"+defs[i] + '\n')

dic_data = json.load(open("data.json")) 
    
look_for = input("Word to look up:")

if look_for in dic_data.keys():
    print_matches(look_for)
else:
    close_matches = get_close_matches(look_for, dic_data.keys())
    if len(close_matches) > 0:
        for i in range(len(close_matches)):
            if input("Word " + look_for + " not found, did you mean " + close_matches[i] + "? (y/n): ") == "y":
                print_matches(close_matches[i])
                break
            else:
                continue    
    else:
        print("Word not in dictionary.")
    
print("Bye!")
        
