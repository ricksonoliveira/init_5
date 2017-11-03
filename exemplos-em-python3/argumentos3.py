#!/usr/bin/python3
from sys import argv
from os import system
from re import findall
from tkinter import *
# Completo
completo = argv[1]

# Caminho sem o arquivo
caminho = findall(r'/.+/', completo)

# Extenção do arquivo
extencao = findall(r'\..*', completo)

# Apelação com erro fdp ao converter list pra string
c1 = '{}'.format(completo)
comp = c1.replace('[', '').replace(']', '')

c2 = '{}'.format(caminho)
cami = c2.replace("['", "").replace("']", "")

c3 = '{}'.format(extencao)
exte = c3.replace("['", "").replace("']", "")

# Nome do arquivo com extenção
nomec = comp.replace(cami, '')

# Nome do arquivo sem extenção
nomes = nomec.replace(exte, '')

master = Tk()
master.title('instalador')

text1 = Label(master, wraplength=480, justify='left' ,text='O seguinte arquivo será instalado\n\n{}'.format(nomec),
              font='Arial 12')
text1.place(x=10, y=10)

ok = Button(master, text='Continuar')
ok.place(x=300, y=260)

cc = Button(master, text='Cancelar')
cc.place(x=410, y=260)

master.geometry('500x300+500+100')
master.resizable(0, 0)
master.mainloop()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
