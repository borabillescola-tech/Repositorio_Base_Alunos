# contar quantas linhas tem no arquivo

with open('pessoa.txt','r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
# Aqui estamos lendo o arquivo e armazenando a leitura na variável linhas
    print('Total de linhas: ', len(linhas))
# A função len() conta quantas linhas tem no arquivo lido

