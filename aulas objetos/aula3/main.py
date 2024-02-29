import json

CAMINHO_ARQUIVO = "AulaJson.json"

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 22)
p3 = Pessoa('Mário', 11)

bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w',  encoding='Utf-8') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
        
if __name__ == '__main__':
    fazer_dump()