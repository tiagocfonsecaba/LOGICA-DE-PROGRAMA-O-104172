import os
os.system("cls")




def calc_positivo_negativo(numero):
    if numero > 0:
        resultado = "Positivo"
    elif numero < 0:
        resultado = "Negativo"
    else:
        resultado = "Neutro"
    return resultado


print("= SOLICITANDO DADOS =")
numero = float(input("Digite um número: "))
resultado = calc_positivo_negativo(numero)
print(f"Resultado: {resultado}")
