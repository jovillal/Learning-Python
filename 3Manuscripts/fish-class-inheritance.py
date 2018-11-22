#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:48:12 2018

about base (parent) classes and childs, things to do with inheritance

@author: jovillal
"""

class Fish:
    def __init__(self,first_name,last_name = 'Fish', 
                 skeleton = 'Bone', eyelids = False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
        
    def swim(self):
        print('The fish is swimming')
        
    def swim_backwards(self):
        print('The fish can swim backwards')
    
class SeaHorse(Fish):  #a child of Fish (it is ¿declared? in the argument) 
   pass #inherits everithing defined in class Fish

class Trout(Fish):  #a child of Fish (it is ¿declared? in the argument) 
   def __init__(self, water = 'Freshwater'): #includes a new paramether into init, needs the super to work out well
       self.water = water
       super().__init__(self) #Warning, first name now must be initialized differently

   
class Clownfish(Fish):  #This inherits all Fish methods, so pass is apparenty not necesary
    def live_with_anemone(self):
        print("Fish coexisting with a sea anemone")
        
class Shark(Fish): #This inherits all Fish methods, but we will override them
    def __init__(self, first_name, last_name = 'F-ing Shark', 
                 skeleton = 'cartilage', eyelids = True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
        
    def swim_backwards(self):
        print("The shark can't swim backwards, but it can sink backwards.")

eclipse = SeaHorse("Eclipse d'")
print("Our new sea horse is named " + eclipse.first_name + " " + eclipse.last_name + 
      "!")
print(eclipse.skeleton)
print(eclipse.eyelids)
eclipse.swim()
eclipse.swim_backwards()
print()
   
terry = Trout()
terry.first_name = "Terry d'"
print("Our new trout is named " + terry.first_name + " " + terry.last_name + 
      "!")
print(terry.skeleton)
print(terry.eyelids)
print(terry.water)
terry.swim()
terry.swim_backwards()
print()

casey = Clownfish("Casey d'", "Clown")
print("Our new clown is named " + casey.first_name + " " + casey.last_name + 
      "!")
print(casey.skeleton)
print(casey.eyelids)
casey.swim()
casey.swim_backwards()
casey.live_with_anemone()
#terry.live_with_anemone()  #This would not work
print()

robert = Shark("Robert")
print("The shark is named " + robert.first_name + " " + robert.last_name + 
      "!")
print(robert.skeleton)
print(robert.eyelids)
robert.swim()
robert.swim_backwards()
print()












