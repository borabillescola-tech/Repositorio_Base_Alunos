# Utilizamos o try/except para apresentar uma exceção
# de uma maneira mais amigável ao usuário

try: # O código tenta executar o comando
    resultado = 10/0
except: # caso não consiga, ele executa o except
    print("Não é possível dividir por zero.")