import os
os.system ("cls")

#função com parametros e com retorno
def calcular_notas(nota_1,nota_2):
    resultado= (nota_1 + nota_2)/2
    return resultado


print ("= SOLICITANDO NOTAS =")
nota_1 = float(input("digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))


#usando a função com parametros
#inserindo o retorno na variavel soma
media = calcular_notas(nota_1,nota_2)

print ("= EXIBINDO DADOS =")
print (f'Media:{media}')