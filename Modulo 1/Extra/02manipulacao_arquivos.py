# ler um arquivo

arquivo = open('pessoa.txt','r', encoding='utf-8') # 'r' de read (ler o arquivo)
conteudo = arquivo.read()
print(conteudo)
arquivo.close()