# Crie um código Python, utilizando match case
# Um código que analise as notas dos alunos
# Peça ao usuário 4 notas, calcule a média e classifique a média em:
# 0 a 4 = reprovado
# 5 a 6 = recuperação
# 7 a 10 = aprovado

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

match media:
    case media if media < 5:
        print(f"Sua média é de {media} e você está Reprovado")
    case media if 5 <= media < 7:
        print(f"Sua média é de {media} e você está de Recuperação")
    case media if 7 <= media <= 10:
        print(f"Sua média é de {media} e você está Aprovado")
    case _:
        print(f"Média inválida.")
