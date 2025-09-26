# Criar um arquivo nomes.txt

nomes = ['João\n','Maria\n','Bill\n'] # Criamos uma lista com nomes para ser
# Inseridos no arquivo nomes.txt

with open('nomes.txt','w', encoding='utf-8') as arquivo:
	# estamos criando o arquivo
	arquivo.writelines(nomes) # Estamos pedindo para escrever
	
