import os
os.system ("cls")


def calcular_notas(nota_1,nota_2):
    resultado= (nota_1 + nota_2)/2
    return resultado

def resultado_final(media):
    if media >= 7:
        resultado ="Aprovado!"
    else:
        resultado = "Reprovado!"
    return resultado



    print ("= SOLICITANDO NOTAS =")

nota_1 = float(input("digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))



media = calcular_notas(nota_1,nota_2)
situacao = resultado_final(media)



if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")

print ("= EXIBINDO DADOS =")
print (f'Media:{media}')
print(f'Resultado: {situacao}')