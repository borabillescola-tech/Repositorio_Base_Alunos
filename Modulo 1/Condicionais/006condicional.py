# Crie um código python que peça o valor da sua conta. Se for maior que R$100.00, adicione uma gorjeta de 10% e exiba o total a pagar.
# Caso contrário, adicione uma gorjeta de 5%.

# Etapas para Resolução:
# 1) Solicitar o valor da conta para o usuário 
# 2) Se a conta for maior que 100, adicionar 10% de gorjeta e apresentar o total a pagar
# 3) Se a conta for menor que 100, adicionar 5% de gorjeta e apresentar o total a pagar

valorconta = float(input("Digite o valor da conta: "))
if valorconta >= 100.00:
    gorjeta = valorconta * 0.10
else:
    gorjeta = valorconta * 0.05
totalconta = valorconta + gorjeta
print(f"O Valor a ser pago é de R${totalconta :2f}")