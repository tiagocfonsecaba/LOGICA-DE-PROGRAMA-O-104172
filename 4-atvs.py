import os
os.system ("cls")

print (''' ===MENU===
1  PICANHA R$25,00
2  LASANHA R$20,00
3  STROGONOFF R$18,00
4  BIFE R$ 15,00
5  PÃO COM OVO R$5,00''')



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