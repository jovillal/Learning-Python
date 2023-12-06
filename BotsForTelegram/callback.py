#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""Simple inline keyboard bot with multiple CallbackQueryHandlers.

This Bot uses the Application class to handle the bot.
First, a few callback functions are defined as callback query handler. Then, those functions are
passed to the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot that uses inline keyboard that has multiple CallbackQueryHandlers arranged in a
ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line to stop the bot.
"""
import logging
import datetime
import pytz
from random import uniform

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
     __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,    
    filters,
    )

QUOTEALIVE = datetime.timedelta(minutes=2) 	#the time for the quotations to stay valid
DEFAULTAMOUNT = 10000  						#A default transaction amount
quote_ID = 0

class TextMessages:
    hello = "Hello Bitso!\nThis is KraviBot chat, (Kravata’s virtual assistant)."
    outside_hours = "We are outside office hours."
    holiday = "Today is a holiday in Colombia."
    #TODO: poder cambiar las horas de funcionamiento
    hours = "Remember, we are here to help during our business hours (*Colombia Time*): *Monday through Friday from 8:15 to 13:45*."
    help = "I can help you with the following actions related to your account:"
    choose = 'Please choose one of the following:'
    thanks = "Thank you for using Kravibot: web3 made simple for everyone."
    bye = "Have an excellent day!"

class Memory:
    """Memory is a dictionary with the following structure:
	{
		chat_id (id from telegram):{
			name (the name from telegram): string,
            active_quote (the active quote, same as display_ID): int, 
            quotes: {
				 display_ID (an identifier to be displayed): int,{
                	ramp_ID: (the associated ramp number): str
                	operation (on or off ramp): string,
                	date_start (the time it was created): dateString,
                	date_end (date_start + QUOTEALIVE): dateString,
                	token (USDT or USDC): string,
                	reference (COP): string,
                	rate (the simulated value): float,
                    amount (the order amount): int
                }
			}
			
		}
	}"""
    chats = {}
        
order_keyboard = [
	[
	InlineKeyboardButton("Accept the quote", callback_data='A'),
	InlineKeyboardButton("Refresh", callback_data='B'),
    ],
    [
	InlineKeyboardButton("New USDT Off Ramp quote", callback_data='C'),
	InlineKeyboardButton("New USDC Off Ramp quote", callback_data='D'),
    ],
    [
	InlineKeyboardButton("Available quotes", callback_data='E'),
    ],]

short_keyboard = [
    [
	InlineKeyboardButton("New USDT Off Ramp quote", callback_data='C'),
	InlineKeyboardButton("New USDC Off Ramp quote", callback_data='D'),
    ],
    [
	InlineKeyboardButton("Available quotes", callback_data='E'),
    ],]

start_keyboard = [
    [
        InlineKeyboardButton("New USDT Off Ramp quote", callback_data='C'),
        InlineKeyboardButton("New USDC Off Ramp quote", callback_data='D'),
    ],
    [
        InlineKeyboardButton("Available quotes", callback_data='E'),
        InlineKeyboardButton("Transaction volume", callback_data='F'),
    ],]
 
# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
# set higher logging level for httpx to avoid all GET and POST requests being logged
#logging.getLogger("httpx").setLevel(logging.WARNING)
 
logger = logging.getLogger(__name__)
 
# Stages
START_ROUTES, TEXT_ROUTES, QUOTE_ROUTES, END_ROUTES = range(4)
 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    
    if False: #reeplazar por algo que revise si es festivo
        msg = TextMessages.hello + '\n' + TextMessages.holiday + '\n' + TextMessages.hours + '\n' + TextMessages.thanks + '\n' + TextMessages.bye
        await update.message.reply_markdown(text=msg)
        return END_ROUTES
        

    # elif not 495 <= (datetime.datetime.now(pytz.timezone('America/Bogota')).hour * 60 + datetime.datetime.now(pytz.timezone('America/Bogota')).minute) <= 10825:
    #     msg = TextMessages.hello + '\n' + TextMessages.outside_hours + '\n' + TextMessages.hours + '\n' + TextMessages.thanks + '\n' + TextMessages.bye
    #     await update.message.reply_markdown(text=msg)
    #     return END_ROUTES
    
    else:
        #TODO: ¿limpiar los usuarios al iniciar el día?
        if not update.effective_user.id in Memory.chats: # Crear el usuario
            Memory.chats[update.effective_user.id] = {"name": update.effective_user.full_name, "active_quote": 'NONE', "quotes":{}}
        reply_markup = InlineKeyboardMarkup(start_keyboard)
        msg = TextMessages.hello + '\n' + TextMessages.help + '\n'
        # Send message with text and appended InlineKeyboard
        await update.message.reply_text(msg, reply_markup=reply_markup)
        # Tell ConversationHandler that we're in state `FIRST` now
        return START_ROUTES
 
async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    reply_markup = InlineKeyboardMarkup(start_keyboard)
    msg = TextMessages.hello + '\n' + TextMessages.help + '\n'
    await update.message.reply_text(msg, reply_markup=reply_markup)
    return START_ROUTES
 
async def process_market_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
	chat_id = update.effective_user.id
	query = update.callback_query
	#TODO: revisar que la quote esté válida
	if __is_quote_void(chat_id, Memory.chats[chat_id]['active_quote']):
		msg = f""""This quote has expired, they are only valid for {QUOTEALIVE} minutes. Please obtain a new one."""
		await query.edit_message_text(text = msg, reply_markup = InlineKeyboardMarkup(short_keyboard))
		return START_ROUTES
        
	active_quote = Memory.chats[chat_id]['active_quote']
	data =  Memory.chats[chat_id]['quotes'][active_quote]
	await update.effective_message.reply_text((f'''Please type the amount you wish to sell (greater than *500 {data['token']}*).
		Write the amount without using periods or commas (“.” or “,”).''').replace("\t", ""))
	return TEXT_ROUTES	
	
