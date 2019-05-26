# DAVIDRVU - 2019

from tkinter import filedialog
import tkinter as tk

def main():
    root = tk.Tk()
    root.withdraw()
    selected_file = filedialog.askopenfilename(initialdir = "/",title = "Seleccione archivo de XXXX")
    print ("selected_file = " + str(selected_file))

if __name__== "__main__":
    main()