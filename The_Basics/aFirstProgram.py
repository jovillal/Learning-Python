#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:05:05 2020

@author: jovillal

A script that ask for phrases until the user types '\end'.
Returns all phrases capitalized and if it is a question it will place a '?' at the end.
"""
def toPrint(txt):
    tmp = txt.capitalize()
 #   first = tmp.split()[0]
 #   if first == "Where" or first == "How" or first == "Who" or first == "Whom" or first == "Why":
    if tmp.startswith(("Where", "How", "Who", "Whom", "Why")):
        return tmp + '? '
    else:
        return tmp + '. '

phrases = []
to_print = ''


print("Write phrases, write \'\end\' to exit")
while True:
     next_phrase = input('Say something: ')
     if next_phrase == '\end':
        for txt in phrases:
            to_print = to_print + toPrint(txt)
            
        print(to_print)
        break
    
     else:
         phrases.append(next_phrase)
         continue