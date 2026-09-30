import os
os.system("cls")

login = "1234"
senha = "1234"


while True:
    print("\n== Faça seu login ==")
    usuario = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    
    if usuario == login and senha == senha:
        print("\n login aceito.")
        break  
    else:
        print("Login ou senha invalidos tente novamente.\n")
        input("Pressione uma tecla para continuar...")

        os.system("cls")