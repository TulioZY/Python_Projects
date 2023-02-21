num1 = input('Digite um número para somar: ')
num2 = input('Digite o outro número: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)

else:
    print('Vai digitar letra na casa do carai fi, rato branco')