d1 = {'chave1':'valor da chave'}
d1['nova chave'] = 'valor da nova chave'

print(d1['chave1'])

d2 = dict(chave='Valor da chave', chave2= 'valor da chave 2')
print('Valor da chave' in d2.values())

for k in d2.items():
    print(k)

clientes = {
    'cliente1' : {
        'nome' : 'Luiz',
        'sobrenome' : 'Miranda',
    },
    'cliente2': {
        'nome': 'Marcos',
        'sobrenome': 'Correia',
    },

}
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')