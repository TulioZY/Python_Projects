"""
While com else em python
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5: #faz parar o codigo antes de chegar no else
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Terminou.')
print('Isso mostra')