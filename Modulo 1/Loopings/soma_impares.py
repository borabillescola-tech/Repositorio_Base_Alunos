# Crie um programa que some todos os números ímpares que são multiplos de 3 e 1 a 500 e apresente o resultado.

# Etapas para resolução:
# Criar um for para captar os números ímpares
# Criar uma condicional para checar se o número é múltiplo de 3
# Somar os números que atenderem a condição
# Apresentar o resultado

soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
print(f"A soma dos números ímpares múltiplos de 3 entre 1 e 500 é: {soma}")
