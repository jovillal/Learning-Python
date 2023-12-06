#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:55:44 2023

A first attempt at a telegram bot

@author: jovillal
"""
"""
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
   app.run(threaded=True)

run this, then run on a terminal and get a https link for a webhook
       ngrok http 5000
      
Now set the webhook for the telegram bot, run this on a browser:
    https://api.telegram.org/bot<Your Bot Token>/setWebhook?url=<URL that you got from Ngrok>
After running the link in your web browser you will get the response:
    {"ok":true,"result":true,"description":"Webhook was set"}

￼

"""

from flask import Flask
from flask import request
from flask import Response
import requests
 
TOKEN = "6365315898:AAHkH7qUed2dMVQ-Mj9JSyEwYlLIgoZzIzg"
app = Flask(__name__)
 
def parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id,txt
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r
 
@app.route('/http://127.0.0.1:5000', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
       
        chat_id,txt = parse_message(msg)
        if txt == "hi":
            tel_send_message(chat_id,"Hello!!")
        else:
            tel_send_message(chat_id,'from webhook')
       
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
   app.run(debug=True)