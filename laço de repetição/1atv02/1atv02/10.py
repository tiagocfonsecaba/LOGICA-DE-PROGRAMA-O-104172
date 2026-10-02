import os

os.system("cls")

soma = 0
quantidade_notas = 2

print("   Média das Notas\n   ")

for i in range(quantidade_notas):
 while True:
       
    nota = float(input(f"Digite a {i + 1}ª nota entre 0 e 10: "))
    if 0 <= nota <= 10:
      soma = soma + nota
      break
    else:
      print()
      print("Nota inválida.\nTente novamente.\n")
    
media = soma / quantidade_notas
print(f"A média das notas é: {media}")
print("=fim=")