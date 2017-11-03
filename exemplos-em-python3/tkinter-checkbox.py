#!/usr/bin/python3
#https://github.com/rg3/youtube-dl/blob/master/README.md#readme
from os import system
from tkinter import *
root = Tk()

def cb():
        print ("variable is", peg.get())
        if peg.get() == 1:
            ch["text"]="fota"
        else:
            ch["text"]="cuzao"
peg = IntVar()
ch = Checkbutton(root, text="Expand", variable=peg)
ch.place(x=10, y=10)

btn_info = Button(root, text="ok", bd=1, cursor="hand2", command=cb)
btn_info.place(x=10, y=99)

root.mainloop()
