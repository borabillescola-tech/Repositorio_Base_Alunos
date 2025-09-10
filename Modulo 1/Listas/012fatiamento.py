# Como fatiar uma lista?
# Podemos extrair "pedaços" de uma lista utilizando o fatiamento.

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letras[2:5]) # Do índice 2 ao 4 (5-1)
print(letras[:5])  # Do início ao índice 4 (5-1)
print(letras[5:])  # Do índice 5 até o final
print(letras[::2]) # Do início ao fim, pulando de 2 em 2
print(letras[::-1])# Inverte a lista
print(letras[-3:]) # Últimos 3 elementos
print(letras[:-3]) # Todos menos os últimos 3 elementos
print(letras[-5:-2]) # Do 5º elemento a partir do fim até o 3º elemento a partir do fim

