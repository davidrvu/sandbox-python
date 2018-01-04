import argparse

def main():
    #############################
    ## ARGUMENTS AND PARAMETERS 
    #############################
    print("ARGUMENTS AND PARAMETERS: ")

    parser = argparse.ArgumentParser(description='Process some arguments.')

    parser.add_argument('--delay_time', type=int,  default=5,  help='Tiempo retardo entre envío de cada correo')

    args = parser.parse_args()
    delay_time  = args.delay_time
    print("_________________________________________________________")
    print("_________________ARGUMENTS_______________________________")
    print("delay_time    = " + str(delay_time))

if __name__ == "__main__":
    main()