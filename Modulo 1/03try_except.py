# Crie uma função chamada calculadora que receba três parâmetros:
# Dois numeros e uma operaçãop
# A função deve retornar o resultado da operação
# Mas precisa tratar as seguintes exceções:
# Divisão por zero(ZeroDivisionError)
# Tipo de dado inválido(ValueError)

def calculadora():
    try:
        n = input("Digite o primeiro número ou x para sair do sistema: ")
        if n.lower() == 'x':
            print("Saindo do sistema...")
            return
        n1 = input('Digite o primeiro número ou x para sair do sistema: ')
        if n1.lower() == 'x':
            print("Saindo do sistema...")
        operador = input("Digite a operação (+, -, *, /) ou x para sair do sistema: ")
        if operador.lower() == 'x':
            print("Saindo do sistema...")
            return
        
        # converter as entradas (inputs) em float
        n = float(n)
        n1 = float(n1)
        if operador == '+':
            resultado = n + n1
        elif operador == '-':
            resultado = n - n1
        elif operador == '*':
            resultado = n * n1
        elif operador == '/':
            resultado = n / n1
        else:
            print("Operação inválida.")
            return

        print(f"O resultado da operação {n} {operador} {n1} é: {resultado}")

    except ValueError:
        print("Erro: Tipo de dado inválido.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
calculadora()
