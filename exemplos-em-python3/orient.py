#!/usr/bin/python3
from tkinter import *
root = Tk()


class Janela:
    def __init__(self, top_level):
        self.frame1 = Frame(top_level)
        self.frame1.grid()

        self.lbl = Label(self.frame1, text="Menu cara")
        self.lbl.grid(column=0, row=0)

        self.btn = Button(self.frame1, text="Ir para config 1", command=self.change_text_0)
        self.btn.grid(column=2, row=1)

    def change_text_0(self):
        self.frame1.destroy()
        Janela2(root)


class Janela2:
    def __init__(self, top_level2):
        self.frame2 = Frame(top_level2)
        self.frame2.grid()

        self.lbl = Label(self.frame2, text="Config 2")
        self.lbl.grid(column=0, row=0)

        self.btn = Button(self.frame2, text="Sai", command=self.change_text)
        self.btn.grid(column=2, row=1)

    def change_text(self):
        self.frame2.destroy()
        Janela(root)

Janela(root)
root.geometry("500x400+300+100")
root.mainloop()
