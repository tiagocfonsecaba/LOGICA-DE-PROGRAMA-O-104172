import os
os.system ("cls")

nota = float (input("Digite sua nota entre 0 e 10: "))

while True:
    if nota < 0 or nota > 10:
        print ("Nota invalida.")
        print ("Tente novamente. \n")

    else:
        print (f'Nota: {nota}')
        break