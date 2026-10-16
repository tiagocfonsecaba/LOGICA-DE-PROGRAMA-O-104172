import os
os.system ("cls")

print ("Inserindo numeros")

quantidade_negativos = 0
vetor_numeros = []
soma_positivos = 0

for i in range(5):
    numero= float(input(f'digite o {i+1}ºnumero: '))
    vetor_numeros.append(numero)
    for num in vetor_numeros:
        if numero < 0:
            quantidade_negativos += 1
        elif numero > 0:
            soma_positivos += numero

print ("EXIBINDO NUMEROS")
print (f"quantidade de numeros negativos{quantidade_negativos}")
print (f"quantidade de numeros positivos {soma_positivos}")

