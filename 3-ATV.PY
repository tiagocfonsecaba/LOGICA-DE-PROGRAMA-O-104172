import os
from datetime import date
os.system ("cls")





dia = input ("Digite dia da semana. ").lower ()

match dia: 
 case"1":
    print ("hoje é dia util. ")

 case"2":
    print ("hoje é dia util.")

 case "3":
    print (" hoje é dia util.")

 case "4":
    print  (" hoje é dia util.")

 case "5":
    print  ("hoje é dia util.")

 case "6" | "7":
    print ("hoje é fim de semana.")

 case _:
      print("dia invalido. ")

    




print (dia)

print ("==FIM==")