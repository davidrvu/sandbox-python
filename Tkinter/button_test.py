from tkinter import *


class display():
    def __init__(self, controlframe):
        self.controlframe = controlframe
        self.namelist = ["Mike", "Rachael", "Mark", "Miguel", "Peter", "Lyn"]

    def callback(self, index):
        print(self.namelist[index])

    def showlist(self):
        self.frame = Frame(self.controlframe, height=100)
        self.frame.pack()
        row = 0
        for index, x in enumerate(self.namelist):
            label = Label(self.frame, text="%s " % x, width=17, anchor="w") #limit the name to 17 characters
            fooButton = Button(self.frame, text=str(x), command=lambda index=index: self.callback(index))
            label.grid(row=row, column=0, sticky="W")
            fooButton.grid(row=row, column=1)
            row = row + 1


tk = Tk()

D = display(tk)
D.showlist()
tk.mainloop()