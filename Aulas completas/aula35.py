"""
Zip = unindo iteráveis
Zip_longest = itertools
"""
from itertools import zip_longest, count

indice = count()

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador']

Estados = ['SP', 'MG', 'BA']

cidades_estados = zip(indice, cidades, Estados)
for valor in cidades_estados:
    print(valor)


print('#' * 50)
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Veredinha']

Estados = ['SP', 'MG', 'BA']

cidades_estados = zip_longest(cidades, Estados, fillvalue='Estado')
for valor in cidades_estados:
    print(valor)