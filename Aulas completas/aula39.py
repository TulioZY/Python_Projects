try:
    a = []
    print(a)
except NameError as erro:
    print('Erro do desenvolvedor.')
except (IndexError, KeyError) as erro:
    print('Erro de indice')
except Exception as erro:
    print('Erro inesperado.')
else:
    print('Seu código foi executado com sucesso')
finally:
    print("fecha saporra")
print('oi')