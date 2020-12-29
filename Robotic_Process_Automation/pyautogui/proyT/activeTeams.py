# DAVIDRVU - 2020

import datetime
import pyautogui
import random
import subprocess
import time

#### OJO!:
# PyAutoGUI functions will raise a pyautogui.FailSafeException 
# if the mouse cursor is in the upper left corner of the screen.
# If you lose control and need to stop the current PyAutoGUI function,
# keep moving the mouse cursor up and to the left.

def main():

    screenWidth, screenHeight = pyautogui.size()

    #pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    #currentMouseX, currentMouseY = pyautogui.position()
    #pyautogui.moveTo(100, 150)
    #pyautogui.click()
    #pyautogui.moveRel(None, 10)  # move mouse 10 pixels down

    for i in range(0,5):
        j = 5 - i
        print("Espera " + str(j) + " segundos.")
        time.sleep(1)

    cont = 0
    while(True):
        print(str(datetime.datetime.now())+ " cont = " + str(cont) + "     ", end='\r', flush=True)
        pyautogui.click()
        pyautogui.moveRel(1, 0) # move mouse 1 pixel RIGHT
        pyautogui.moveRel(-1, 0) # move mouse 1 pixel LEFT
        time.sleep(10)
        cont = cont + 1

    print("DONE!")

if __name__ == "__main__":
    main()