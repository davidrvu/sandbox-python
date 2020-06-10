# DAVIDRVU - 2020

# EJEMPLOS SIMPLES PULP

# PARA INSTALAR:
#   pip install pulp
#   conda install -c conda-forge glpk

import math
import numpy as np
import pulp
import sys

#########################################################################################################################################
def ejemplo01():
    print("\n----> START " + str(sys._getframe().f_code.co_name) )
    # FUENTE: https://benalexkeen.com/linear-programming-with-python-and-pulp-part-2/

    my_lp_problem = pulp.LpProblem("My_LP_Problem", pulp.LpMaximize)

    x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
    y = pulp.LpVariable('y', lowBound=2, cat='Continuous')

    # Objective function
    my_lp_problem += 4 * x + 3 * y, "Z"

    # Constraints
    my_lp_problem += 2 * y <= 25 - x
    my_lp_problem += 4 * y >= 2 * x - 8
    my_lp_problem += y <= 2 * x - 5

    print("\nPROBLEMA PLANTEADO: ")
    print(my_lp_problem)

    print("\nSOLVE: ")
    my_lp_problem.solve()

    print("\nSTATUS: ")
    print(pulp.LpStatus[my_lp_problem.status])

    print("\nRESULTADOS: ")
    for variable in my_lp_problem.variables():
        print("{} = {}".format(variable.name, variable.varValue))

    print("\nOPTIMO: ")
    print(pulp.value(my_lp_problem.objective))

#########################################################################################################################################
def ejemplo02():
    print("\n----> START " + str(sys._getframe().f_code.co_name) )

    my_lp_problem = pulp.LpProblem("Problema_simple", pulp.LpMinimize)

    x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
    y = pulp.LpVariable('y', lowBound=0, cat='Continuous')

    # Objective function
    my_lp_problem += x+y, "Z" # IDEAL: FUNCIÓN OBJETIVO DISTANCIA EUCLIDIANA! pero es un solver lineal!

    # Constraints
    my_lp_problem += -x + 4 <= y
    my_lp_problem += y >= 2
    my_lp_problem += x >= 2

    print("\nPROBLEMA PLANTEADO: ")
    print(my_lp_problem)

    print("\nSOLVE: ")
    my_lp_problem.solve()

    print("\nSTATUS: ")
    print(pulp.LpStatus[my_lp_problem.status])

    print("\nRESULTADOS: ")
    for variable in my_lp_problem.variables():
        print("{} = {}".format(variable.name, variable.varValue))

    print("\nOPTIMO: ")
    print(pulp.value(my_lp_problem.objective))

#########################################################################################################################################
def escalera_v01():
    print("\n----> START " + str(sys._getframe().f_code.co_name) )

    estimacion_unidades = [200, 200, 400, 200, 200, 200, 200]
    cota_total_maxima   = 1000 #1600

    dias_secuencia      = list(range(0, len(estimacion_unidades)+0))
    num_dias_escalera   = len(estimacion_unidades)
    unidades_totales    = sum(estimacion_unidades)
    print("dias_secuencia    = " + str(dias_secuencia))
    print("unidades_totales  = " + str(unidades_totales))
    print("cota_total_maxima = " + str(cota_total_maxima))

    prob      = pulp.LpProblem("Escalera_de_Cotas", pulp.LpMinimize)

    # Creación de las variables
    #cota      = pulp.LpVariable('cota', lowBound=0, cat='Continuous')
    cota      = pulp.LpVariable.dicts("cota", dias_secuencia, 0, None, pulp.LpInteger)

    #Crea un diccionario llamado escalera, se crea para guardar las variables referenciadas
    x         = pulp.LpVariable.dicts("Escalera", (dias_secuencia,dias_secuencia), 0, None, pulp.LpInteger) # TODOTODO: OJO REVISAR RESTRICCIONES

    # x(v,p) [MATRIZ DE 31x31]
    #        v -> día de venta   (COLUMNAS)
    #        p -> dia de picking (FILAS)

    #Funcion objetivo
    prob += pulp.lpSum([x[v][p]*(p-v) for v in dias_secuencia for p in range(v, num_dias_escalera)]), "Funcion_Objetivo"


    # 1.3. Restricciones

    # 1.3.1. Escalera de picking
