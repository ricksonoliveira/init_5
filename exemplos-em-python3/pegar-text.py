from tkinter import *
root=Tk()
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    #print(inputValue)
    lbl["text"]=inputValue

textBox=Text(root, height=2, width=10)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Commit", command=lambda: retrieve_input())

lbl = Label(root, text="")
lbl.place(x=0, y=130)

buttonCommit.pack()
root.geometry("200x200+100+100")
mainloop()
