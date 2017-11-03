#!/usr/bin/python3
from tkinter import *
master = Tk()

#--- Geometry
master.attributes("-fullscreen", True)

#--- Quit
def close(event):
    master.withdraw()
master.bind('<Escape>', close)


def sair():
    master.destroy()
quit = Button(master, text='x', bg='#000', activebackground='#000', padx=20, pady=10,
              fg='#fff', activeforeground='#fff', command=sair, relief='flat', cursor='hand2')
quit.place(relx=1, x=-1, y=1, anchor=NE)

#--- Continue

master.mainloop()
