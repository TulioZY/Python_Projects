"""
Operador ternário em python
"""

logged_user = False
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'


idade = input("Qual sua idade? ")
if not idade.isnumeric():
    print("Somente numeros")
else:
    idade = int(idade)
    maior = (idade>=18)
    msg = 'Pode acessar' if maior else 'Vaza kid'
    print(msg)

nome = input("teu nome??")
print(nome or 'Digitou nada carai')
