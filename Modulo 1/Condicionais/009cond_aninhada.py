dia = int(input("Digite um número de 1 a 7: "))

match dia:
    case 2|3|4|5|6:
        print("Ainda não é final de semana.")
    case 1|7:
        print("Chegou o final de semana.")
    case _:
        print("Número inválido.")