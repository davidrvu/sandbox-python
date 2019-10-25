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

from checkPass import checkPass
import datetime
import imgkit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import six
import sys
import telegram
import time

def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#445b11', row_colors=['#CFF4AB', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in  six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax

def sendMessage(bot, chat_id, mensaje):
    while True:
        try:
            bot.send_message(chat_id=chat_id, text=mensaje, parse_mode=telegram.ParseMode.HTML)
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

    TOKEN   = "XXX"
    chat_id = "XXX" # "AI Planning"

    # Telegram Bot Authorization Token
    bot = telegram.Bot(TOKEN)


    data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd'], 'col_3': [123, 345, 567, 678]}
    df_in = pd.DataFrame.from_dict(data)

    ax = render_mpl_table(df_in, header_columns=0, col_width=2.0)
    fig = ax.get_figure()
    fig.savefig('df_image.png')

    bot.sendPhoto(chat_id=chat_id, photo=open('df_image.png', 'rb'))

    sendMessage(bot, chat_id, "HOLA: ESTA ES LA <b>TABLA AUTOMÁTICA</b> PARA TELEGRAM")

    sendMessage(bot, chat_id, df_in.to_string(index=False, col_space=15, justify="right"))

    print("DONE!")

if __name__ == "__main__":
    main()