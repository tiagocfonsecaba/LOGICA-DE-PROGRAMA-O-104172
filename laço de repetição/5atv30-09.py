import os
os.system("cls")

login = "1234"
senha = "1234"
tentativas = 3

while True:
    if tentativas <=3:
        print("\n== Faça seu login ==")
        print(f"Você tem {tentativas} tentativas restantes.")
        login = input("Digite o seu login: ")
        senha = input("Digite a sua senha: ")

        
        if login== login and senha == senha:
            print("\n login aceito.")
            break
        else:
            print("Login ou senha invalidos tente novamente.\n")
            tentativas += 1
            input("Pressione uma tecla para continuar...")

            os.system("cls")


