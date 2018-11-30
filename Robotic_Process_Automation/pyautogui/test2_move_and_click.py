# DAVIDRVU - 2018

import pyautogui
import subprocess
import time

#### OJO!:
# PyAutoGUI functions will raise a pyautogui.FailSafeException 
# if the mouse cursor is in the upper left corner of the screen.
# If you lose control and need to stop the current PyAutoGUI function,
# keep moving the mouse cursor up and to the left.

def main():

    print("MOVE AND CLICK!!!")
    waitTime = 5 # Seconds
    for i in range(0,waitTime):
        j = waitTime - i
        print("Espera " + str(j) + " segundos.    ", end="\r", flush=True)
        time.sleep(1)

    print("")
    acum_clicks = 0
    while(True):
        pyautogui.moveTo(688, 457)
        pyautogui.click()
        print("Click = " + str(acum_clicks))
        acum_clicks = acum_clicks + 1
        #pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
        time.sleep(2)


    print("DONE!")

if __name__ == "__main__":
    main()