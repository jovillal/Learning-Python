#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 12:58:13 2021

@author: jovillal

    A program that gets a numerical input, interprets it as kilograms and returns 
its value converted to grams, pounds and ounces.
"""

from tkinter import * #this bypasses the need to reference objects to tkinter (use Button instead of tkinter.Button)

def kg_to_var():
    lb = float(e1_value.get()) * 2.2
    g = 1000 * float(e1_value.get())
    ou = float(e1_value.get()) * 35.27
    tOutGr.delete("1.0", END) #deletes tect in the box
    tOutGr.insert(END, g) #this puts 'g' at the end of the tOutGr text box
    tOutLb.delete("1.0", END)
    tOutLb.insert(END, lb)
    tOutOu.delete("1.0", END)
    tOutOu.insert(END, ou)
    

#create a window
window = Tk()

b1 = Button(window,text="Convert",command=kg_to_var) 
        #a button widget in the window labeled "Convert"
        #the command options tells the button what to call when pressed

b1.grid(row=0,column=2) #this puts the button on the window, it is supposed to give more control than pack, 
                        #can add rowspan=n to indicate that the widget goes over multiple rows (like a merge)

e1_value=StringVar() #a string stream object
e1 = Entry(window, textvariable = e1_value) 
        #a entry widget in the window (captures input?)
        # the textvariable options tells where to store the value that is inputed
e1.grid(row=0,column=1)

t1 = Text(window, height=3, width=20) #a text widget in the window, displays text, size is specified
t1.grid(row=0,column=0)
t1.insert(END,"Enter kilograms")

tDescGr = Text(window, height=1, width=20) #a text widget in the window, displays text, size is specified
tDescGr.grid(row=1,column=0)
tDescGr.insert(END,"Grams")

tDescLb = Text(window, height=1, width=20) #a text widget in the window, displays text, size is specified
tDescLb.grid(row=1,column=1)
tDescLb.insert(END,"Pounds")

tDescOu = Text(window, height=1, width=20) #a text widget in the window, displays text, size is specified
tDescOu.grid(row=1,column=2)
tDescOu.insert(END,"Ounces")

tOutGr = Text(window, height=1, width=20) #a text widget in the window, displays text, size is specified
tOutGr .grid(row=2,column=0)

tOutLb = Text(window, height=1, width=20) #a text widget in the window, displays text, size is specified
tOutLb .grid(row=2,column=1)

tOutOu = Text(window, height=1, width=20) #a text widget in the window, displays text, size is specified
tOutOu .grid(row=2,column=2)


window.mainloop() #this keeps the window open, all widgets must be created between the creation and this.

