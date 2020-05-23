# DAVIDRVU - 2020

# Basado en: alejandroortega | https://github.com/alexFocus92/juego_de_la_vida/blob/master/juego.py
# Inspirado en el video del canal Dot CSV: https://www.youtube.com/watch?v=qPtKv9fSHZY
# Conway's Game of Life: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# pip install pygame

import pygame
import numpy as np
import time
import tkinter as tk
import tkinter.font as font
import os
import sys
from create_patterns import create_patterns

initial_option = None

def OnButtonClick(gui, button_id):
    global initial_option
    if button_id == 1:
        initial_option = "boton1"
    elif button_id == 2:
        initial_option = "boton2"
    elif button_id == 3:
        initial_option = "boton3"
    elif button_id == 4:
        initial_option = "boton4"
    
    print("initial_option = " + str(initial_option))
    gui.destroy()

def initialMenu():
    gui = tk.Tk(className="Conway's Game of Life | DAVIDRVU - 2020")

    # Gets the requested values of the height and widht.
    windowWidth  = 500 # gui.winfo_reqwidth()
    windowHeight = 500 # gui.winfo_reqheight()
    print("Width",windowWidth,"Height",windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(gui.winfo_screenwidth()/2 - windowWidth/2)
    positionDown  = int(gui.winfo_screenheight()/2 - windowHeight/2)

    # Positions the window in the center of the page.
    gui.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))
    
    # Texto de bienvenida
    #text2 = tk.Text(gui, height=20, width=50)
    #text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    #text2.insert(tk.END,'\nWilliam Shakespeare\n', 'big')
    #text2.pack(side=tk.LEFT)

    font_title    = font.Font(family='Helvetica', size=18, weight='bold')
    font_subtitle = font.Font(family='Helvetica', size=13, weight='bold')
    font_inst1    = font.Font(family='Helvetica', size=12)
    font_buttons  = font.Font(family='Helvetica', size=15, weight='bold')
    font_version  = font.Font(family='Helvetica', size=12)

    button_height = 2
    button_width  = 20

    label_title = tk.Label(gui, text="Wellcome to Conway's Game of Life")
    label_title['font'] = font_title
    label_title.place(relx = 0.5, rely = 0.0, anchor = 'n')

    label_subtitle = tk.Label(gui, text="DAVIDRVU - 2020")
    label_subtitle['font'] = font_subtitle
    label_subtitle.place(relx = 0.35, rely = 0.06)

    label_inst1 = tk.Label(gui, text="Press any key to pause simulation!\nSelect one initialization:")
    label_inst1['font'] = font_inst1
    label_inst1.place(relx = 0.25, rely = 0.11)

    label_version = tk.Label(gui, text="v2020.05.22")
    label_version['font'] = font_version
    label_version.place(relx = 1, rely = 1, anchor = "se")

    button1 = tk.Button(text=u"Empty", command=lambda: OnButtonClick(gui, 1), height = button_height, width = button_width )
    button1['font'] = font_buttons

    button2 = tk.Button(text=u"Random", command=lambda: OnButtonClick(gui, 2), height = button_height, width = button_width )
    button2['font'] = font_buttons

    button3 = tk.Button(text=u"Oscillators", command=lambda: OnButtonClick(gui, 3), height = button_height, width = button_width )
    button3['font'] = font_buttons

    button4 = tk.Button(text=u"Spaceships", command=lambda: OnButtonClick(gui, 4), height = button_height, width = button_width )
    button4['font'] = font_buttons

    button1.place(relx = 0.25, rely = 0.2)
    button2.place(relx = 0.25, rely = 0.4)
    button3.place(relx = 0.25, rely = 0.6)
    button4.place(relx = 0.25, rely = 0.8)

    gui.mainloop()

