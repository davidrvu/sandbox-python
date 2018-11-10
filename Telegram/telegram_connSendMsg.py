# DAVIDRVU - 2018

from checkPass import checkPass
from sendMessage import sendMessage
import telegram

def telegram_connSendMsg(debug, TOKEN, chat_id, mensaje):
    # Telegram Bot Authorization Token
    bot = telegram.Bot(TOKEN)
    # get the first pending update_id, this is so we can skip over it in case we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None
        sys.exit()
    #logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    sendMessage(debug, bot, chat_id, mensaje)

def main():
    ##################################################
    ## PARAMETROS
    ##################################################
    debug = 0
    keyring_serv = "telegram_group"
    ##################################################

    TOKEN, chat_id = checkPass(debug, keyring_serv)
    mensaje = "Estimado, soy un bot. Saludos coordiales!"

    telegram_connSendMsg(debug, TOKEN, chat_id, mensaje)

if __name__ == "__main__":
    main()