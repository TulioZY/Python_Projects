"""
Split, Join, Enumerate em python
Split - Dividir uma String # str
Join - Juntar uma lista # str
Enumerate - Enumerar elementos de uma lista # list / iteráveis
strip - remove espaços do inicio e fim
capitalize - primeira letra sempre maiuscula
"""

string = "bora fi, ce ta brabo?"
lista = string.split(",")
print(lista)
for valor in lista:
    contagem = lista.count(valor)
    print(valor)
    print(contagem)