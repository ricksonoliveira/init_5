#!/usr/bin/python3
from tkinter import *
from conf.kdialog import *
def rmprog():
    root = Tk()

    def CurSelet(evt):
        value=str((mylist.get(mylist.curselection())))
        print(value)
        dialog_info('text')

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y, )

    mylist = Listbox(root, yscrollcommand = scrollbar.set, width=70, height=30)
    mylist.place(x=0, y=0)
    mylist.bind('<<ListboxSelect>>',CurSelet)

    for line in range(100):
        mylist.insert(END, "This is line number " + str(line))

    #mylist.pack( side = LEFT, fill = BOTH )

    scrollbar.config( command = mylist.yview )

    root.geometry('500x470+500+100')
    root.mainloop()
