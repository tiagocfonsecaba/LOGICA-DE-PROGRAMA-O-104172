import os
os.system ("cls")
import time
opcao = ""

while opcao != "5":

    print("\n--- MENU ---")
    print("[1] arroz")
    print("[2] Feijão")
    print("[3] carne")
    print("[4] frango")
    print("[5] peixe")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        print("Você escolheu a Opção 1 R$ 10!")
        break
    elif opcao == "2":
        print("Você escolheu a Opção 2 R$ 20!")
        break
    elif opcao =="3":
        print ("voce escolheu a opção 3 R$ 30!")
        break
    elif opcao == "4":
        print ("Você escolheu a opção 4 R$ 40!")
        break
    elif opcao == "5":
        print ("Você escolheu a opção 5 R$ 50!")
        break

    else:
        print ("Opção inválida! Tente novamente.")
        time.sleep (3)
        
        os.system ("cls")