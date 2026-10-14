import os
os.system ("cls")

print ("= Enumerando Notas=")
vetor_nota = []

for i in range (3):
    nota = float(input(f"Digite a {i+1} sua nota: "))
    vetor_nota.append(nota)

for indice in enumerate (vetor_nota,start=1):
        print (f"Nota: {indice}")