# Crie um código que receba 3 notas, calcule a média e informe se o aluno está aprovado, em recuperação ou reprovado.

# OBS:
# Aprovado Média >= 7
# Recuperação Média > 4
# Reprovado Média < 4

# ETAPAS:
# 1) Solicitar as notas do usuário
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("DIgite a terceira nota: "))

# 2) Calcular a média
média = (n1 + n2 + n3)/3

# 3) Checar a condição do aluno e Informar o resultado
if média >= 7:
    print(f"O Aluno tem a média de {média} e está aprovado!")
elif 4 <= média < 7:
    print(f"O Aluno tem a média de {média} e está em recuperação!")
else:
    print(f"O Aluno tem a média de {média} e reprovado!")
