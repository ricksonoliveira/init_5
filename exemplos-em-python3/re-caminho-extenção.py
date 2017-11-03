#!/usr/bin/python3
from sys import argv
from os import system
from re import findall

novo = 'MOMOMO'

le = len(argv)
l = []
x = 0
while x < le:
    l.append(x)
    x += 1
del l[0]
del argv[0]
for (l, a) in zip(l, argv):

    completo = a

    # Caminho sem o arquivo
    x = findall(r'/.+/', str(completo))
    if not x:
        caminho = 'null'
    else:
        caminho = x[0]

    # Extenção do arquivo
    xx = findall(r'\..*', str(completo))
    if not xx:
        extencao = 'null'
    else:
        extencao = xx[0]

    #system('mv "{}" "{}{}{}{}"\n'.format(completo, caminho, novo, l, extencao))
    #print('mv "{}" "{}{}{}{}"\n'.format(completo, caminho, novo, l, extencao))

    f = open('/home/neon/cuibo.txt', 'a')
    f.write('mv "{}" "{}{}{}{}"\n'.format(completo, caminho, novo, l, extencao))
    f.close
