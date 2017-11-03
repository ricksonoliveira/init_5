from tkinter import *
janela = Tk()

import webbrowser

def callback(event):
    webbrowser.open_new(r"http://www.google.com")


link = Label(janela, text="Link do google", fg="blue", cursor="hand2")
link.place(x=0, y=50)
link.bind("<Button-1>", callback)

janela.geometry("300x200")
janela.mainloop() 
