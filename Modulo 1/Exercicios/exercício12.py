# Uma empresa de vendas deseja automatizar o cálculo de bônus de seus vendedores.
# Cada vendedor recebe um bônus de 10% sobre o total das vendas. Desde que tenha:
# 1. Alcançado mais de R$10.000,00 em vendas no mês
# 2. Trabalhado pelo menos 20 dias úteis no mês
# Se não atender a essas condições, o bônus será de apenas 3% das vendas.

# Crie um código que receba como entrada:
# 1. O nome do funcionário
# 2. O valor total das vendas do mês
# 3. O número de dias úteis trabalhados
# Calcule o valor do bônus conforme as regras acima.
# Exiba uma mensagem com:
# 1. O nome do funcionário
# 2. O valor das vendas
# 3. Os dias trabalhados
# 4. O valor do bônus

nome = input("Digite o nome do funcionário: ")
vendas = float(input("Digite o valor total das vendas do mês: "))
dias_trabalhados = int(input("Digite o número de dias úteis trabalhados: "))

if vendas > 10000 and dias_trabalhados >= 20:
    bonus = vendas * 0.1
else:
    bonus = vendas * 0.03

print(f"Funcionário: {nome}")
print(f"Vendas: R${vendas:.2f}")
print(f"Dias trabalhados: {dias_trabalhados}")
print(f"Bônus: R${bonus:.2f}")