# Crie um código que faça a conversão de moedas do real para o dólar e vice-versa.

# Etapas para a resolução:
# Criar uma variável chamada cotacao
# Solicitar ao usuário a opção de conversão desejada
# Apresentar o resultado da conversão de moedas
# Perguntar se ele deseja continuar a conversão

letra = 's'
while letra == 's':
    cotacao = float(input("Digite a cotação do dólar hoje: "))
    opcao = int(input("Escolha a opção de conversão:\n1- Real para Dólar\n2- Dólar para Real\nOpção: "))
if opcao == 1:
    real = float(input("Digite o valor em Real (R$): "))
    dolar = real / cotacao
    print(f"O valor de R${real:.2f} convertido para Dólar é: US${dolar:.2f}")
elif opcao == 2:
    dolar = float(input("Digite o valor em Dólar (US$): "))
    real = dolar * cotacao
    print(f"O valor de US${dolar:.2f} convertido para Real é: R${real:.2f}")
else:
    print("Opção inválida. Tente novamente.")
letra = input("Deseja fazer outra conversão? [s/n]: ").lower()