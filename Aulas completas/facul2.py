nome = input('Qual seu nome? ')
peso = input('Qual seu peso? ')
altura = input('Qual sua altura? ')
sexo = input('Qual seu sexo? (f ou m) ')

peso = int(peso)
altura = float(altura)

if sexo == 'f':
    peso_ideal = ((62.1 * altura) - 44.7)
else:
    peso_ideal = ((72.7 * altura) - 58.0)

diferenca = peso - peso_ideal
percentagem = (abs(diferenca) / peso_ideal) * 100

print(f'Nome: {nome}')
print(f'Sexo: {sexo}')
print(f'Altura: {altura}m')
print(f'Peso atual: {peso}Kg')
print(f'Peso ideal: {peso_ideal}Kg')

if diferenca > 0:
    print(f'Você precisa emagrecer {diferenca:2f}Kg.')
    print(f'Você está {percentagem:2f}% acima do peso ideal.')
    if (peso / (altura*altura)) > 30:
        print('Atenção: peso muito acima do ideal.')
        print('Você foi classificado como obeso')
    elif diferenca < 0:
        print('Você precisa engordar ',abs(diferenca),'Kg')
        print(f'Você está {percentagem}% abaixo do ideal.')
    else:
        print('O seu peso atual está ideal para a sua altura!')
