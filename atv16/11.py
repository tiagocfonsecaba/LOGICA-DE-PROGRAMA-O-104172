import os

os.system("cls")


def taxa_do_pecado(preco):
  if preco < 100:
    imposto = preco * 0.10
    return imposto
  elif preco >= 100:
    imposto = preco * 0.20
    return imposto


# Recebe o preço digitado pelo usuário
preco = float(input("Digite o preço do produto: "))

# Chama a função e guarda o resultado na variável 'imposto_calculado'
imposto_calculado = taxa_do_pecado(preco)

# Exibe o resultado na tela
print(f"O valor do imposto do amor é: R$ {imposto_calculado:.2f}")

# (Opcional) Exibindo o preço total com o imposto
preco_total = preco + imposto_calculado
print(f"O preço final com imposto do amor é: R$ {preco_total:.2f}")