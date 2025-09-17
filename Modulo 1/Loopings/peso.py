# Crie um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lido.

# Etapas para resolução:
# Crie uma lista vazia para receber os pesos.
# Crie um for para receber os pesos das 5 pessoas.
# Adicione os pesos recebidos à lista.
# Utilize as funções max() e min() ou ordene a lista e busque o primeiro e o último elemento.
# Apresente os resultados.

pesos = []
for i in range(5):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa (kg): "))
    pesos.append(peso)
maior_peso = max(pesos)
menor_peso = min(pesos)
print(f"O maior peso lido foi: {maior_peso} kg")
print(f"O menor peso lido foi: {menor_peso} kg")