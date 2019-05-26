# DAVIDRVU - 2019

from tkinter import messagebox
import tkinter as tk

def main():
    root = tk.Tk()
    root.withdraw()
    
    respuesta = messagebox.askyesno('Titulo de la ventana 1','¿Quieres descargar el archivo XXXX desde EBOOK?',icon = 'question')
    if respuesta == True:
    	print("La respuesta es SI")
    else:
    	print("La respuesta es NO")

    print ("DONE!")

if __name__== "__main__":
    main()