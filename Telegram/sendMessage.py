# DAVIDRVU - 2018

# PASOS CREACION BOT TELEGRAM - PYTHON
# 1) pip install python-telegram-bot    # REFERENCIA: https://github.com/python-telegram-bot/python-telegram-bot
# 2) En telegram crear bot con BotFather -> Se obtiene el TOKEN
# 3) Para obtener el chat_id:
#     3.1) Add the Telegram BOT to the group.
#     3.2) Get the list of updates for your BOT:
#           https://api.telegram.org/bot<YourBOTToken>/getUpdates
#     3.3) Look for the "chat" object
#     3.4) Use the "id" of the "chat" object to send your messages.

#import logging
from checkPass import checkPass
import datetime
import telegram
import time

def sendMessage(debug, bot, chat_id, mensaje):
    while True:
        try:
            bot.send_message(chat_id=chat_id, text=mensaje)
            print(mensaje)
            break
        except telegram.error.TimedOut:
            print("telegram.error.TimedOut ...")
            time.sleep(1)
        except telegram.error.NetworkError:
            print("NetworkError ...")
            time.sleep(1)
        except telegram.error.Unauthorized:
            print("The user has removed or blocked the bot. ...")
            time.sleep(1)

def main():
    ##################################################
    ## PARAMETROS
    ##################################################
    debug = 1
    keyring_serv = "telegram_group"
    ##################################################

    TOKEN, chat_id = checkPass(debug, keyring_serv)

    # Telegram Bot Authorization Token
    bot = telegram.Bot(TOKEN)
    # get the first pending update_id, this is so we can skip over it in case we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None
        sys.exit()
    #logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    for i in range(0, 10):
        time_now = datetime.datetime.now()
        mensaje = "Hola soy Juanito y ahora puedo mandar mensajes por Telegram -> " + str(time_now)
        sendMessage(debug, bot, chat_id, mensaje)
        time.sleep(5)

if __name__ == "__main__":
    main()