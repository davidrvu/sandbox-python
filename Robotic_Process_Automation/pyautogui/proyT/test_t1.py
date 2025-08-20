# DAVIDRVU - 2019

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

    print("Go to center screen...")
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2) #MOVE TO CENTER OF SCREEN
    distance = 100
    #while distance > 0:
    #    pyautogui.dragRel(distance, 0, duration=0.5)   # move right
    #    distance -= 5
    #    pyautogui.dragRel(0, distance, duration=0.5)   # move down
    #    pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
    #    distance -= 5
    #    pyautogui.dragRel(0, -distance, duration=0.5)  # move up
    #    print("distance = " + str(distance))

    cont = 0
    while(True):
        print("\n"+ str(datetime.datetime.now())+ " cont = " + str(cont) + "     ", end='\r', flush=True)
        #pyautogui.click(x=screenWidth / 2, y=screenHeight / 2)
        if ((cont != 0) and (cont % 800 == 0)):
            print("    Refreshing webpage ...")
            pyautogui.press('f5')
            time.sleep(4)
        time.sleep(random.uniform(0.5, 2))
        if random.uniform(0, 1) > 0.5:
            print("    Presiona espacio ...")
            pyautogui.press('space')
            time.sleep(0.2)
        if random.uniform(0, 1) > 0.5:
            print("    Presiona espacio ...")
            pyautogui.press('space')
            time.sleep(0.2)
        print("    Presiona escape ...")
        pyautogui.press('escape') 
        print("    Presiona flecha a la derecha ...")
        pyautogui.click(x=screenWidth / 2, y=3*screenHeight / 4)         
        pyautogui.press('right')   # press the right arrow key
        cont = cont + 1

    print("DONE!")

if __name__ == "__main__":
    main()