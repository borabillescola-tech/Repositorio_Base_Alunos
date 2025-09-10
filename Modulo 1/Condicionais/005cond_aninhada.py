# Peça ao usuário para digitar uma letra
# Se for vogal, informe qual vogal.
# Se for consoante, verifique se é maiúscula ou minúscula

# Solicitação de entrada de dados do tipo String (texto)
letra = input("Digite uma letra: ")

if letra.lower() in "aeiou": # .lower() transforma em minúscula
    print(f"Vogal: {letra}")
else:
    if letra.isupper(): # isupper identifica se a letra está em maiúsculo
        print(f"Consoante Maiúscula: {letra}")
    else:
        print(f"Consoante Minúscula: {letra}")
