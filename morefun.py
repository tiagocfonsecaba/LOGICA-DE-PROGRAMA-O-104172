import os
os.system ("cls")





def logo_senai():
  print("=" * 15)
  print("  SENAI-BAHIA")
  print("=" * 15)


def mostrar_dados(nome, email, telefone):
  print(f"Nome: {nome}")
  print(f"E-mail: {email}")
  print(f"Telefone: {telefone}")


# --- Início do Programa ---
os.system("cls")  # Limpa o terminal (use 'clear' se estiver no Linux/Mac)
logo_senai()

print("\n= SOLICITANDO DADOS =")
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone: ")

os.system("cls")  # Limpa a tela novamente para mostrar só o resultado final
logo_senai()
mostrar_dados(nome, email, telefone)
