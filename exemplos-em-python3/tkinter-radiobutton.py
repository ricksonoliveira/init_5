#https://github.com/rg3/youtube-dl/blob/master/README.md#readme
from os import system
from tkinter import *
root = Tk()

def cb():
        print ("variable is", peg.get())
        if peg.get() == 1:
            rad1["text"]="fota"
            rad2["text"]="Two"
        else:
            rad2["text"]="fota"
            rad1["text"]="One"
peg = IntVar()

rad1 = Radiobutton(root, text="One", variable=peg, value=1)
rad1.place(x=10, y=10)
rad2 = Radiobutton(root, text="Two", variable=peg, value=2)
rad2.place(x=10, y=30)

btn_info = Button(root, text="ok", bd=1, cursor="hand2", command=cb)
btn_info.place(x=10, y=99)

root.mainloop()
