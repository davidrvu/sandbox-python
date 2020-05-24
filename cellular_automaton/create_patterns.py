# DAVIDRVU - 2020

import numpy as np

# SOURCE: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

def create_patterns(type_pat, nX, nY):
    status = np.zeros((nX,nY))

    if type_pat == "Oscillators":

        ###################################################################################################
        ###################################################################################################
        # Blinker  (period 2)
        status[10,10] = 1
        status[10,11] = 1
        status[10,12] = 1

        ###################################################################################################
        ###################################################################################################
        # Toad (period 2)
        status[20,10] = 1
        status[21,10] = 1
        status[22,10] = 1
        status[21,11] = 1
        status[22,11] = 1
        status[23,11] = 1

        ###################################################################################################
        ###################################################################################################
        # Beacon (period 2)
        status[30,10] = 1
        status[31,10] = 1
        status[30,11] = 1
        status[31,11] = 1
        status[32,12] = 1
        status[33,12] = 1
        status[32,13] = 1
        status[33,13] = 1

        ###################################################################################################
        ###################################################################################################
        # OTRO
        status[40,10] = 1
        status[41,10] = 1
        status[42,10] = 1
        status[46,10] = 1
        status[47,10] = 1
        status[48,10] = 1

        status[38,11] = 1
        status[44,11] = 1
        status[45,11] = 1
        status[50,11] = 1

        status[38,12] = 1
        status[44,12] = 1
        status[45,12] = 1
        status[50,12] = 1

        status[38,13] = 1
        status[44,13] = 1
        status[45,13] = 1
        status[50,13] = 1

        status[40,14] = 1
        status[41,14] = 1
        status[42,14] = 1
        status[46,14] = 1
        status[47,14] = 1
        status[48,14] = 1

        ###################################################################################################
        ###################################################################################################
        # Pulsar (period 3) x, y  -> fila, columna
        status[20,30] = 1
        status[21,30] = 1
        status[22,30] = 1
        status[26,30] = 1
        status[27,30] = 1
        status[28,30] = 1

        status[18,32] = 1
        status[23,32] = 1
        status[25,32] = 1
        status[30,32] = 1

        status[18,33] = 1
        status[23,33] = 1
        status[25,33] = 1
        status[30,33] = 1

        status[18,34] = 1
        status[23,34] = 1
        status[25,34] = 1
        status[30,34] = 1

        status[20,35] = 1
        status[21,35] = 1
        status[22,35] = 1
        status[26,35] = 1
        status[27,35] = 1
        status[28,35] = 1

        ####################### espejo
        status[20,37] = 1
        status[21,37] = 1
        status[22,37] = 1
        status[26,37] = 1
        status[27,37] = 1
        status[28,37] = 1

        status[18,38] = 1
        status[23,38] = 1
        status[25,38] = 1
        status[30,38] = 1

        status[18,39] = 1
        status[23,39] = 1
        status[25,39] = 1
        status[30,39] = 1

        status[18,40] = 1
        status[23,40] = 1
        status[25,40] = 1
        status[30,40] = 1

        status[20,42] = 1
        status[21,42] = 1
        status[22,42] = 1
        status[26,42] = 1
        status[27,42] = 1
        status[28,42] = 1

        ###################################################################################################
        ###################################################################################################
        # Penta-decathlon (period 15)
        status[50,37] = 1
        status[51,37] = 1
        status[52,37] = 1

        status[50,38] = 1
        status[51,38] = 0
        status[52,38] = 1

        status[50,39] = 1
        status[51,39] = 1
        status[52,39] = 1

        status[50,40] = 1
        status[51,40] = 1
        status[52,40] = 1

        status[50,41] = 1
        status[51,41] = 1
        status[52,41] = 1

        status[50,42] = 1
        status[51,42] = 1
        status[52,42] = 1

        status[50,43] = 1
        status[51,43] = 0
        status[52,43] = 1

        status[50,44] = 1
        status[51,44] = 1
        status[52,44] = 1

        ###################################################################################################
        ###################################################################################################
        
    elif type_pat == "Spaceships":
        # Glider
        status[10,10] = 1
        status[11,10] = 1
        status[12,10] = 1
        status[12,9]  = 1
        status[11,8]  = 1
        #Light-weight spaceship (LWSS)
        status[20,10] = 1
        status[23,10] = 1
        status[24,11] = 1
        status[20,12]  = 1
        status[24,12]  = 1
        status[21,13]  = 1
        status[22,13]  = 1
        status[23,13]  = 1
        status[24,13]  = 1
        
        #Middle-weight spaceship (MWSS)
        status[32,30] = 1
        status[30,31] = 1
        status[34,31] = 1
        status[35,32] = 1
        status[30,33] = 1
        status[35,33] = 1
        status[31,34] = 1
        status[32,34] = 1
        status[33,34] = 1
        status[34,34] = 1
        status[35,34] = 1

        #Heavy-weight spaceship (HWSS)
        status[32,45] = 1
        status[33,45] = 1
        status[30,46] = 1
        status[35,46] = 1
        status[36,47] = 1
        status[30,48] = 1
        status[36,48] = 1
        status[31,49] = 1
        status[32,49] = 1
        status[33,49] = 1
        status[34,49] = 1
        status[35,49] = 1
        status[36,49] = 1

        #The R-pentomino
        #status[21,60] = 1
        #status[22,60] = 1
        #status[20,61] = 1
        #status[21,61] = 1
        #status[21,62] = 1
    
    elif type_pat == "glider_gun": # Gosper glider gun
        x_ini = 35
        y_ini = 25
        status[x_ini + 24, y_ini + 0] = 1

        status[x_ini + 22, y_ini + 1] = 1
        status[x_ini + 24, y_ini + 1] = 1

        status[x_ini + 12, y_ini + 2] = 1
        status[x_ini + 13, y_ini + 2] = 1
        status[x_ini + 20, y_ini + 2] = 1
        status[x_ini + 21, y_ini + 2] = 1
        status[x_ini + 34, y_ini + 2] = 1
        status[x_ini + 35, y_ini + 2] = 1

        status[x_ini + 11, y_ini + 3] = 1
        status[x_ini + 15, y_ini + 3] = 1
        status[x_ini + 20, y_ini + 3] = 1
        status[x_ini + 21, y_ini + 3] = 1
        status[x_ini + 34, y_ini + 3] = 1
        status[x_ini + 35, y_ini + 3] = 1

        status[x_ini + 0 , y_ini + 4] = 1
        status[x_ini + 1 , y_ini + 4] = 1
        status[x_ini + 10, y_ini + 4] = 1
        status[x_ini + 16, y_ini + 4] = 1
        status[x_ini + 20, y_ini + 4] = 1
        status[x_ini + 21, y_ini + 4] = 1

        status[x_ini + 0 , y_ini + 5] = 1
        status[x_ini + 1 , y_ini + 5] = 1
        status[x_ini + 10, y_ini + 5] = 1
        status[x_ini + 14, y_ini + 5] = 1
        status[x_ini + 16, y_ini + 5] = 1
        status[x_ini + 17, y_ini + 5] = 1
        status[x_ini + 22, y_ini + 5] = 1
        status[x_ini + 24, y_ini + 5] = 1

        status[x_ini + 10, y_ini + 6] = 1
        status[x_ini + 16, y_ini + 6] = 1
        status[x_ini + 24, y_ini + 6] = 1

        status[x_ini + 11, y_ini + 7] = 1
        status[x_ini + 15, y_ini + 7] = 1

        status[x_ini + 12, y_ini + 8] = 1
        status[x_ini + 13, y_ini + 8] = 1

    return status