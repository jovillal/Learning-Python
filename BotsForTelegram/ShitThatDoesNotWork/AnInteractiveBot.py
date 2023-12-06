#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:44:51 2023

A telegram bot that does ...?

@author: jovillal
"""
#Updater: This will contain the API to specify in which bot we are adding functionalities to using python code.
from telegram.ext import Updater 
#Update: This will invoke every time a bot receives an update i.e. message or command and will send the user a message.
from telegram.update import Update
#CallbackContext: not used directly in our code but when we will be adding the dispatcher it is required (and it will work internally)
from telegram.ext.callbackcontext import CallbackContext
#CommandHandler: This Handler class is used to handle any command sent by the user to the bot, a command always starts with “/” i.e “/start”,”/help” etc.
from telegram.ext.commandhandler import CommandHandler
#MessageHandler: This Handler class is used to handle any normal message sent by the user to the bot,
from telegram.ext.messagehandler import MessageHandler
#FIlters: This will filter normal text, commands, images, etc from a sent message.
from telegram.ext.filters import Filters

#
updater = Updater("6365315898:AAHkH7qUed2dMVQ-Mj9JSyEwYlLIgoZzIzg", use_context=True)

#Start function: It will display the first conversation, 
#the message inside it will be sent to the user whenever they press ‘start’ at the very beginning.
def start(update: Update, context: CallbackContext):
	update.message.reply_text("Hello, welcome!")

def help(update: Update, context: CallbackContext):
    commands='''Here are the available commands:
        \t/youtube gives a youtube url
        \t/linkedin gives my personal linkedin url
        \t/gmail gives the gmail url
        \t/geeks fools you.
    '''
    update.message.reply_text("Available commands\n"+commands)
    
#Functions that do some stuff
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("www.gmail.com")
  
  
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://youtu.be/4fezP875xOQ")
  
  
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://www.linkedin.com/in/jorge-villalobos-6104776/")
  
  
def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text("GeeksforGeeks url here")
  
#unknown_text sends the message written inside it whenever it gets some unknown messages
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
#unknown function Filters out all unknown commands sent by the user and reply to the message written inside it.
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
    
#Handlers to handle our messages and commands
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	# Filters out unknown commands
	Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

#start polling the bot will be active and it will look for any new message sent by any of the users and if it matches the command specified there it will reply accordingly.
updater.start_polling()



