from tkinter import*
root=Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y, )

sizex = 600
sizey = 400
posx  = 40
posy  = 20
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

def CurSelet(evt):
    value=str((mylistbox.get(mylistbox.curselection())))
    print(value)


mylistbox = Listbox(root, yscrollcommand = scrollbar.set)
mylistbox.bind('<<ListboxSelect>>',CurSelet)
mylistbox.place(x=32,y=90)

for line in range(100):
    mylistbox.insert(END, "This is line number " + str(line))

root.mainloop()
