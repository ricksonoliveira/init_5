#!/usr/bin/python3
from tkinter import *
from os import path
import base64
master = Tk()

# Imagem encodada na base64
img1 = "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"

img = PhotoImage(data=img1)
master.tk.call('wm', 'iconphoto', master._w, img)

lbinput = Label(master, text='Caminho exato da imagem')
lbinput.place(x=10, y=15)

ent = Entry(master)
ent.place(x=10, y=40)

lbinput2 = Label(master, text='Variavel da imagem')
lbinput2.place(x=10, y=80)

ent2 = Entry(master)
ent2.place(x=10, y=105)

t0 = '---------------------------------------------------------------------------------------------'
lbout0 = Label(master, text=t0, justify='left')
lbout0.place(x=10, y=150)

lbout = Label(master, text='. . .', justify='left')
lbout.place(x=10, y=160)


def imagefor64(imagem_path, var, file_py, var_py):  # caminho da imagem, variavel que a imagem receberá, arquivo python a ser gravado
    myimage = open("{}".format(imagem_path), "rb")  # le o arquivo no modo binario
    content = myimage.read()  # le o arquivo
    myimage.close()
    imagebyte = base64.b64encode(content)  # codifica para base64
    imagestr = imagebyte.decode()  # transforma em string
    # cria arquivo com o código da imagem no formato base64
    output = open("{}".format(file_py),"a")
    output.write('{} = "{}"\n\n'.format(var, imagestr))
    output.close()

    if path.exists(var_py) == True:
        pass
    else:
        outfile = open("{}".format(var_py),"w")
        outfile.write('#### Variaveis para usar com tkinter 3 ####\n\n\n')
        outfile.close()

    outputvar = open("{}".format(var_py),"a")
    outputvar.write('img_{} = PhotoImage(data={})\n\n'.format(var, var))
    outputvar.close()
    pass


def ok():
    p = ent.get().strip()
    v = ent2.get().strip()
    try:
        if p == '':
            lbout['text'] = 'Caixa vazia'
        elif v == '':
            lbout['text'] = 'Variável vazia'
        else:
            g = ent.get()
            i = imagefor64(g, v, 'image_code.py', 'image_var.txt')
            lbout['text'] = '\nCódigo salvo no arquivo com o nome image_code.py\n\nVariáveis salvas no arquivo image_var.txt'
            ent.delete(0, END)
            ent2.delete(0, END)

    except Exception as er:
        lbout['text'] = 'Ocorreu um erro\n\n{}'.format(er)
        ent.delete(0, END)

bt = Button(master, text='OK', command=ok)
bt.place(x=340, y=310)



master.geometry('400x350+500+100')
master.mainloop()
