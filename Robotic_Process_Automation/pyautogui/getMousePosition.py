# DAVIDRVU - 2018

import pyautogui
import subprocess
import time

#### OJO!:
# PyAutoGUI functions will raise a pyautogui.FailSafeException 
# if the mouse cursor is in the upper left corner of the screen.
# If you lose control and need to stop the current PyAutoGUI function,
# keep moving the mouse cursor up and to the left.

def getMousePosition(debug):
    pos = pyautogui.position()
    return pos

def main():
    print("=========================")
    print("==  getMousePosition   ==")
    print("=========================")
  
    debug = 1
    screenWidth, screenHeight = pyautogui.size()

    print("screenWidth  = " + str(screenWidth))
    print("screenHeight = " + str(screenHeight))

    while(True):
        pos = getMousePosition(debug)
        print("("+str(pos[0])+","+str(pos[1])+")     ", end="\r", flush=True)
        time.sleep(0.2)


    print("DONE!")

if __name__ == "__main__":
    main()