async def refresh_quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global quote_ID
    query = update.callback_query
    # create the quote ID
    quote_ID += 1
    if len(str(quote_ID)) == 6:
        quote_ID = 1
       
    chat_id = update.effective_user.id
    active_quote = Memory.chats[chat_id]['active_quote']
    data =  Memory.chats[chat_id]['quotes'][active_quote]
    token = data['token']
    old_ramp = data['ramp_ID']
    #generar el quote en token
    #get the quote
    #TODO: poner el generador que es
	#rate = await __get_rate(context, chat_id, token, 1000)
    rate = uniform(3800.00, 4500.00)
    ramp = await __create_ramp(context, chat_id, token, DEFAULTAMOUNT, rate) #create the ramp 	
        
    data = {
        "ramp_ID": ramp['id'],
        "operation": ramp['rampType'],
        'date_start': datetime.datetime.now(pytz.timezone('America/Bogota')),
        'date_end': datetime.datetime.now(pytz.timezone('America/Bogota')) + QUOTEALIVE,
        'token' : token,
        'reference' : data['reference'],
        'rate' : rate
	}
    
    Memory.chats[chat_id]["active_quote"] = str(quote_ID).zfill(5)  #update this quote to be the active quote
    Memory.chats[chat_id]["quotes"][str(quote_ID).zfill(5)] = data
    del Memory.chats[chat_id]['quotes'][active_quote] #remove old quote
    #TODO actualizar la rampa para que la que genero el quote quede cerrado
    msg = (f"""*Refresh Quote details*:
			Quote ID: {Memory.chats[chat_id]["active_quote"]}
			Quote time: {data['date_start'].strftime("%d/%m/%Y, %H:%M:%S")}
			Valid until: {data['date_end'].strftime("%d/%m/%Y, %H:%M:%S")}
			Operation: Off Ramp
			Active and reference: {token}/COP
			`{Memory.chats[chat_id]["active_quote"]}: {token}/COP Quote: { '${:,.1f}'.format(rate) }, valid until {data['date_end'].strftime("%d/%m/%Y, %H:%M:%S")}`
            """).replace("\t", "") + '\n' + TextMessages.choose + '\n'
    
    await query.edit_message_text(text = msg, reply_markup = InlineKeyboardMarkup(order_keyboard),parse_mode='MarkdownV2')
    # Tell ConversationHandler that we're in state `FIRST` now
    return START_ROUTES   

