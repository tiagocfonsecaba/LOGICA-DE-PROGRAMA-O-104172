import os
from datetime import date
os.system ("cls")


codigo = int (input ("Digite seu codigo: "))
ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
tempo_de_trabalho= float (input ("Digite seu tempo de trabalho: "))
idade = date.today().year - ano_de_nascimento


if  idade >= 65 and tempo_de_trabalho >= 30:
    print ("você pode se aposentar")

else:
    print("Você nao pode se aposentar")

