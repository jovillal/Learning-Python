#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:20:13 2021

@author: jovillal

How to use tkinter for GUI apps
This builds a window where one inputs miles and gets kilometers
"""
from tkinter import * #this bypasses the need to reference objects to tkinter (use button instead of tkinter.button)

def km_to_miles():
    #print(e1_value.get()) #the method gets a string from the stream e1_value
    miles = 1.6 * float(e1_value.get())
    t1.insert(END, miles) #this puts 'miles' at the end of the t1 text box

#create a window
window = Tk()

b1 = Button(window,text="Execute",command=km_to_miles) 
        #a button widget in the window labeled "Execute"
        #the command options tells the button what to call when pressed

#b1.pack() #this puts the button on the window
b1.grid(row=0,column=0) #this puts the button on the window, it is supposed to give more control than pack, 
                        #can add rowspan=n to indicate that the widget goes over multiple rows (like a merge)

e1_value=StringVar() #a string stream object
e1 = Entry(window, textvariable = e1_value) 
        #a entry widget in the window (captures input?)
        # the textvariable options tells where to store the value that is inputed
e1.grid(row=0,column=1)

t1= Text(window, height=1, width=20) #a text widget in the window, displays text, size is specified
t1.grid(row=0,column=2)

window.mainloop() #this keeps the window open, all widgets must be created between the creation and this.