a = lambda x, y: x * y
print(a(2,2))

lista = [
    ['p1', 3],
    ['p2', 6],
    ['p3', 14],
    ['p4', 30],
    ['p5', 13],
]

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

print(sorted(lista, key=lambda i: i[1]))