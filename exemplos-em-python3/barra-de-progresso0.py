from tkinter import *
from time import sleep
master = Tk()

lb1 = Label(master, text='', bg='#ff0000', width='10')
lb1.place(x=0, y=0)

button = Button(master, text="start", command=start)
button.place(x=0, y=30)

master.geometry('500x500+300+100')
master.mainloop()
