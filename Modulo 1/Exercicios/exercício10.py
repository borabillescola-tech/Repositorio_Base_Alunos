# Crie um código Python, utilizando o match case
# Solicite ao usuário o tipo desejado de pizza e informe o preço

print("Menu de Pizzas")
print("1- Margherita")
print("2- Frango com Catupiry")
print("3- Quatro Queijos")
print("4- Pepperoni")
print("5- Portuguesa")
print("6- Calabresa")

pizza = int(input("Digite o número da pizza desejada: "))

match pizza:
    case 1:
        print("Margherita: R$60,00")
    case 2:
        print("Frango com Catupiry: R$68,00")
    case 3:
        print("Quatro Queijos: R$65,00")
    case 4:
        print("Pepperoni: R$62,00")
    case 5:
        print("Portuguesa: R$68,00")
    case 6:
        print("Calabresa: R$62,00")
    case _:
        print("Opção inválida.")