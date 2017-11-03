#!/usr/bin/python3
from sys import argv
from os import system
from re import findall
from tkinter import *
if len(argv) <= 1:
    print('Sem argumentos')
else:
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
    l = Label(master, text=nomes)
    l.place(x=0, y=0)
    master.mainloop()
