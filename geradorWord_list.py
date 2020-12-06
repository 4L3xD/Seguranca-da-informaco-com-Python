import itertools

string = input('String a ser permutada: ')
resultados = itertools.permutations(string, len(string))

for i in resultados:
    print(''.join(i))