import os
os.system ("cls")

A = int(input("Digite o numero 1. "))
B = int(input("Digite o numero 2. "))
operacao = input("Digite a operação (+, -, *, /): ")

match operacao:
    case '+':
        resultado = A + B
        print(f"Resultado: {A} + {B} = {resultado}")
    case '-':
        resultado = A - B
        print(f"Resultado: {A} - {B} = {resultado}")
    case '*':
        resultado = A * B
        print(f"Resultado: {A} * {B} = {resultado}")
    case '/':
    
        resultado = A / B
        print(f"Resultado: {A} / {B} = {resultado}")

        
    case _:
        print("Operação inválida.")

