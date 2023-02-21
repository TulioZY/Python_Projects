"""
num1 = input('Digite um número inteiro: ')
if num1.isdigit():
    num1 = int(num1)
    if num1 % 2 == 0:
        print(f'{num1} é um número par')
    else:
        print(f'{num1} é um número ímpar')
else:
    print('Número inválido')
"""
"""
horario = input('Quantas horas ai amigão? (0 a 23) ')
if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('Digite um horário entre 0 e 23.')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Digite um horário entre 0 e 23.')
"""

nome = input('Digite seu primeiro nome: ')
tamanho = len(nome)
if tamanho <=4:
    print('Seu nome é muito curto kkkkk')
elif tamanho <=6:
    print('Seu nome é mediano, ta safe')
else:
    print('Nome grande da porra meno seloco.')