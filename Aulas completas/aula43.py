#   Criando, lendo, escrevendo arquivos
#   https://docs.python.org/3/library/functions.html#open


with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.write('Linha 4\n')

    file.seek(0)
    print(file.read())



"""file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
file.write('Linha 4\n')

file.seek(0,0)

print('Lendo linhas:')
print(file.read())
file.close()
"""
