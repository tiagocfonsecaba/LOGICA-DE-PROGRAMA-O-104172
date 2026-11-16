import os
os.system ("cls")

vetor_notas =[]
QUANTIDADE_NOTAS = 3

print("= Inserindo Notas =")


def lendo_notas(notas):
  media = sum (vetor_notas) / QUANTIDADE_NOTAS
  




for i in range (QUANTIDADE_NOTAS):
    nota = float (input (f"digite a {i+1}ª nota: "))
    vetor_notas.append(nota)


media = sum (vetor_notas) / QUANTIDADE_NOTAS


print ('\n = EXIBINDO A MEDIA =')
print (f"{media}")