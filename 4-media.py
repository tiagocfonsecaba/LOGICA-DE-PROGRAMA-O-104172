import os

# limpa o terminal
os.system ('cls')

print ('=SOLICITANDO DADOS=')
nome = input ("Digite seu nome: ")
idade = int (input("Digite sua idade: "))
primeira_nota = float(input("Digite a primeira nota:  "))
segunda_nota = float (input("Digite a segunda nota:  "))

media  =  (primeira_nota + segunda_nota) / 2

print ('\n=EXIBINDO  DADOS=')
print ("nome: ", nome)
print ("idade: ", idade)
print ("primeira_nota: ", primeira_nota)
print ("segunda_nota: ", segunda_nota)
print ("média: ", media)


