"""
for in em Pyton
iterando strings com for
função range(start=0, stop, step=1)
"""

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)

#for letra in texto:
    #print(letra)

#for n in range(10):
    #print(n)

"""
c = 0
while c < len(texto):
    print(texto[c])
    c = c + 1
"""

