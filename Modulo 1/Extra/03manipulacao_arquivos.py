# Criar um arquivo chamado mensagem.txt e escrever uma frase

with open('mensagem.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Python facilita a vida!')
    