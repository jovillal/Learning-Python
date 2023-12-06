#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:11:02 2023

Decorators

Functions are like variables, they can be passed as arguments or returned
A Higher Order Function (HOF) can be either
    - a function that receives a function as an argument
    - a function that returns a function 
    
The example below is basically saying that 
    hello() -> my_decorator(hello)()
    bye() -> my_decorator(bye)()
    
@author: jovillal
"""

#this defines a decorator
def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func

#these are fnctions that use the decorator
@my_decorator
def hello():
    print('Hello')
    
@my_decorator
def bye():
    print('See you')
    
hello()
bye()

#with arguments
def another_decorator(func):
    def wrap_func(x):
        print('+++++++++++')
        func(x)
        print('**********')
    return wrap_func

@another_decorator
def greeting(x):
    print(x)
    
greeting('hurry')

#with general arguments
def general_decorator(func):
    def wrap_func(*args, **kwargs):
        print('+++++++++++')
        func(*args, **kwargs)
        print('-----------')
    return wrap_func

@general_decorator
def greet(x,emoji = ':('):
    print(x+emoji)
    
greet('hurry')

#this tests how efficient another function is
from time import time
def performance(f):
    def wrap_func(*args, **kwargs):
        t0 = time()
        result = f(*args, **kwargs)
        t1 = time()
        print(f'Function took {t1-t0} s')
        return result
    return wrap_func

@performance
def long_time():
    for i in range(10000000):
        i*5

long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  def wrap(*args, **kwargs):
      if args[0]['valid']:
          return fn(*args, **kwargs)
  return wrap

# def authenticated(fn):
#   def wrapper(*args, **kwargs):
#     if args[0]['valid']:
#         return fn(*args, **kwargs)
#   return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)








