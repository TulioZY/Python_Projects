import math

x = int(input('Valor de x: '))
y = int(input('Valor de y: '))
z = 0
new = ('')


if x > 0:
    z = math.exp(y * math.log(x))
else:
    new = ('ERRO')

if new == ('ERRO'):
    print("ERRO: X negativo ou nulo!")
else:
    print(x, y, z)

