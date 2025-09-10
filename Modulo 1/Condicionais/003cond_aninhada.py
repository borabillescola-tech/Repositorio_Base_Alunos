# 3. Classificação por idade
# Faça um programa que leia a idade de uma pessoa e classifique-a em:
# Criança: menor que 12 anos.
# Adolecente: entre 12 e 17 anos.
# Adulto: maior ou igual a 18 anos.
# Utilize a estrutura de condicional aninhada

idade = int(input("Informe a idade a sua idade: "))

if idade > 0:
    if idade >= 18:
        print(f"Você tem {idade} anos e é um adulto.")
    elif 12 <= idade <=17:
        print(f"Você tem {idade} anos e é um adolescente.")
    else:
        print(f"Você tem {idade} anos e é uma criança.")
else:
    print("Sua idade não pode ser negativa, digite uma idade válida.")
