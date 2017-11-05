#!/usr/bin/python3
from sys import argv
from os import system

arquivo = argv[1]

# Pegar extenções com pontos
ext_8 = str(arquivo[-8:])  # De 8 caracteres
ext_7 = str(arquivo[-7:])  # De 7 caracteres
ext = str(arquivo[-4:])    # De 4 caracteres

# Verificar os de 2 extenções primeiro

# tar.bz2
if ext_8 == '.tar.bz2':
    print('\ntar -jxvf {}\n\n...'.format(arquivo))
    system('tar -jxvf "{}"'.format(arquivo))

# tar.gz
elif ext_7 == '.tar.gz':
    print('\ntar -vzxf {}\n\n...'.format(arquivo))
    system('tar -vzxf "{}"'.format(arquivo))

# zip
elif ext == '.zip':
    print('\nunzip {}\n\n...'.format(arquivo))
    system('unzip "{}"'.format(arquivo))

# rar
elif ext == '.rar':
    print('\nunrar x {}\n\n...'.format(arquivo))
    system('unrar x "{}"'.format(arquivo))


# tar
elif ext == '.tar':
    print('\ntar -xvf {}\n\n...'.format(arquivo))
    system('tar -xvf "{}"'.format(arquivo))

# bz2
elif ext == '.bz2':
    print('\nbunzip2 -d {}\n\n...'.format(arquivo))
    system('bunzip2 -d "{}"'.format(arquivo))

else:
    print('Desculpe, extenção não suportada :(')
