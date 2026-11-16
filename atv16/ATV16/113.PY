import os
import time
os.system('cls')

# Pega o ano atual do sistema
ano_atual = time.localtime().tm_year



#dade.today para pegar a data do dia
def calculo_de_idade(ano_nascimento):
  # A conta correta é: Ano Atual menos o Ano de Nascimento
  calculo = ano_atual - ano_nascimento
  return calculo


# Converte a entrada para inteiro (int) em vez de float
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

# Passa o ano_nascimento como argumento para a função
idade = calculo_de_idade(ano_nascimento)

print(f"Sua idade é {idade}")
