# 1. Peça dois números ao usuário. Se forem diferentes, exiba "Os números são diferentes", caso contrário, exiba "Os números são iguais".

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 != numero2:
    print("Os números são diferentes")
else:
    print("Os números são iguais")