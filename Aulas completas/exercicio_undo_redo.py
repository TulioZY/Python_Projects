"""
Faça uma lista de tarefa com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer  (a cada vez que chamarmos, desfaz a ultima ação)
    opção de refazer    (a cada vez que chamarmos, refaz a ultima ação)
"""
from time import sleep

print('1 - Adicionar tarefa')
tarefas = []
tarefas_backup = []

num_tarefas = len(tarefas)
num_tarefas_backup = len(tarefas_backup)

if num_tarefas_backup > num_tarefas:
    tarefas_backup = tarefas_backup.pop()

while True:
    opcoes = input("Digite um número correspondente à opção desejada: ")
    if opcoes == '1':
        add = input('Descreva sua tarefa a ser adicionada: ')
        tarefas.append(add)
        tarefas_backup.append(add)
        print("Tarefa adicionada com sucesso!")
        print('#'*50)
        print("Sua lista de tarefas: ")
        for t in tarefas:
            print (t)
        print('#'*50)

    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Desfazer última tarefa')
    print('4 - Refazer última tarefa')
    if opcoes == '2':
        print('#'*50)
        for t in tarefas:
            print (t)
        print('#'*50)
    if opcoes == '3':
        tarefas.pop()
        print('Tarefa removida!')
        print('#'*50)
        print('Tarefas Atuais:')
        for t in tarefas:
            print (t)
        print('#'*50)
    if opcoes == '4':
        tarefas = tarefas_backup
        print('Voltando no tempo...')
        sleep(1)
        print('...')
        sleep(1)
        print('Feito!')
        print('#'*50)
        print('Tarefas Atuais:')
        for t in tarefas:
            print (t)
        print('#'*50)