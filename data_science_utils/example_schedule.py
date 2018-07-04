# DAVIDRVU - 2018
from print_time import print_time
import schedule
import time

def job_function(parameter1, parameter2):
    string_out = "I'm working... " + parameter1 + parameter2
    print_time(string_out)
    return

def main():
    print("=============================================")
    print("== Testing SCHEDULE FUNCTION -> EVERY DAY! ==")
    print("=============================================")

    hora_programacion = "18:14"
    parameter1        = "Hello "
    parameter2        = "World!"

    #####################################################
    # TEST 1
    schedule.every().day.at(hora_programacion).do(job_function, parameter1, parameter2)
    
    # TEST 2
    #schedule.every(1).minute.do(job_function, parameter1, parameter2)

    print("while True ...")
    while True:
        schedule.run_pending()
        time.sleep(1)

    print("DONE!")

if __name__ == "__main__":
    main()