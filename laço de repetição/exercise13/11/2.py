import os
os.system("cls")


def soma_numeros(numero_1,numero_2):
    resultado= (numero_1 + numero_2)
    return resultado

def subtracao(numero_1,numero_2):
    resultado= (numero_1 - numero_2)
    return resultado

def multiplicacao(numero_1,numero_2):
    resultado= (numero_1 * numero_2)
    return resultado

def divisao(numero_1,numero_2):
    resultado= (numero_1 / numero_2)
    return resultado



    print("= SOLICITANDO DADOS = ")

numero_1 = float(input("Digite o nº1: "))
numero_2 = float(input("Digite o nº2: "))



soma= numero_1 + numero_2
multiplicacao=numero_1 * numero_2
divisao=numero_1 / numero_2
subtracao=numero_1 - numero_2

print ("= EXIBINDO DADOS =")

print(f'A soma é  {soma}')
print(f'A subtração é {subtracao}')
print(f'A multiplicação é {multiplicacao}')
print(f'A divisão é {divisao}')

