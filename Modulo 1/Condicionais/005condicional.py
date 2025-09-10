# Crie um código Python que verifique se a senha digitada pelo usuário for "1234", exiba "Acesso Permitido".

# Etapas para resolção:

# 1) Criar uma variável e atribuir a ela uma senha
# 2) Através de um input, solicitar a senha ao usuário
# 3) Através de uma condicional checar se a senha é igual a senha armazenada
# 4) Liberar, ou não, o acesso ao usuário

senha1 = "bumbumguloso"

senha = input("Digite a sua senha: ")

if senha == senha1:
    print("Acesso Liberado!")
else:
    print("Acesso Negado! Tente novamente.")