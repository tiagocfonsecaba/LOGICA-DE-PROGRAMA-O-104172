import os
os.system ("cls")

print ("= Esolha seu livro favorito =")

vetor_nome =[]

for i in range (5):
    nome = (input ("digite um nome de um livro: "))
    vetor_nome.append(nome)

    print ('\n = Lista de livros =')

    for indice in enumerate (vetor_nome,start=1):
        print (f"Livro escolhido: {indice}")