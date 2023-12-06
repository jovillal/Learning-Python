#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:15:01 2023

Requests

@author: jovillal
"""

import requests

r = requests.get('https://api.github.com/users/jovillal')

# check status code for response received
# success code - 200
print(r)
  
# print content of request
#print(r.content)


# Making a get request
response = requests.get('https://api.github.com/')

# print request object
print(response.url)

# print status code
print(response.status_code)

