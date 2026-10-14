import os
os.system ("cls")

print ("= Insira Numeros  =")

vetor_notas =[]
QUANTIDADE_NOTAS = 5

for i in range (QUANTIDADE_NOTAS):
    nota = float (input (f"digite a {i+1}ª nota: "))
    vetor_notas.append(nota)



menor_nota = min (vetor_notas)
maior_nota = max (vetor_notas)




print ('\n = EXIBINDO NOTAS =')

for posicao,nota in enumerate (vetor_notas,start=1):
        print (f"{posicao}ª: nota {nota}")



print("\n = Exibindo Notas:")
print (f"Menor nota: {menor_nota}")
print (f"Maior nota: {maior_nota}")

