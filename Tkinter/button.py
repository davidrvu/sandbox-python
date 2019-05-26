# DAVIDRVU - 2019

from tkinter import *

def callback(root, custom_text):
    print("click en " + str(custom_text))
    root.destroy()


def main():

    root = Tk()
    frame = Frame(root)
    frame.pack()

    bottomframe = Frame(root)
    bottomframe.pack(side = BOTTOM)

    redbutton = Button(frame, text="Red", fg="red", command = lambda: callback(root, "Red"))
    redbutton.pack(side = LEFT)

    greenbutton = Button(frame, text="Brown", fg="brown", command = lambda: callback(root, "Brown"))
    greenbutton.pack(side = LEFT)

    bluebutton = Button(frame, text="Blue", fg="blue", command = lambda: callback(root, "Blue"))
    bluebutton.pack(side = LEFT)

    blackbutton = Button(bottomframe, text="Black", fg="black", command = lambda: callback(root, "Black"))
    blackbutton.pack(side = BOTTOM)

    

    root.mainloop()

if __name__== "__main__":
    main()