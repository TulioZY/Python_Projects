"""
count - itertools
"""
from itertools import count

contador1 = count(start=5, step=-0.1)

for valor in contador1:
    print(round(valor, 2))
    if valor >= 10 or valor <=-10:
        break
contador2 = count()
lista = ['Maria', 'Joao', 'Eduardo', 'Rafaela']
lista = zip(contador2, lista)

print(list(lista))