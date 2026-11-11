import os
os.system("cls")


def logo_senai():
    print("\n")
    print('=' *  15)
    print("  SENAI-BAHIA")
    print('='*  15)


logo_senai()

def mostrar_dados(nome, email, telefone):
    print(f"{nome} - {email} - {telefone}")


print("= SOLICITANDO DADOS =")
logo_senai()
nome = input("Digite seu nome: ")
logo_senai()
email = input("Digite seu email: ")
logo_senai()
telefone = input("Digite seu telefone: ")

logo_senai()
print("= EXIBINDO DADOS =")
mostrar_dados(nome, email, telefone)
