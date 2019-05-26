# DAVIDRVU - 2019

from tkinter import messagebox
import tkinter as tk

def main():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo('Titulo de la ventana 1','You will now return to the application screen',icon = 'error')

    messagebox.showinfo('Titulo de la ventana 2','You will now return to the application screen',icon = 'warning')

    messagebox.showinfo('Titulo de la ventana 3','You will now return to the application screen',icon = 'info')

    messagebox.showinfo('Titulo de la ventana 4','You will now return to the application screen',icon = 'question')

    print ("DONE!")

if __name__== "__main__":
    main()