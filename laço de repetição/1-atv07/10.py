import os
os.system ("cls")

# Inicialização das variáveis
soma_notas = 0.0
contador = 0
deseja_continuar = 's'

# Laço de repetição
while deseja_continuar.lower() == 'n':
    # Solicita a nota ao usuário
    nota = float(input(f"Digite a {contador + 1}ª nota: "))
    
    # Acumula a nota e incrementa o contador de iterações
    soma_notas += nota
    contador += 1  # Contador exigido no enunciado
    
    # Pergunta se o usuário deseja continuar
    deseja_continuar = input("Deseja inserir mais uma nota? (s/n): ")

# Verifica se alguma nota foi inserida para evitar divisão por zero
if contador > 0:
    media = soma_notas / contador
    print(f"\nTotal de notas inseridas: {contador}")
    print(f"A média aritmética das notas é: {media:.2f}")
else:
    print("\nNenhuma nota foi informada.")