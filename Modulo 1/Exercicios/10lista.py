# copy()
# Dada a lista original = [1, 2, 3, 4], use .copy() para criar uma nova lista
# chamada copia. Altere a copia (adicione o número 99) e mostre as duas listas
# para verificar que são independentes.

original = [1, 2, 3, 4] # lista original
copia = original.copy() # criando a copia
copia.append(99) # alterando a copia

print("Original:", original) # mostrando a lista original
print("Copia:", copia) # mostrando a copia