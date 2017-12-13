# Test function with optional arguments

def funcion_con_parametros_opcionales(obligatorio1, obligatorio2, **key_param):
    aux = obligatorio1 + obligatorio2
    if ('opcional1' in key_param):
        aux = aux + key_param["opcional1"]
    return aux

def main():
    resultado = funcion_con_parametros_opcionales(10, 20, opcional1 = 30)
    print("resultado = " + str(resultado))
    resultado = funcion_con_parametros_opcionales(10, 20)
    print("resultado = " + str(resultado))

if __name__ == "__main__":
    main()