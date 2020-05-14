# DAVIDRVU - 2020

import sys
import matplotlib.pyplot as plt
import datetime

def first_step(max_cell):
    # Se inicializa con una fila de ceros y un 1 al centro (Semilla inicial)
    ini = [0]*max_cell
    if max_cell%2: # CASO IMPAR
        ini[max_cell // 2] = 1
    else:       # CASO PAR
        ini.insert(max_cell//2, 1)
    return [ini]

def get_trios(l):
    return zip(l,l[1:],l[2:])       

def rule30(trio):
    return trio[0] ^ (trio[1] or trio[2]) # [left_cell XOR (central_cell OR right_cell)]

def calc_rule(fila):
    list_trios_input = get_trios([0] + fila + [0]) # Se agregan ceros en los bordes (padding)
    new_gen = []
    for trio in list_trios_input:
        new_gen.append(rule30(trio))
    return new_gen
    #return [rule(t) for t in list_trios_input] 

def all_rules_loop(max_cell, max_iter):
    matrix = first_step(max_cell)
    #while matrix[-1][0] == 0: # Mientras el primer valor de la generación más reciente sea un 0
    for i in range(0,max_iter):
        #print(matrix[-1][0])
        matrix.append(calc_rule(matrix[-1]))
    return matrix

def plot_output(output):
    plt.figure(figsize=(10,6))
    plt.imshow(output, cmap='hot')
    plt.show(block=False)
    return plt

def main():
    print("=====> RULE30 CELLULAR AUTOMATON") # https://en.wikipedia.org/wiki/Rule_30
    print("Stephen Wolfram in 1983")

    ######################################################################
    # PARAMS
    ######################################################################
    max_cell = 2000
    max_iter = 1500
    ######################################################################
    tini_all_main = datetime.datetime.now()
    output = all_rules_loop(max_cell, max_iter)
    #print(output)
    plt = plot_output(output)

    tfin_all_main = datetime.datetime.now()
    delta_time_all_main = tfin_all_main - tini_all_main
    print("delta_time_all_main = " + str(delta_time_all_main))
    print("DONE!")
    plt.show()

if __name__ == "__main__":
    main()