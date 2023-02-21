perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4','c': '5',},
        'resposta_certa': 'b',

    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '3', 'b': '10', 'c': '6', },
        'resposta_certa': 'c',

    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 10*2? ',
        'respostas': {'a': '20', 'b': '40', 'c': '50', },
        'resposta_certa': 'a',

    },
    'Pergunta 4': {
        'pergunta': 'Qual a capital do Brasil? ',
        'respostas': {'a': 'Minas gerais', 'b': 'Brasília', 'c': 'Acre', },
        'resposta_certa': 'b',

    },
    'Pergunta 5': {
        'pergunta': 'You ______ beautiful. ',
        'respostas': {'a': 'is', 'b': 'are', 'c': 'to', },
        'resposta_certa': 'b',

    },
    'Pergunta 6': {
        'pergunta': 'Quanto é 100 + 100? ',
        'respostas': {'a': '300', 'b': '123', 'c': '200', },
        'resposta_certa': 'c',

    },
}
respostas_certas = 0
for chave_p, chave_r in perguntas.items():
    print(f'{chave_p}: {chave_r["pergunta"]} ')

    for resposta_key, resposta_value in chave_r['respostas'].items():
        print(f'[{resposta_key}]: {resposta_value}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == chave_r['resposta_certa']:
        print("GG acertou memo")
        respostas_certas += 1
    else:
        print('Uma mula msm, errou obviamente')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acertos = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} das respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acertos}% das questões.')