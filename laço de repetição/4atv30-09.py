import os
os.system("cls")

login = "1234"
senha = "1234"

quantidade_tentativas = 3
for i in range(quantidade_tentativas):

    print("\n== Faça seu login ==")
    print(f"Você tem {quantidade_tentativas} tentativas restantes.")
    login = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")

    
    if login == login and senha == senha:
        print("\n login aceito.")
        break
    else:
        print("Login ou senha invalidos tente novamente.")
        input("Pressione uma tecla para continuar...")

    

        os.system("cls")