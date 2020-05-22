# DAVIDRVU - 2020 

from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
print(datetime.strptime("2020-05-21", "%Y-%m-%d").strftime("%A"))
