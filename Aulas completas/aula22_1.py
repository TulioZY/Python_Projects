chave = "perfume"
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print("Você perdeu!!!")
        break

    letra = input("Digite uma letra: ")
    if len(letra) < 1:
        print("Digita uma letra só ne garaio ta de trotos")
        continue

    digitadas.append(letra)

    if letra in chave:
        print(f'Ae porra a letra {letra} ta na palavra gg')
    else:
        print(f'Carai q burro, {letra} n existe nessa caraia aq n mano')
        digitadas.pop()

    chave_temp = ''

    for letra_chave in chave:
        if letra_chave in digitadas:
            chave_temp += letra_chave
        else:
            chave_temp = '*'

    if chave_temp == chave:
        print("gg ganhou o jogo parabens mas fodase")
        break
    else:
        print(f"a palavra ainda ta assim mano {chave_temp}, agiliza ai")

    if letra not in chave:
        chances = chances - 1

    print(f"Tu ainda tem {chances} chances parsa")
    print()