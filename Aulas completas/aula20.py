frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_frase = ''

input_do_usuario = input('Qual letra deseja ver maiúscula? ')
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_frase += input_do_usuario.upper()
    else:
        nova_frase += letra
    contador += 1

print(nova_frase)
    # print(frase[contador], contador)
#     nova_frase += frase[contador]
#     print(nova_frase)
#     contador += 1
# print(nova_frase)
