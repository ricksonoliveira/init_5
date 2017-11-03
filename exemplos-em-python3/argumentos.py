from argparse import ArgumentParser
variavel = ArgumentParser(description = 'Um programa de exemplo.')
variavel.add_argument('--frase', action = 'store', dest = 'frase',
                           default = 'Hello, world!', required = False,
                           help = 'A frase que deseja imprimir n vezes.')
variavel.add_argument('-n', action = 'store', dest = 'n', required = True,
                           help = 'O número de vezes que a frase será impressa.')
arguments = variavel.parse_args()
for i in range(0, int(arguments.n)):
    print(arguments.frase)
