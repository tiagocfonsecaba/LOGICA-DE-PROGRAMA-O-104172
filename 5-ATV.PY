import os
os.system ("cls")

print (''' ===Meses do ano=== ''')




prato = input("digite o numero do cardapio. ") .lower()

match prato: 
 case"1":
    print ("Picanha R$ 25,00. ")

 case"2":
    print ("Lasanha R$20,00.")

 case "3":
    print (" Strogonoff R$18,00.")

 case "4":
    print  (" Bife R$15,00.")

 case "5":
    print  ("Pão com ovo R$5,00.")

 
 case _:
      print("Numero invalido ")