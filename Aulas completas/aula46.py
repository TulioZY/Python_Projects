def generator (n = 0, maximun=0):
    while True:
        
        yield n
        n += 1
        
        if n > maximun:
            return
        
gen = generator (maximun=100000)
for n in gen:
    print(n)