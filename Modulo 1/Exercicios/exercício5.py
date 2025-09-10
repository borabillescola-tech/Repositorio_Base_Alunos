# Peça o valor da conta. Se for maior que R$100,00, adicione uma gorjeta de 10% e exiba o total a pagar. Caso contrário, adicione uma gorjeta de 5%.

valorconta = float(input("Digite o valor da conta: "))
if valorconta >= 100.00:
    gorjeta = valorconta * 0.10
else:
    gorjeta = valorconta * 0.05
totalconta = valorconta + gorjeta
print(f"O Valor a ser pago é de R${totalconta :2f}")
