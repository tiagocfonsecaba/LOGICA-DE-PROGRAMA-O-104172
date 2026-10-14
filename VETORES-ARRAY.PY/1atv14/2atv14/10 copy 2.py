import os
os.system ("cls")

print ("= Inserindo Notas =")

vetor_notas =[]
QUANTIDADE_NOTAS = 4

for i in range (QUANTIDADE_NOTAS):
    nota = float (input (f"digite a {i+1}ª nota: "))
    vetor_notas.append(nota)


media = sum (vetor_notas) / QUANTIDADE_NOTAS
menor_nota = min (vetor_notas)
maior_nota = max (vetor_notas)

if media >=7:
    print ("Aprovado!")
elif media<= 7 and media >= 5:
    print ("Recuperação!")

else:
    print ("Reprovado!")


print ('\n = EXIBINDO NOTAS =')

for posicao,nota in enumerate (vetor_notas,start=1):
        print (f"{posicao}ª: nota {nota}")
        print (f"sua media é: {media}")


print("\n = Exibindo Notas:")
print (f"Menor nota: {menor_nota}")
print (f"Maior nota: {maior_nota}")

