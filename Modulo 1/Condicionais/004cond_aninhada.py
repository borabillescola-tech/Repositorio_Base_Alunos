# Tipo um triângulo
# Crie um programa que receba três lados de um triângulo.
# Verifique se os lados realmente podem formar um triângulo.
# E Determine os triângulos em:
# Equilátero (todos os lados são iguais)
# Isóceles (dois lados iguais)
# Escalêno (todos os lados diferentes)

a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b: "))
c = int(input("Digite o valor do lado c: "))

# Verificar se os lados formam um triângulo:
if a + b > c and a + c > b and b + c > a: # Condição para formação do triângulo.
    if a == b:
        if b == c:
            print(f"Os lados do triângulo são {a}, {b} e {c}: Triângulo Equilátero")
        else:
            print(f"Os lados do triângulo são {a}, {b} e {c}: Triângulo Isósceles")

    else: # Não é possível formar um triângulo.
        if b == c or a == c:
            print(f"Os lados do triângulo são {a}, {b} e {c}: Triângulo Isósceles.")
        else:
            print(f"Os lados do triângulo são {a}, {b} e {c}: Triângulo Escaleno.")
else:
    print("Os lados não formam um triângulo válido.")