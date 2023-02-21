k = 0
soma = 0
nota = 80
n = 5

while soma == 0:
    soma = 290 + nota
    k = k + 1
    if k >= n:
        break
    media = soma / n
    print(f'Nota média: {media}')
    if media >= 70:
        print('Aprovado!')
    else:
        print('Reprovado :c')
