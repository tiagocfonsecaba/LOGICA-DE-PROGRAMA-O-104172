import os
os.system ("cls")

#função com parametros e com retorno
def calcular_notas(nota_1,nota_2):
    resultado= (nota_1 * 100)
    return resultado


print ("= SOLICITANDO NOTAS =")
nota_1 = float(input("digite uma medida: "))



#usando a função com parametros
#inserindo o retorno na variavel soma
conversao = calcular_notas(nota_1,nota_2)

print ("= EXIBINDO DADOS =")
print (f'Valor em centimetros: {soma}')
