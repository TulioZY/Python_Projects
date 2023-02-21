lista_1 = [10, 14, 513, 53, 61, 74]
lista_2 = [53, 13, 64, 2, 5]

lista_junta = [(x + y) for x, y in zip(lista_1, lista_2)]
print(lista_junta)

lista_soma = []
for i, _ in enumerate(lista_2):
    lista_soma.append(lista_1[i] + lista_2[i])
print(lista_soma)