import os
os.system ("cls")

print ("= Insira Numeros  =")
vetor_numeros=[]
QUANTIDADE_NUMEROS= 6
pares = 0
impares = 0


for i in range(QUANTIDADE_NUMEROS):
        numero = float(input(f"Digite o {i+1}º numero: "))
        vetor_numero.append(numero)
        if numero %2 == 0:
                pares +=1
        else:
                imapres +=1




print ('\n = EXIBINDO NOTAS =')

for posicao,numero in enumerate (vetor_numeros,start=1):
        print (f"{posicao}ª: nota {numero}")

        print ("\n= Impartes e Pares do vetor = ")
        print (f"Quantidade de pares{pares}")
        print (f"Quantidade de impares {impares}")






