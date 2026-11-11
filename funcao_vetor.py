import os
os.system("cls")

lista_produtos = []

def solicitar_dados():
    for i in range(3):
        produto= input("Digite o nome do produto: ")
        lista_produtos.append(produto)

def mostar_dados (lista_produtos):
    for i in range (3):
        print(f'{i+1} - {lista_produtos[i]}')


print("= SOLICITANDO DADOS =")
for i in range(3):
    produto = input("Digite o nome do produto: ")
    lista_produtos.append(produto)

    print ("\n= Exibindo Dados = ")
    mostar_dados(lista_produtos)