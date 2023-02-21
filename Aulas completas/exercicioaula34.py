carrinho = []
total= []

carrinho.append(('Produto 1', 20))
carrinho.append(('Produto 2', 40.50))
carrinho.append(('Produto 3', '10'))
carrinho.append(('Produto 4', 650))
carrinho.append(('Produto 5', 720))
carrinho.append(('Produto 6', 7))

total = sum([float(y) for x, y in carrinho])

print(total)