toler = 0.000001
a = 12
p = 0
if a <= 0:
    a = 121
if p < 2:
    p = 2
z = a
i = 0
print(i, z)
x = 0
while x <= 0:
    x = ((p - 1) * z + a / (z ^ (p - 1))) * 1 / p
    delta = (x - z)
    i = i + 1
    print((i),x,delta)
    if (delta <= toler) or i == 50:
        break
    z = x

if (delta > toler):
    print('processo não convergiu com 50 iterações')
else:
    print(a,x)
