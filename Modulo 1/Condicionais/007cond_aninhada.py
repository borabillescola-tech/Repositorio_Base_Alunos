# Crie um programa que:
# Peça ao usuário que digite um número de 1 a 7 para indicar os dias da semana
# Use match case para exibir o nome correspondente ao número:
# 1- Domingo 2- Segunda 3- Terça 4- Quarta 5- Quinta 6- Sexta 7- Sábado

dia = int(input("Digite um número de 1 a 7: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido.")