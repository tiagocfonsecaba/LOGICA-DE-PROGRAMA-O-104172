import os
from datetime import date
os.system ("cls")





dia = input ("Digite dia da semana. ").lower ()

match dia: 
 case"segunda":
    print ("hoje é segunda feira. ")

 case"Terça":
    print ("hoje é Terça feira.")

 case "quarta":
    print ("hoje é quarta feira.")

 case "quinta":
    print  ("hoje é quinta  feira.")

 case "sexta":
    print  ("hoje é sexta feira.")

 case "sabado"|"domingo":
    print ("hoje é fim de semana.")

print (dia)

print ("==FIM==")
