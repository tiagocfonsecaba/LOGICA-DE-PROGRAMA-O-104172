import os
os.system('cls')

numero_1= int(input('Digite o número 1: '))
numero_2= int(input("Digite o número 2: "))
numero_3 = int(input("Digite o numero 3: "))

if numero_1 + numero_2 > numero_3:
    print('É MAIOR QUE O NUMERO 3!')
elif numero_1 + numero_2 < numero_3:
    print('É MENOR QUE O NUMERO 3 !')
else:
    print('É IGUAL AO NUMERO 3 !')