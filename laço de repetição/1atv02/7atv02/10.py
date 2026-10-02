import os
os.system ("cls")

soma = 0
quantidade_notas = 3


for i in range(quantidade_notas):
    while True:
        nota = float(input(f"Digite a  {i + 1}ª nota entre 0 e 10: "))
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            break
        elif nota 
        else:
            print()
            print("Nota inválida. Tente novamente")

            media = soma / quantidade_notas


            print(f"A média das notas é: {media}")
            print ("=fim=")