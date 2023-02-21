"""
Funções - def em Python
"""
def partiu():
    print("eae parsa")
    print("belesa?")
    print("tmjjjj")
partiu()

def saudacao(msg="Olá", nome="Usuário."):
    print(msg, nome)
saudacao()
saudacao('Hello', 'Jorgin')

def teste(msgg="Olá", nomee="Usuário."):
    return f'{msgg, nomee}'

variavel = teste()
print(variavel)

def divisao(n1, n2):
    return n1 / n2
divide = divisao(8,4)
print(divide)

