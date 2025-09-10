# Se o valor da compra for maior que R$150,00, aplique um desconto de R$20,00. Caso contrário, não aplique desconto.

valor_compra = float(input("Digite o valor da compra: R$ "))
if valor_compra > 150:
    valor_final = valor_compra - 20
    print(f"Desconto aplicado! Valor final: R$ {valor_final:.2f}")
else:
    valor_final = valor_compra
    print(f"Sem desconto. Valor final: R$ {valor_final:.2f}")