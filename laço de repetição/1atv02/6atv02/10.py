import os
os.system("cls")

print ("= Cadastre seu login. =")

login_cadastrado = input("cadastre nome de usuario: ")
senha_cadastrada = input ("cadastre sua senha: ")
print("Cadastro realizado!")
while True:
    
        login = input("Digite o seu login: ")
        senha = input("Digite a sua senha: ")
        
        
        if login == login_cadastrado and senha == senha_cadastrada:
            print("\nLogin confirmado. ")

            #ou utilize uma variavel para determinar o login e e senha 
            break
        else:
            print("\nLogin ou senha inválidos. Tente novamente.\n")
        
            input("Pressione uma tecla para continuar...")
            os.system('cls')



