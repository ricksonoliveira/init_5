#!/usr/bin/python3
from tkinter import *
from tkinter.filedialog import askopenfilename
root = Tk()
texto = "ola mundão vei"
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Aqui adicionamos a parte que fica o texto:
text = Text(root)
text.pack(expand=YES, fill=BOTH)

#aqui configura o scrollbar
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

text.insert(INSERT, texto)

root.mainloop()
