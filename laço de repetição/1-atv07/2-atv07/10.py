import os
os.system ("cls")

# Inicialização das variáveis de contagem e soma
qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_geral = 0
qtd_geral = 0

print("Digite os números  ( ou digite 0 para encerrar):")

# Laço de repetição que executa indefinidamente até encontrar o break
while True:
    numero = int(input("Informe um número: "))
    
    # Condição de parada do algoritmo
    if numero == 0:
        break
        
    # Validação para garantir que o número seja positivo
    if numero < 0:
        print("Por favor, digite apenas números positivos.")
        continue
    
    # Atualiza as estatísticas gerais
    soma_geral += numero
    qtd_geral += 1
    
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        qtd_pares += 1
        soma_pares += numero
    else:
        qtd_impares += 1

# Exibição dos resultados (com verificações para evitar divisão por zero)
print("\n--- RESULTADOS ---")
print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")

# Média dos valores pares
if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print(f"Média dos valores pares: {media_pares:.2f}")
else:
    print("Média dos valores pares: Nenhum número par foi digitado.")

# Média geral de números lidos
if qtd_geral > 0:
    media_geral = soma_geral / qtd_geral
    print(f"Média geral dos números lidos: {media_geral:.2f}")
else:
    print("Média geral dos números lidos: Nenhum número válido foi digitado.")
