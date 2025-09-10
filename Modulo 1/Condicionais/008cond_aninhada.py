# Crie um código pytohn que solicite ao usuário um produto e informe o preço

print("Menu de Produtos")
print("1 - Café")
print("2 - Chá")
print("3 - Suco")
print("4 - Refrigerante")
print("5 - Água")

codigo = int(input("Digite o código do produto: "))

match codigo:
    case 1:
        print("Café: R$ 36,90")
    case 2:
        print("Chá: R$ 9,50")
    case 3:
        print("Suco: R$ 14,50")
    case 4:
        print("Refrigerante: R$ 10,50")
    case 5:
        print("Água: R$ 8,90")
    case _:
        print("Produto não encontrado")