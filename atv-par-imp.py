import os
os.system("cls")

def calculo_par(numero):
    if numero% 2==0:
        resultado = "O numero é par"

    else:
        resultado = "O numero é impar!"
        return resultado

print("SOLICITANDO DADOS:")

numero=float(input("Digite um numero: "))
resultado = calculo_par(numero)

if numero% 2==0:
    print ("O numero é par")
else:
    print("O numero é impar!")

print ("= EXIBINDO DADOS =")
print(resultado)

