def somatoria(n1, n2, n3):
    return n1 + n2 + n3
soma = somatoria(1, 2, 3)
print(soma)

def somaporcentagem(n1, n2):
    test = n1*(n2/100)
    soma = n1 + test
    return soma
print (somaporcentagem(500,20))

def fizzbuzz(n1):
    if n1%3==0 and n1%5 == 0:
        return "FizzBuzz"
    if n1%3==0:
        return "Fizz"
    if n1%5==0:
        return "Buzz"
    return n1
print(fizzbuzz(15))
