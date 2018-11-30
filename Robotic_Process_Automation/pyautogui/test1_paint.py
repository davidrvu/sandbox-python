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

    screenWidth, screenHeight = pyautogui.size()

    print("Opening PAINT ...")
    subprocess.Popen(['C:/Windows/System32/mspaint.exe'])
    print("PAINT OPENED!")

    #pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    #currentMouseX, currentMouseY = pyautogui.position()
    #pyautogui.moveTo(100, 150)
    #pyautogui.click()
    #pyautogui.moveRel(None, 10)  # move mouse 10 pixels down

    for i in range(0,5):
        j = 5 - i
        print("Espera " + str(j) + " segundos.")
        time.sleep(1)

    pyautogui.moveTo(screenWidth / 2, screenHeight / 2) #MOVE TO CENTER OF SCREEN
    distance = 100
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.5)   # move down
        pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.5)  # move up
        print("distance = " + str(distance))

    print("DONE!")

if __name__ == "__main__":
    main()