async def new_USDT_quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
	
    global quote_ID
    
    query = update.callback_query
    # create the quote ID
    quote_ID += 1
    if len(str(quote_ID)) == 6:
        quote_ID = 1
       
    chat_id = update.effective_user.id

    if query.data =='C':
    	token = 'USDT'            
    elif query.data =='D':
        token = 'USDC'            
    #generar el quote en USDT
    #get the quote
    #TODO: poner el generador que es
	#rate = await __get_rate(context, chat_id, "USDT"", 1000)
    rate = uniform(3800.00, 4500.00)
    ramp = await __create_ramp(context, chat_id, token, DEFAULTAMOUNT, rate) #create the ramp 	
        
    data = {
        "ramp_ID": ramp['id'],
        "operation": ramp['rampType'],
        'date_start': datetime.datetime.now(pytz.timezone('America/Bogota')),
        'date_end': datetime.datetime.now(pytz.timezone('America/Bogota')) + QUOTEALIVE,
        'token' : token,
        'reference' : 'COP',
        'rate' : rate
	}
    
    Memory.chats[chat_id]["active_quote"] = str(quote_ID).zfill(5)  #update this quote to be the active quote
    Memory.chats[chat_id]["quotes"][str(quote_ID).zfill(5)] = data
    
	#TODO: Entender qué hace esto.
    # context.job_queue.run_repeating(__close_quota, 600, first=600, chat_id=chat_id, name="close_quota_" + str(chat_id) + "_" + data['token'], data=data)
    
    msg = (f"""*Quote details*:
			Quote ID: {Memory.chats[chat_id]["active_quote"]}
			Quote time: {data['date_start'].strftime("%d/%m/%Y, %H:%M:%S")}
			Valid until: {data['date_end'].strftime("%d/%m/%Y, %H:%M:%S")}
			Operation: Off Ramp
			Active and reference: {token}/COP
			`{Memory.chats[chat_id]["active_quote"]}: {token}/COP Quote: { '${:,.1f}'.format(rate) }, valid until {data['date_end'].strftime("%d/%m/%Y, %H:%M:%S")}`
            """).replace("\t", "") + '\n' + TextMessages.choose + '\n'
    
    await query.edit_message_text(text = msg, reply_markup = InlineKeyboardMarkup(order_keyboard))
    # Tell ConversationHandler that we're in state `FIRST` now
    return START_ROUTES

async def new_USDC_quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
	
    global quote_ID
    
    query = update.callback_query
    # create the quote ID
    quote_ID += 1
    if len(str(quote_ID)) == 6:
        quote_ID = 1
       
    chat_id = update.effective_user.id

    token = 'USDC'            
    #generar el quote en USDT
    #get the quote
    #TODO: poner el generador que es
	#rate = await __get_rate(context, chat_id, "USDT"", 1000)
    rate = uniform(3800.00, 4500.00)
    ramp = await __create_ramp(context, chat_id, token, DEFAULTAMOUNT, rate) #create the ramp 	
        
    data = {
        "ramp_ID": ramp['id'],
        "operation": ramp['rampType'],
        'date_start': datetime.datetime.now(pytz.timezone('America/Bogota')),
        'date_end': datetime.datetime.now(pytz.timezone('America/Bogota')) + QUOTEALIVE,
        'token' : token,
        'reference' : 'COP',
        'rate' : rate
	}
    
    Memory.chats[chat_id]["active_quote"] = str(quote_ID).zfill(5)  #update this quote to be the active quote
    Memory.chats[chat_id]["quotes"][str(quote_ID).zfill(5)] = data
    
	#TODO: Entender qué hace esto.
    # context.job_queue.run_repeating(__close_quota, 600, first=600, chat_id=chat_id, name="close_quota_" + str(chat_id) + "_" + data['token'], data=data)
    
    msg = (f"""*Quote details*:
			Quote ID: {Memory.chats[chat_id]["active_quote"]}
			Quote time: {data['date_start'].strftime("%d/%m/%Y, %H:%M:%S")}
			Valid until: {data['date_end'].strftime("%d/%m/%Y, %H:%M:%S")}
			Operation: Off Ramp
			Active and reference: {token}/COP
			`{Memory.chats[chat_id]["active_quote"]}: {token}/COP Quote: { '${:,.1f}'.format(rate) }, valid until {data['date_end'].strftime("%d/%m/%Y, %H:%M:%S")}`
            """).replace("\t", "") + '\n' + TextMessages.choose + '\n'
    
    await query.edit_message_text(text = msg, reply_markup =  InlineKeyboardMarkup(order_keyboard))
    # Tell ConversationHandler that we're in state `FIRST` now
    return START_ROUTES

