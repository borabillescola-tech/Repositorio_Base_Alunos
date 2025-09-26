# Criar aquivo e escrever dados do usuário

# Solicitação de entrada
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

# Criar arquivo
arquivo = open('pessoa.txt','a', encoding='utf-8') # 'a' de append (adicionar ao final do arquivo)
# 'w' de write (sobrescrever o arquivo) e encoding utf-8 para aceitar caracteres especiais

# Escrever dados no arquivo
arquivo.write(nome + '|' + email + '\n') # \n para pular linha
arquivo.close() # fechar o arquivo