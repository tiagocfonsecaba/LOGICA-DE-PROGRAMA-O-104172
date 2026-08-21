import os

# limpa o terminal
os.system ("ols")

print ("=SOLICITANDO DADOS=")
valor = float (input ("Digite o valor: ") )

#CALCULANDO
#Descontando 10%
desconto = valor * 0.10
valor_com_desconto = valor - desconto

print("\n=EXIBINDO DADOS=")
print("valor com desconto de 10%: ",valor_com_desconto)