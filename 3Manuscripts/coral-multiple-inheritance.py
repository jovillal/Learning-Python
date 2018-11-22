# -*- coding: utf-8 -*-
"""
Spyder Editor

Doing multiple inheritances

This is a temporary script file.
"""

class Coral:
    def community(self):
        print('Coral lives in a comunity')
        
class Anemone:
    def protect_clownfish(self):
        print('The anemone is protecting the clown.')
        
class CoralReef(Coral, Anemone): #This inherits all methods from the above classes
    pass

great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()
