# Como adicionar um elemento em uma posição específica?

# .append() Adiciona um item ao final da lista.
# lista = [1, 2]
# lista.append(3) [1, 2, 3]

# .extend() Adiciona todos os elementos de outra lista
# lista = [1]; lista.extend([2, 3]) [1, 2, 3]

diversos = [1, 'banana', 'mouse', 23.5, 'aciou', True, [1,2,3,5]]

diversos.append(5)
print(diversos)

diversos.extend([4])
print(diversos)