#    for v in range(0, num_dias_escalera):
#        for p in range(v, num_dias_escalera):
#            if p == 0:
#                prob += x[0][0] <= cota[0], "x_0_0"
#            else:
#                # TODOTODO: LINEALIZAR ESTE MÍNIMO
#
#                #prob += x[v][p] == min( cota[p]- pulp.lpSum(x[vv][p] for vv in range(0, p) ), x[v][p]), "x_" + str(v) + "_" + str(p)
#                #prob += x[v][p] == np.min( [ cota[p]- pulp.lpSum(x[vv][p] for vv in range(0, p) ), x[v][p] ] ), "x_" + str(v) + "_" + str(p)
#                prob += x[v][p] == np.min( [ cota[p]- pulp.lpSum(x[vv][p] for vv in range(0, p) ), estimacion_unidades[v] - pulp.lpSum(x[v][pp] for pp in range(0,p) ) ] ), "x_" + str(v) + "_" + str(p)
#
#                #prob += x[v][p] == cota[p] - pulp.lpSum(x[vv][p] for vv in range(0, p) ), "x_" + str(v) + "_" + str(p)

    # 1.3.2. Picking de todas las ventas -> Cumplir estimacion de unidades (SUMA POR COLUMNAS)
    for v in dias_secuencia: # v columna # p filas
        #if v == num_dias_escalera-1:
        #    prob += pulp.lpSum([x[v][p] for p in range(v, min(v + 6, num_dias_escalera))]) <= estimacion_unidades[v], "Estimacion"+str(v)
        #else:
        #    prob += pulp.lpSum([x[v][p] for p in range(v, min(v + 6, num_dias_escalera))]) == estimacion_unidades[v], "Estimacion"+str(v)
        prob += pulp.lpSum([x[v][p] for p in range(v, min(v + 6, num_dias_escalera))]) == estimacion_unidades[v], "Estimacion"+str(v)

    # 1.3.3. Límite de cotas por días -> Cumplir la cota (SUMA POR FILAS)
    for p in dias_secuencia: # v columna # p filas
        prob += pulp.lpSum([x[v][p] for v in range(0, p+1)]) <= cota[p], "Cota"+str(p)

    # 1.3.4. Límite de cotas del periodo -> Sumatoria de cotas menor a cota_total_maxima
    prob += pulp.lpSum([cota[p] for p in range(0, num_dias_escalera)]) <= cota_total_maxima, "Cota_total"


    print("\nPROBLEMA PLANTEADO: ")
    print(prob)

    print("\nSOLVE: ")
    prob.solve(pulp.GLPK_CMD())
    #prob.solve()

    #for v in dias_secuencia: # columnas
    #    for p in range(v, min(v + 6, num_dias_escalera)): # filas
    #        print(str(v) + " " + str(p) + " " + str(x[v][p]) + " " + str(x[v][p].varValue))
    #sys.exit()

    print("\nSTATUS: ")
    print(pulp.LpStatus[prob.status])

    print("\nRESULTADOS: ")
    for variable in prob.variables():
        print("{} = {}".format(variable.name, variable.varValue))

    print("\nOPTIMO: ")
    print(pulp.value(prob.objective))

    escalera_output = np.zeros((num_dias_escalera,num_dias_escalera))
    for v in dias_secuencia:
         for p in range(v, num_dias_escalera):
            escalera_output[p,v] = x[v][p].varValue
    print("escalera_output = ")
    print(escalera_output)

#########################################################################################################################################
def main():
    num_char = 130

    print('='*num_char)

    ejemplo01()

    print('='*num_char)

    ejemplo02()

    print('='*num_char)

    escalera_v01()

    print('='*num_char)

    print("DONE !")

if __name__ == "__main__":
    main()