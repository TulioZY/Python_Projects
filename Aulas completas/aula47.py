from itertools import combinations, permutations, product

pessoas = ['João', 'Maria', 'Luiz', 'Túlio']
camisetas = [
    ['Preta', 'Branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
    ]


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))