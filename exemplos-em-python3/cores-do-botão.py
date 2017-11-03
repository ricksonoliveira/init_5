from tkinter import *

master=Tk()
def ok():
    if lb["text"] == "Sapo":
        lb["text"] = "Cobra"
    elif lb["text"] == "Cobra":
        lb["text"] = "Sapo"
        
lb = Label(master, text="Sapo", font="Helvetica 10 bold italic")
lb.place(x=10, y=50)

bt = Button(master, text="n", fg="#fff", activeforeground="#fff", bg="#999", activebackground="#aaa", relief=FLAT, padx=30, pady=7, cursor="hand2", font="Icon-Works 15", command=ok)
bt.place(x=10, y=100)

master.geometry("200x200+500+100")
master.mainloop()
