#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 10:41:27 2023

Feom https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot



@author: jovillal
"""
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# check https://github.com/python-telegram-bot/python-telegram-bot/wiki/Exceptions%2C-Warnings-and-Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

if __name__ == '__main__':
    #first important step, see https://github.com/python-telegram-bot/python-telegram-bot/wiki/Builder-Pattern
    application = ApplicationBuilder().token('6365315898:AAHkH7qUed2dMVQ-Mj9JSyEwYlLIgoZzIzg').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()