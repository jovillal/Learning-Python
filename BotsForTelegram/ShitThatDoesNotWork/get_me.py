#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 016:50:42 2023

A bot using the api

@author: jovillal
"""
from telegram import Bot

# initializing the bot with API
bot = Bot("6365315898:AAHkH7qUed2dMVQ-Mj9JSyEwYlLIgoZzIzg")

# getting the bot details
print(bot.get_me())
