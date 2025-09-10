# 1. Identificação de número positivo, negativo ou zero.
# Crie um código em Python que leia e informe se o número é positivo ou negativo.

# 1) Entrada de dados
número = int(input("Digite um número inteiro: "))
# 2) Condicional para checar se o número é zero.
if número >= 0:
    if número == 0:
        print("O Número digitado é zero.")
    else: # informa que o número é positivo.
        print(f"O Número {número} é positivo.")
else: # # Se o if for falso, entra no else e, informa que o número é negativo.
    print(f"O Número {número} é negativo.")