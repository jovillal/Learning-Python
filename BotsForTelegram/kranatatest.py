import logging
import time
import traceback
import datetime
import requests

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
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

class Memory:
    
    last = 0
    token = "USDT"
    amount = 0.0
    token_cop = 0.0
    date = datetime.datetime.now()


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

context_local = None
Memory.last = 0
Memory.token = "USDT"


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    Memory.last = 1
    await update.message.reply_html(
        rf"""Hola {user.mention_html()}!
        
Te habla KraviBot, tu asistente virtual de Kravata.

Actualmente puedo ayudarte brindándote información sobre los siguientes temas relacionados con tu cuenta en Kravata:

*1 - Cotizar una orden off-ramp*

Si deseas continuar, escribe la opción deseada.

Puedes seleccionar la opción "0" en cualquier momento para terminar el proceso.""",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'good' in update.message.text.lower() or 'hello' in update.message.text.lower() or 'hola' in update.message.text.lower() or 'buenas' in update.message.text.lower() or 'hi' in update.message.text.lower():
        await update.message.reply_text(f"Hola {update.effective_chat.first_name}, para dar la tasa digite la palabra 'tasa'")
    elif update.message.text.lower() == 'tasa':
        await update.message.reply_text(f"Hola {update.effective_chat.first_name}, la tasa de hoy para usted es de 4.841,57 COP/USD")
    else:
        id = update.effective_chat.id
        await update.message.reply_text("Lo siento no entiendo su solicitud")

async def echo_bitso(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = None
    if 'good' in update.message.text.lower() or 'hello' in update.message.text.lower() or 'hola' in update.message.text.lower() or 'buenas' in update.message.text.lower() or 'hi' in update.message.text.lower() or Memory.last == 0:
        Memory.last = 1
        msg = f'''¡Hola {update.effective_chat.first_name}! 
        
Te habla KraviBot, tu asistente virtual de Kravata.

Actualmente puedo ayudarte brindándote información sobre los siguientes temas relacionados con tu cuenta en Kravata:

*1 - Cotizar una orden off-ramp*

Si deseas continuar, escribe la opción deseada.

Puedes seleccionar la opción "0" en cualquier momento para terminar el proceso.'''
    elif Memory.last == 1:
        msg = process_1(update.message.text)
    elif Memory.last == 2:
        msg = process_2(update.message.text)
    elif Memory.last == 3:
        msg = process_3(update.message.text)
    elif Memory.last == 4:
        msg = process_4(update.message.text)
        
    if not msg:
        Memory.last = 0
        msg = """¡Gracias por contactar a KraviBot!

Tu sesión ha finalizado exitosamente. Recuerda que estoy aquí siempre para ayudarte.

Que tengas un exelente día."""

    await update.message.reply_markdown(text=msg)
    
def process_1(text):
    if text == "1":
        Memory.last = 2
        return """*Cotizar una orden off-ramp*

Para cotizar una orden off-ramp, primero selecciona el token que quieres obtener:

*1 - USDT
2 - USDC*"""

    elif text != "0":
        return """Has ingresado una opción inválida. Por favor verifica la información ingresada e inténtalo nuevamente.

Actualmente puedo ayudarte brindándote información sobre los siguientes temas relacionados con tu cuenta en Kravata:

*1 - Cotizar una orden off-ramp*

Si deseas continuar, escribe la opción deseada.

Puedes seleccionar la opción "0" en cualquier momento para terminar el proceso."""

    return None

  
def process_2(text):
    if text == "1" or text == "2":
        Memory.last = 3
        Memory.token = "USDT" if text == "1" else "USDC"
        return f"""*Cotizar una orden off-ramp*

¡Gracias! Has seleccionado *{Memory.token}* para tu off-ramp. Ahora indica el monto de este token que deseas cotizar. Recuerda que el valor ingresado debe ser igual o superior a *500 {Memory.token}*

Escribe el número sin comas ni puntos ("," o ".")"""

    elif text != "0":
        return """*Cotizar una orden off-ramp*

Has ingresado una opción inválida. Por favor verifica la información ingresada e inténtalo nuevamente.

Para cotizar una orden off-ramp, primero selecciona el token que quieres obtener:

*1 - USDT
2 - USDC*

¿No es lo que buscabas?

Puedes seleccionar la opción "0" en cualquier momento para terminar el proceso."""

    return None


def process_3(text:str):
    if text.isdecimal() and float(text) >= 500:
        Memory.last = 4
        Memory.amount = float(text)
        Memory.date = datetime.datetime.now()
        res = requests.get(f"https://simulation.kravata.co/api/offramp/{text}?token={Memory.token}", verify=False)
        if res.status_code == 200:
            Memory.token_cop = res.json()["rateCopUsd"]
        
        return f"""*Detalles de la orden*

Fecha: {Memory.date.strftime("%d/%m/%Y, %H:%M:%S")}
Operación: off-ramp
Activo: {Memory.token}
Referencia: COP
Monto: {'$ {:,.2f}'.format(Memory.amount)} {Memory.token}

`Tasa {Memory.token}/COP: {'$ {:,.2f}'.format(Memory.token_cop)}`

_Esta cotización es válida durante 15 minutos_.

Elige una de las siguientes opciones:

*1 - Aceptar la negociación y crear la orden off-ramp
2 - Actualizar la cotización*

Puedes seleccionar la opción "*2*" en cualquier momento para tener una tasa cotizada en tiempo real."""

    elif text != "0":
        return f"""*Cotizar una orden off-ramp*

Has ingresado un valor {Memory.token} inválido nuestro sistema. Por favor indica el monto de este token que desas cotizar. Recuerda que el valor ingresado debe ser igual o superior a *500 {Memory.token}*

Escribe el número sin comas ni puntos ("," o ".")

Puedes seleccionar la opción "0" en cualquier momento para terminar el proceso."""

    return None

def process_4(text:str):
    if text == "1":
        Memory.last = 5
        return f"""*Confirmación de la orden*

Equipo Bitso, confirmamos la recepción de la solicitud. 

¡Vamos a revisar que tengamos la línea disponible para tu orden!

Detalles:

Fecha: {datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}
Operación: off-ramp
Activo: {Memory.token}
Referencia: COP
Monto: {'$ {:,.2f}'.format(Memory.amount)} {Memory.token}

`Tasa {Memory.token}/COP: {'$ {:,.2f}'.format(Memory.token_cop)}`"""

    elif text == "2":
        res = requests.get(f"https://simulation.kravata.co/api/offramp/{Memory.amount}?token=USDT", verify=False)
        if res.status_code == 200:
            Memory.token_cop = res.json()["rateCopUsd"]
        return f"""*Detalles de la orden*

Fecha: {datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}
Operación: off-ramp
Activo: {Memory.token}
Referencia: COP
Monto: {'$ {:,.2f}'.format(Memory.amount)} {Memory.token}

`Tasa {Memory.token}/COP: {'$ {:,.2f}'.format(Memory.token_cop)}`

_Esta cotización es válida durante 15 minutos_.

Elige una de las siguientes opciones:

*1 - Aceptar la negociación y crear la orden off-ramp
2 - Actualizar la cotización*

Puedes seleccionar la opción "*2*" en cualquier momento para tener una tasa cotizada en tiempo real."""

    elif text != "0":
        return """Has ingresado una opción inválida. Por favor verifica la información ingresada e inténtalo nuevamente.

Puedes seleccionar la opción "0" en cualquier momento para terminar el proceso."""
    
    return None



def remove_job_if_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    if not context.job_queue is None:
        current_jobs = context.job_queue.get_jobs_by_name(name)
        if not current_jobs:
            return False
        for job in current_jobs:
            job.schedule_removal()
    return True


async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Add a job to the queue."""
    context_local = context
    try:
        # args[0] should contain the time for the timer in seconds
        due = float(context.args[0])
        if due < 0:
            await update.effective_message.reply_text("Sorry we can not go back to future!")
            return

        while(True):
            for chat in ["1347866892", "5788309611", "-898858644", '1241745442']: 
                await context_local.bot.send_message(chat, text=f"Hola envio tasa actual!")
            time.sleep(due)

    except (IndexError, ValueError):
        await update.effective_message.reply_text("Usage: /set <seconds>")
    except Exception as e:
        traceback.print_exc()

async def unset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove the job if the user changed their mind."""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = "Timer successfully cancelled!" if job_removed else "You have no active timer."
    await update.message.reply_text(text)

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:    
    if 'blockfills' in update.message.text.lower():
        context_local = context
        chat_id = update.message.chat_id
        await update.message.reply_text("Usuario registrado")
        while(True):
            for chat in ['1241745442']: 
                await context_local.bot.send_message(chat, text=f"Hola envio tasa actual!")
            time.sleep(1)



def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6365315898:AAHkH7qUed2dMVQ-Mj9JSyEwYlLIgoZzIzg").build()
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("set", set_timer))
    application.add_handler(CommandHandler("unset", unset))
    application.add_handler(CommandHandler("register", register))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_bitso))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()
    
    
if __name__ == "__main__":
    main()
