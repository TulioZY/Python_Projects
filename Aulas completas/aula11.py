"""
Operadores relacionais
== - Igualdade
> - Maior que
>= - Maior ou igual que
< - Menor que
<= - Menor ou igual que
!= - é Diferente?
"""

nome = input('Qual é o seu nome meu parça? ')
idade = input('E quantos anos vc tem????? ')
idade_minima = 18
idade_maxima = 40
idade = int(idade)

if idade >= idade_minima and idade <= idade_maxima:
    print(f'Beleza {nome} vo te passar os link dos hentão brabo. Pega a visão:'
          'hentaihaven.com, hanime.tv')
    print('mas presta atenção, tua mae nunca podera saber dessa porra aq em')
    discord = input('Passa teu discord ai pra gente trocar uma ideia no chat dos confradecidos: ')
    print(f'vlw mano, o discord {discord} foi hackeado boa sorte!')

else:
    print('Sai fora parsa ta no lugar errado.')
