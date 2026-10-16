import os
os.system ("cls")

# Inicializa o vetor (lista) vazio
vetor = []

print("Digite 5 números:")

# Loop para receber os 5 valores do usuário
for i in range(5):
    valor = float(input(f"Digite o {i+1}º número: "))
    
    # Condição: se for negativo, atribui o valor 0
    if valor < 0:
        valor = 0
        
    # Adiciona o valor ao vetor
    vetor.append(valor)

# Exibe os valores armazenados no vetor
print("\nValores armazenados no vetor:")
for i, valor in enumerate(vetor):
    print(f"Posição {i}º: {valor}")