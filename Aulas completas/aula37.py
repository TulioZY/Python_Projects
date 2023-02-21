"""
combinations, permutations e product
combinação = ordem nao importa
permutação = ordem importa
ambos n repetem valores unicos
produto = ordem importa e permite repetir valores unicos
"""
from itertools import permutations, combinations, product, count
contador = count()
itens = ['sword', 'helm', 'boots', 'legs', 'ring', 'necklace']
itens = zip(contador, itens)
i = 0
for set in permutations(itens, 2):
    print(i, set)
    i = i + 1
    