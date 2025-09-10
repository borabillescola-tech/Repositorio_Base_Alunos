# 2. Paridade e Tamanho do número

# Crie um código que receba um número inteiro e informe:
# - se é par ou ímpar
# - e, ao mesmo tempo, se é maior que 10 ou menor ou igual a 10.
# Utilize condicionais aninhadas para organizar as verificações.

número = int(input("Digite um número inteiro: "))

if número % 2 == 0:
    if número >= 10:
        print("O Número informado é par e maior que 10.")
    else:
        print("O Número informado é par e menor, ou igual, a 10.")
else: 
    if número < 10:
        print("O Número informado é impar e menor que 10." )
    else: 
        print("O Número informado é impar e menor, ou igual, a 10.")



