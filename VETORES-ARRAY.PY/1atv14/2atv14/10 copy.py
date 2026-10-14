import os
os.system ("cls")

print ("= Inserindo Notas no vetor=")

vetor_notas =[]
QUANTIDADE_NOTAS = 2

for i in range (QUANTIDADE_NOTAS):
    nota = float (input (f"digite a {i+1}ª nota: "))
    vetor_notas.append(nota)

media = sum (vetor_notas) / QUANTIDADE_NOTAS


print ('\n = EXIBINDO NOTAS =')

for posicao,nota in enumerate (vetor_notas,start=1):
        print (f"{posicao}ª: nota {nota}")
        print (f"{media}")