# DAVIDRVU - 2018

from datetime import datetime 

def print_time(input_string):
    dtnow = datetime.now()
    dtnow = dtnow.replace(microsecond=0)
    current_time = str(dtnow)
    print(current_time + " " + input_string)

def main():
    print_time("Sólo testing ...")

if __name__ == "__main__":
    main()