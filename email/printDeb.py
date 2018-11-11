# DAVIDRVU - 2018

def printDeb(debug, str_in):
    if debug == 1:
        print(str_in)

def main():
    debug = 1
    printDeb(1, "Sólo testing 1 ...")
    debug = 0
    printDeb(0, "Sólo testing 2 ...")
    debug = 1
    printDeb(1, "Sólo testing 3 ...")

if __name__ == "__main__":
    main()