#nome = 'Tulio'

#if 'l' not in nome:
 #   print('Tomanocu memo ne')
#else:
 #   print('Boa cara isso msm')


usuario = input('Login: ')
senha = input('Senha: ')

usuario_bd = 'tuliotcr'
senha_bd = '12345'

if usuario == usuario_bd and senha == senha_bd:
    print('Login efetuado com sucesso.')
else:
    print('Login ou senha incorretos.')
