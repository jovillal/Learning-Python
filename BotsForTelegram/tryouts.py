msg = """*Hello Bitso!"

	This is KraviBot chat, (Kravata’s virtual assistant).

	Today is a holiday in Colombia.

	Remember, we are here to help during our business hours (*Colombia Time*): *Monday through Friday from 8:15 to 13:45*.

	Thank you for using Kravibot: web3 made simple for everyone.

	Have an excellent day!""".replace("\t","")
print(msg)
quote_ID = 485
if len(str(quote_ID+1)) == 6:
    quote_ID = 0
else:
    quote_ID += 1

print(str(quote_ID).zfill(5))

import datetime
import pytz

QUOTEALIVE = datetime.timedelta(minutes=3) 

class Memory:
	chats = {}
        
Memory.chats['16786'] = {"name": "Jorge Villalobos", "state": 'START', "quotes":{}}

chat_id = '16786'

ramp = {
        "amountReceived": 'null',
        "amountSent": 446952.55,
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
        "symbolTypeSent": "USDT",
        "trackType": "fasttrack"
    }

Memory.chats[chat_id]["quotes"][ramp["id"]] = {
        "display_ID" : str(quote_ID).zfill(5),
        "operation": ramp['rampType'],
        'date_start': datetime.datetime.now(pytz.timezone('America/Bogota')),
        'date_end': datetime.datetime.now(pytz.timezone('America/Bogota')) + QUOTEALIVE,
        'token' : 'USDT',
        'reference' : 'COP',
         'rate' : 156
	}

print(Memory.chats)

