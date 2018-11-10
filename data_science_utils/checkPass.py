# DAVIDRVU - 2018

from print_time import print_time
from printDeb import printDeb
import keyring
import os
import sys

def checkPass(debug, keyring_serv):
    printDeb(debug, "\n----> START " + str(sys._getframe().f_code.co_name) )
    try:
        username_value = keyring.get_password(keyring_serv, "username")
        password_value = keyring.get_password(keyring_serv, username_value)
    except Exception as e:
        print("ERROR KEYRING: Revisar credencial para keyring_serv = " + str(keyring_serv) + " | e = " + str(e))
        sys.exit()

    if username_value is None:
        print("ERROR KEYRING: Revisar credencial para keyring_serv = " + str(keyring_serv) + " | username_value = " + str(username_value))
        sys.exit()
    printDeb(debug, "----> END " + str(sys._getframe().f_code.co_name) + "\n")
    return [username_value, password_value]