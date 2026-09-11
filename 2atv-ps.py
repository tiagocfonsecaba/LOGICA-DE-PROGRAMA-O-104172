import os
os.system ("cls")



nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (H para homem e M para mulher): ")
estado_civil = input("Digite seu estado civil (S para solteiro e C para casado): ")
anos_de_casado = input("Digite os anos de casamento: ")



if estado_civil == "C" and sexo == "M":
    print(f"{nome} | {estado_civil} | {sexo} | {anos_de_casado}")