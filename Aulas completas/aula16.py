"""
Formatando valores com modificadores

:s
:d
:f
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 1
num_2 = 1550
num_3 = 5555
num_1 = float(num_1)

print(f'{num_1:0<10}')
print(f'{num_2:0>10}')
print(f'{num_3:0^10}')
print(f'{num_2:.2f}')
print(f'{num_2:0>10.2f}')

nome = 'Alabahama'
nome_formatado = '{:@>54}'.format(nome)
print(f'{nome:#^70}')
print(nome_formatado)

print(nome.upper())
print(nome.lower())
print(nome.title())