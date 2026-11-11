import os
os.system("cls")



def tabuada(numero):
  print(f"\n--- Tabuada do {numero} ---")
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")



numero = int(input("Digite um número para ver a tabuada: "))
tabuada(numero)

