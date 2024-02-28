caminho = 'C:\\Users\\tulio\\OneDrive\\Documentos\\Programação\\Python\\Python_Projects\\Aulas completas\\'
caminho += 'aula116.txt'

# Utilizando 'a' invés de 'w' é possível escrever no arquivo sem apagar o conteúdo anterior
with open(caminho, 'w+', encoding='utf-8') as arquivo:
    arquivo.write('ola\n')
    arquivo.write('dboa?\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
        )
    arquivo.seek(0, 0)
    print(arquivo.read())
    
with open(caminho, 'r') as arquivo:
    print(arquivo.read())