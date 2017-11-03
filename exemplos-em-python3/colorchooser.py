from tkinter import *
from tkinter.colorchooser import *
from colorvar import *
jan = Tk()
jan.title("Escolher cor")

color1 = c1
def getColor():

    # limpa porcausa da aglomeração do append
    arquivo = open('colorvar.py', 'w')
    # coloca os valores denovo, ficando sempre 2 visto q limpou em cima
    arquivo = open('colorvar.py', 'a')
    arquivo.write('c1 = "' + c1 + '"\n' + 'c2 = "' + c2 + '"\n')
    # retorna uma lista com o a cor na posição [1]
    color = askcolor(color1)
    gcolor = color[1]
    # muda o valor de cor do botão
    btn1["bg"] = gcolor
    # pega a variavel global de cor
    global color1
    # mantem a cor mudada pra próxima vez q for escolher
    color1 = gcolor
    # limpa o texto exadecimal velho
    lbl1.delete('1.0', END)
    # insere o texto exadecimal novo
    lbl1.insert(INSERT, color1)
    # escreve no arquivo de config
    arquivo = open('colorvar.py', 'a')
    arquivo.write('c1 = "'+gcolor+'"\n')

btn1 = Button(jan, text='    ', command=getColor, bg=color1)
btn1.place(x=0, y=0)

lbl1 = Text(jan, height=1, width=10)
lbl1.place(x=50, y=5)
lbl1.insert(INSERT, color1)

#2===============================
color2 = c2
def getColor():
    color = askcolor(color2)
    gcolor = color[1]
    btn2["bg"] = gcolor
    global color2
    color2 = gcolor
    lbl2.delete('1.0', END)
    lbl2.insert(INSERT, color2)
    #---------------------------
    arquivo = open('colorvar.py', 'a')
    arquivo.write('c2 = "'+gcolor+'"\n')

btn2 = Button(jan, text='    ', command=getColor, bg=color2)
btn2.place(x=0, y=30)

lbl2 = Text(jan, height=1, width=10)
lbl2.place(x=50, y=35)
lbl2.insert(INSERT, color2)

jan.geometry("500x300+100+100")
jan.mainloop()
