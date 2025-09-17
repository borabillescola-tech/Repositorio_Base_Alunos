# Solicite ao usuário 4 notas.
# Calcule a média
# Informe se o aluno foi aprovado (media >=7), recuperação(5<media<7) ou reprovado.
# Apresente as notas que o aluno tirou, a media e o status de sua situação.

# lista
# for
# if/elif/else

notas = []
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    if nota > 0:
        notas.append(nota)
    else:
        print(f"Valor Inválido.")
print(f"Suas notas são: {notas}")
media = sum(notas) / len(notas)

if media >= 7:
    print(f"Sua média foi {media:.2f}. Você foi aprovado!")
elif 5 < media < 7:
    print(f"Sua média foi {media:.2f}. Você está de recuperação.")
else:
    print(f"Sua média foi {media:.2f}. Você foi reprovado.")