async def list_quotes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    chat_id = update.effective_user.id
    __is_quote_void(chat_id, Memory.chats[chat_id]['active_quote']) #remove void quotations
    data = Memory.chats[chat_id]['quotes']
    msg = ''
    # print quotes
    for quote_ID in data.keys():
        msg += (f'''Quote ID: {quote_ID}: 
		{ '${:,.1f}'.format(data[quote_ID]['rate']) } {data[quote_ID]['token']}/COP. 
		valid until: {data[quote_ID]['date_end'].strftime("%H:%M:%S")}.''').replace("\t", "").replace("\n", "") + '\n'+'\n'
    msg += 'Please type the *Quote ID* you want to operate on (accept or refresh).'
    await query.answer()
    await update.effective_message.reply_text(msg)
    return QUOTE_ROUTES
   
async def volume(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
	#TODO: conectar con servicios
    # ramps_service_api = RampsServiceAPI()
    # client_id = os.getenv("CLIENT_ID_BITSO") #obtiene el id del cliente de Bitso
    # #Trae las rampas de bitso, filtra las que se hayan realizado hoy
	# ramps = ramps_service_api.get_completed_ramps_by_client(client_id, date_min = datetime.today().strftime('%Y-%m-%d')) 
	# volumeUSDC = [x["amountReceived"] for x in ramps and x["symbolTypeReceived"]=="USDC"]
	# volumeUSDT = [x["amountReceived"] for x in ramps and x["symbolTypeReceived"]=="USDT"]
	# volumeCOP = [x["amountSent"] for x in ramps ]
    volumeUSDC = [uniform(38000.00, 45050.00) for i in range(5)]
    volumeUSDT = [uniform(38000.00, 45050.00) for i in range(5)]
    volumeCOP = [volumeUSDC[i] * uniform(3800.00, 4505.00) + volumeUSDT[i] * uniform(3800.00, 4505.00) for i in range(len(volumeUSDT))]
    msg = (f"""*Processed Volume*.

		Today's processed volume sums to {'${:,.2f}'.format(sum(volumeUSDT))} USDT. and {'${:,.2f}'.format(sum(volumeUSDC))} USDC.
		The total amount of processed COP is {'${:,.2f}'.format(sum(volumeCOP))}""").replace("\t", "")
    reply_markup = InlineKeyboardMarkup(start_keyboard)
    await query.edit_message_text(msg, reply_markup=reply_markup)
    return START_ROUTES
 

async def quote_operations(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat_id = update.effective_user.id
    active_quote = update.message.text
    active_quote = active_quote.zfill(5)
    if __is_quote_void(chat_id, active_quote):
        msg = (f"""*Quote selection*:
		The provided quote ID ({active_quote}) is either non valid or has expired.""").replace("\t", "") + '\n' + TextMessages.choose + '\n'
        reply_markup = InlineKeyboardMarkup(start_keyboard)
    else:
        Memory.chats[chat_id]['active_quote'] = active_quote  #update de quote
        data = Memory.chats[chat_id]['quotes'][active_quote]
        msg = (f"""*Quote selection*:
		{Memory.chats[chat_id]["name"]}, you have selected quote {Memory.chats[chat_id]['active_quote']}.
		Details:
		Quote ID: {active_quote}
		Valid until: {data['date_end'].strftime("%H:%M:%S")}
		Operation: Off Ramp
		Quote: {'${:,.1f}'.format(data['rate'])} {data['token']}/COP
		`{Memory.chats[chat_id]["active_quote"]}: {data['token']}/COP Quote: { '${:,.1f}'.format(data['rate']) }, valid until {data['date_end'].strftime("%d/%m/%Y, %H:%M:%S")}`""").replace("\t", "") + '\n'
        reply_markup = InlineKeyboardMarkup(order_keyboard)
    await update.message.reply_text(msg, reply_markup=reply_markup)
    return START_ROUTES

async def place_market_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat_id = update.effective_user.id
    active_quote = Memory.chats[chat_id]['active_quote']
    data =  Memory.chats[chat_id]['quotes'][active_quote]
    try:
        amount = int(update.message.text)
    except ValueError: 
        msg = (f"""*Order confirmation*
		{Memory.chats[chat_id]["name"]}, the amount you have typed is not a numeric value. Please try again
        Type the amount you wish to sell (greater than *500 {data['token']}*).
		Write the amount without using periods or commas (“.” or “,”).""").replace("\t", "") + '\n'
        await update.effective_message.reply_text(msg)
        return TEXT_ROUTES	
    if amount <= 500:
        msg = (f"""*Order confirmation*
		{Memory.chats[chat_id]["name"]}, the amount you have typed is less than the minimun order. Please try again
        Type the amount you wish to sell (greater than *500 {data['token']}*).
		Write the amount without using periods or commas (“.” or “,”).""").replace("\t", "") + '\n'
        await update.effective_message.reply_text(msg)
        return TEXT_ROUTES
    else:
        Memory.chats[chat_id]['quotes'][active_quote]['amount'] = amount
        #TODO revisar si hay fondos
		#TODO: poner la orden
		#TODO: revisar que quedó plata (esto lo debe haer el market maker)
        msg = (f"""*Order confirmation*
			{Memory.chats[chat_id]["name"]}, we confirm we have received your request.
			We will check that the order is correctly placed in the order book and that the relevant amounts for this operation are available!
			Details:
			Quote ID: {active_quote}
			Quote time: {data['date_start'].strftime("%d/%m/%Y, %H:%M:%S")}
			Operation: Off Ramp
			Active and reference: {data['token']}/COP
			Amount: { '$ {:,.2f}'.format(amount) } {data['token']}""").replace("\t", "") + '\n'
    reply_markup = InlineKeyboardMarkup(start_keyboard)
    await update.message.reply_text(msg, reply_markup=reply_markup)
    return START_ROUTES

async def __create_ramp(context, chat_id, token, amount, rate):
    #TODO: cabiar por la que calcula la rampa
    data = {
        "amountReceived": 'null',
        "amountSent": 'null',
        "bankAccountId": "5a923f8d-760e-4d1a-b7f3-7f1db39006b9",
        "clientId": "e892c7fa-0f38-4fba-9315-66f63b2c743b",
        "clientWalletId": "bbef2d1e-d9a9-4c68-81e7-039aeafed315",
        "environment": "simulation",
        "id": "fba49d5a-32d8-490b-ae58-616be808da6c",
        "numberRamp": "0002324",
        "rampType": "off_ramp",
        "registerDate": "2023-08-11 16:00:29.225550",
        "status": "completed",
        "symbolTypeReceived": "COP",
        "symbolTypeSent": token,
        "trackType": "fasttrack"
    }
    return data

#check if the active quote is valid (returns True is the quote has expired or doesn't exists, False if the quote is valid), 
# removes all invalid quotes from memory for the active user
def __is_quote_void(chat_id, quote_key):
    try:
        int(quote_key)
    except ValueError: 
        return True
    active_quote = quote_key.zfill(5)
    if active_quote:
        data =  Memory.chats[chat_id]['quotes']
        now = datetime.datetime.now(pytz.timezone('America/Bogota'))
        expired = [id for id in data.keys() if data[id]['date_end'] < now] #these are the quotes that have expired
        for id in expired:
            del Memory.chats[chat_id]['quotes'][id]
            #TODO: cerrar las rampas correspondientes
        if active_quote in expired:
            Memory.chats[chat_id]['active_quote'] = 'NONE'
            return True
        elif active_quote in Memory.chats[chat_id]['quotes'].keys():
            return False
    return True

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6365315898:AAHkH7qUed2dMVQ-Mj9JSyEwYlLIgoZzIzg").build()
    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(process_market_order, pattern="^" + 'A' + "$"),
                CallbackQueryHandler(refresh_quote, pattern="^" + 'B' + "$"),
                CallbackQueryHandler(new_USDT_quote, pattern="^" + 'C' + "$"),
                CallbackQueryHandler(new_USDT_quote, pattern="^" + 'D' + "$"),
                CallbackQueryHandler(list_quotes, pattern="^" + 'E' + "$"),
                CallbackQueryHandler(volume, pattern="^" + 'F' + "$"),
            ],
            TEXT_ROUTES:  [
                MessageHandler(filters.TEXT & ~filters.COMMAND, place_market_order)
                ],
            QUOTE_ROUTES:  [
                MessageHandler(filters.TEXT & ~filters.COMMAND, quote_operations)
                ],
            END_ROUTES: [
                CallbackQueryHandler(start_over, pattern="^" + str(0) + "$"),
            ],
            },
    	fallbacks=[CommandHandler("start", start)],
        )
    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
    

