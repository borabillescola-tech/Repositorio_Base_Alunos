# Peça um número ao usuário e verifique se ele é múltiplo de 5. Se for, exiba "Múltiplo de 5", senão exiba "Não é múltiplo de 5".

numero = int(input("Digite um número: "))
if numero % 5 == 0:
    print("Múltiplo de 5")
else:
    print("Não é múltiplo de 5")