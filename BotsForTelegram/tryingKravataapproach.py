"""
Created on Thu Aug 9 11:01:51 2023

A telegram bot from Kravata's flow

@author: jovillal
"""
import datetime
import pytz

from telegram import __version__ as TG_VER
from telegram.ext import Updater
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
from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

class Memory:
    last = 0
    date = datetime.datetime.now()

class TextMessages:
    hello = "Hello Bitso!\nThis is KraviBot chat, (Kravata’s virtual assistant)."
    outside_hours = "We are outside office hours."
    holiday = "Today is a holiday in Colombia."
    #TODO: poder cambiar las horas de funcionamiento
    hours = "Remember, we are here to help during our business hours (*Colombia Time*): *Monday through Friday from 8:15 to 13:45*."
    help = "I can help you with the following actions related to your account:"
    thanks = "Thank you for using Kravibot: web3 made simple for everyone."
    bye = "Have an excellent day!"

async def access_btn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text('You have selected ' + query.data)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = None
    if False: #reeplazar por algo que revise si es festivo
        msg = TextMessages.hello + '\n' + TextMessages.holiday + '\n' + TextMessages.hours + '\n' + TextMessages.thanks + '\n' + TextMessages.bye
        await update.message.reply_markdown(text=msg)
        

    # elif not 495 <= (datetime.datetime.now(pytz.timezone('America/Bogota')).hour * 60 + datetime.datetime.now(pytz.timezone('America/Bogota')).minute) <= 10825:
    #     msg = TextMessages.hello + '\n' + TextMessages.outside_hours + '\n' + TextMessages.hours + '\n' + TextMessages.thanks + '\n' + TextMessages.bye
    #     await update.message.reply_markdown(text=msg)
    
    elif '0' in update.message.text.lower() or 'good' in update.message.text.lower() or 'hello' in update.message.text.lower() or 'hola' in update.message.text.lower() or 'buenas' in update.message.text.lower() or 'hi' in update.message.text.lower() or Memory.last == 0:
        keyboard = [
            [
                InlineKeyboardButton("New USDT Off Ramp quote", callback_data='USDT Off Ramp quote'), 
                InlineKeyboardButton("New USDC Off Ramp quote", callback_data='USDC Off Ramp quote'),
            ],
            [
                InlineKeyboardButton("Available quotes", callback_data='available quotes'),
                InlineKeyboardButton("Transaction volume", callback_data='transaction volume'),
            ],
            ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        msg = TextMessages.hello + '\n' + TextMessages.help + '\n'
        await update.message.reply_text(msg, reply_markup=reply_markup)
   
    # elif Memory.last == 1:
    #     msg = process_1(update.message.text)
    # elif Memory.last == 2:
    #     msg = process_2(update.message.text)
    # elif Memory.last == 3:
    #     msg = process_3(update.message.text)
    # elif Memory.last == 4:
    #     msg = process_4(update.message.text) 

    #await update.message.reply_markdown(text=msg)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #Send a message when the command /start is issued.
    user = update.effective_user
    Memory.last = 1
    await update.message.reply_html(
        rf"""Hola {user.mention_html()}!\nSigue las instrucciones de los mensajes.""",
        reply_markup=ForceReply(selective=False),
    )

def main() -> None:
# esto no funciona ¿?
#def start() -> None:
	#load_dotenv()
	#application = Application.builder().token(str(os.getenv("TOKEN_CHATBOT_TELEGRAM"))).build()
    application = Application.builder().token("6365315898:AAHkH7qUed2dMVQ-Mj9JSyEwYlLIgoZzIzg").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(access_btn))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()

   
if __name__ == "__main__":
    main()
