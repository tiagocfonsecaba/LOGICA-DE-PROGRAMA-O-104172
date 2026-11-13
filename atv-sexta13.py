import os
os.system ("cls")

def logo_senai():
    os.system("cls")
    print ("================")
    print  ("SENAI - BAHIA")
    print ("================")


def mostrar_dados(nome,idade):
    print(f'{nome} tem {idade}anos.')

#função sem retorno
logo_senai()
print("\n= SOLICITANDO DADOS =")
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

logo_senai()
print("\n= EXIBINDO DADOS =")
#FUNÇÃO SEM RETORNOS E COM PARÂMETROS
mostrar_dados(nome,idade)






