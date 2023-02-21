from itertools import groupby

alunos = [
    {'nome':'Luiz', 'nota':'A'},
    {'nome':'João', 'nota':'B'},
    {'nome':'Letícia', 'nota':'A'},
    {'nome':'Rafaela', 'nota':'C'},
    {'nome':'Picles', 'nota':'D'},
    {'nome':'Lívia', 'nota':'A'},
    {'nome':'Aurora', 'nota':'A'},
    {'nome':'Spyro', 'nota':'B'},
    {'nome':'Nyvi', 'nota':'B'},
    {'nome':'Greer', 'nota':'C'},
    {'nome':'Lewdisia', 'nota':'A'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)
for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
    print()
