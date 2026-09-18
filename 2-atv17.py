import os
os.system ("cls")



nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").upper()
estado_civil = input("Digite o estado civil: ").upper()

if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Há quantos anos você é casada? "))

print("\n--- Dados do usuário ---")
print("Nome:", nome)
print("Sexo:", sexo)
print("Estado civil:", estado_civil)

if sexo == "F" and estado_civil == "CASADA":
    print("Tempo de casada:", tempo_casada, "anos")