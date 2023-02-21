from dados import pessoas, produtos, lista

#nova_lista = filter(lambda x: x > 5, lista)
#nova_lista = [x for x in lista if x > 5]
def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False


nova_lista = filter(lambda p: p['preco'] > 15, produtos)


for produto in nova_lista:
    print(produto)
print('#' * 50)
adulto = filter(filtra, pessoas)
for maior in adulto:
    print(maior)