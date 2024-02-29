import json
from main import CAMINHO_ARQUIVO, Pessoa, fazer_dump


with open(CAMINHO_ARQUIVO, 'r', encoding='Utf-8') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p3 = Pessoa(**pessoas[1])
    p2 = Pessoa(**pessoas[2])
    print(p1.nome)
    print(p2.nome)
    print(p3.nome)