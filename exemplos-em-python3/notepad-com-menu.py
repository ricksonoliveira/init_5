#!/usr/bin/python3
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
root = Tk()

def salvar(): # Aqui é a função que salva o arquivo:

    fileName = asksaveasfilename()
    try:
        file = open(fileName, 'w')
        textoutput = text.get(0.0, END)
        file.write(textoutput)
    except:
        pass
    finally:
        file.close()

def abrir():# Aqui é a função que abre um arquivo


    fileName = askopenfilename()
    try:
        file = open(fileName, 'r')
        contents = file.read()

        text.delete(0.0, END)
        text.insert(0.0, contents)
    except:
        pass

def sobre():# uma pequena função "sobre" :D
    root = Tk()
    root.wm_title("Sobre")
    texto=("PyNotePad: Versão 1.0")
    textONlabel = Label(root, text=texto)
    textONlabel.pack()

root.wm_title("PyNotePad")# Aqui é o digito

# "inicia" a scroolbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

menubar = Menu(root)
#Aqui criamos os menus:
MENUarquivo = Menu(menubar)
MENUarquivo.add_command(label="Salvar", command=salvar)
MENUarquivo.add_command(label="Abrir", command=abrir)
menubar.add_cascade(label="Arquivo", menu=MENUarquivo)

MENUajuda = Menu(menubar)
MENUajuda.add_command(label="Sobre", command=sobre)
menubar.add_cascade(label="Ajuda", menu=MENUajuda)
root.config(menu=menubar)

# Aqui adicionamos a parte que fica o texto:
text = Text(root)
text.pack(expand=YES, fill=BOTH)

#aqui configura o scrollbar
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)


# Por Fim, a janela:
root.mainloop()
