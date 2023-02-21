"""
while = Utilizado para realizar ações enquanto uma condição for verdadeira.
"""
"""
while True:
    nome = input("Qual o seu nome? ")
    print(f'Olá {nome}!')
"""
"""
x = 0
while x < 100:
    print(x)
    x = x + 1
print('Acabou garai!!!!!!!!!!')
"""
"""x = 0
while x < 10:
    if x == 3:
        x = x + 1 #soma +1 antes de dar print no 3, ficando 3+1, por isso pula o 3 na hr do print
        continue
    print(x)
    x = x + 1
print('Acabou parsa.')"""

'''x = 0
while x < 10:
    if x == 3:
        x = x + 1 #soma +1 antes de dar print no 3, ficando 3+1, por isso pula o 3 na hr do print
        break #isso aqui faz parar o codigo qnd atinge essa condição
    print(x)
    x = x + 1
print('Acabou parsa.')'''

'''x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'{x},{y}')
        y = y + 1
    x = x + 1
print('Acabou parsa.')'''

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
       print('Número ou operador inválido.')
       continue
    num_1 = int(num_1)
    num_2 = int(num_2)
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador inválido.')
    sair = input('Deseja sair? (sim ou não) ')
    if sair == 'sim' or sair == 's':
        break
    elif sair == 'não' or sair == 'n' or sair == 'nao':
        continue
    else:
        print('Não entendi.')