def main():
    print("====> GAME OF LIFE")

    initialMenu()

    print("MAIN initial_option = " + str(initial_option))

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30) # DISPLAY POSITION
    pygame.init() # Initialize PyGame
    pygame.display.set_caption("Conway's Game of Life | DAVIDRVU - 2020")

    WIDTH, HEIGHT = 800, 800
    #infoObject = pygame.display.Info()
    #WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h

    print("WIDTH  = " + str(WIDTH))
    print("HEIGHT = " + str(HEIGHT))

    nX, nY = 80, 80
    xSize = WIDTH/nX
    ySize = HEIGHT/nY

    screen = pygame.display.set_mode([WIDTH,HEIGHT]) # Set size of screen

    BG_COLOR   = (10,10,10) # Define background color
    LIVE_COLOR = (255,255,255)
    DEAD_COLOR = (128,128,128)
    # Celdas vivas = 1; Celdas muertas = 0

     # Intialize status of cells
    if initial_option == "boton1":   # Empty
        status = np.zeros((nX,nY))
    elif initial_option == "boton2": # Random
        status = np.round(np.random.rand(nX,nY))
    elif initial_option == "boton3": # Oscillators
        status = create_patterns("Oscillators", nX, nY)
    elif initial_option == "boton4": # Spaceships
        status = create_patterns("Spaceships", nX, nY)
    else:
        print("Boton initial_option = " + str(initial_option) + " aún no está configurado!")
        pygame.quit()
        sys.exit()

    pauseRun = False

    running = True
    n_gen = 0
    while running:

        newStatus = np.copy(status) # Copy status

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                pauseRun = not pauseRun

            mouseClick = pygame.mouse.get_pressed()
            if sum(mouseClick) > 0:
                posX, posY = pygame.mouse.get_pos()
                x, y = int(np.floor(posX/xSize)), int(np.floor(posY/ySize))
                #newStatus[x,y] = np.abs(newStatus[x,y]-1)
                newStatus[x,y] = not mouseClick[2]

        screen.fill(BG_COLOR) # Clean background

        for x in range(0,nX):
            for y in range(0,nY):

                if not pauseRun:
                    # Numero de vecinos
                    nNeigh = status[(x-1)%nX, (y-1)%nY] + status[(x)%nX,   (y-1)%nY] + \
                             status[(x+1)%nX, (y-1)%nY] + status[(x-1)%nX, (y)%nY  ] + \
                             status[(x+1)%nX, (y)%nY  ] + status[(x-1)%nX, (y+1)%nY] + \
                             status[(x)%nX,   (y+1)%nY] + status[(x+1)%nX, (y+1)%nY]

                    # Rule 1: Una celula muerta con 3 vecinas revive
                    if status[x,y] == 0 and nNeigh==3:
                        newStatus[x,y] = 1
                    # Rule 2: Una celula viva con mas de 3 vecinos o menos de 2 muere
                    elif status[x,y] == 1 and (nNeigh < 2 or nNeigh > 3):
                        newStatus[x,y] = 0

                poly = [(x*xSize,y*ySize),
                        ((x+1)*xSize,y*ySize),
                        ((x+1)*xSize,(y+1)*ySize),
                        (x*xSize,(y+1)*ySize)]

                if newStatus[x,y] == 1:
                    pygame.draw.polygon(screen, LIVE_COLOR, poly, 0)
                else:
                    pygame.draw.polygon(screen, DEAD_COLOR, poly, 1)
        
        if not pauseRun:
            print("n_gen = " + str(n_gen))
            font = pygame.font.Font('freesansbold.ttf', 32) 
            text = font.render("n_gen = " + str(n_gen), True, (0, 255, 0), (0, 0, 128)) 
            textRect = text.get_rect() # create a rectangular object for the text surface object   
            textRect.topleft = (0,0)  # set the center of the rectangular object. 
            n_gen = n_gen + 1

        screen.blit(text, textRect)

        status = np.copy(newStatus)
        time.sleep(0.1)
        pygame.display.flip()
        

    pygame.quit()
    print("DONE!")

if __name__ == "__main__":
    main()
