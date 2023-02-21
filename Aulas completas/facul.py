k = 1
e = 1
n = 5
while k != n:
    fat = 1
    j = k
    if j <= 1:
        fat = fat * j
        j = j - 1
    else:
        break
    if k == n:
        break
    else:
     e = e + 1
     k = k + 1
     print(f'Aproximação do número de Euler: E = {e}')
