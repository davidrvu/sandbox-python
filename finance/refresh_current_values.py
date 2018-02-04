# DAVIDRVU 2018

from get_VALUES_to_CLP import get_VALUES_to_CLP
from get_VALUES_to_CLP import printdeb
import os
import sqlite3
import sys

##################################################
## Para ver base de datos usar programa : DB Browser for SQLite
##################################################
def refresh_current_values(debug, dir_sql_receiver, current_time, current_USD_to_CLP, current_EUR_to_CLP):
    basename_dir_sql_receiver = os.path.dirname(dir_sql_receiver) 
    if not os.path.exists(basename_dir_sql_receiver):
        os.makedirs(basename_dir_sql_receiver)

    try:
    	conn    = sqlite3.connect(dir_sql_receiver) # Connect accede a la base de datos, en la carpeta del programa. si no existe, la crea
    except sqlite3.OperationalError:
    	print("\nERROR: No es posible crear la base de datos dir_sql_receiver = " + dir_sql_receiver)
    	sys.exit()
    cursor0 = conn.cursor()                     # Cursor abre la base de datos, para poder operar sobre ella

    # SE CREA SÓLO SI NO EXISTE
    cursor0.execute('CREATE TABLE IF NOT EXISTS soluciones (id INTEGER PRIMARY KEY AUTOINCREMENT, current_time BLOB, current_USD_to_CLP REAL, current_EUR_to_CLP REAL)')
    # SE AGREGA UN REGISTRO NUEVO
    cursor0.execute('INSERT INTO soluciones (current_time, current_USD_to_CLP, current_EUR_to_CLP) VALUES (?, ?, ?)', (current_time, current_USD_to_CLP, current_EUR_to_CLP))            
    conn.commit()


def main():
    print("Testing refresh_current_values ...")
    debug = 0

    [current_time, current_USD_to_CLP, current_EUR_to_CLP] = get_VALUES_to_CLP(debug)

    dir_sql_receiver = "C:\\repos\\sandbox-python\\finance\\database\\history.db"
    print("dir_sql_receiver = " + dir_sql_receiver)
    refresh_current_values(debug, dir_sql_receiver, current_time, current_USD_to_CLP, current_EUR_to_CLP)

    print("DONE!")

if __name__ == "__main__":
    main()