import os
os.system("cls || clear")

#Necessário criar 3 variaveis usando listas vazias para armazenar os numeros,numeros pares e os numeros impares.
numeros=[]
pares=[]
impares=[]

for i in range(0,4):#o laço vai rodar três vezes e quando chegar na terceira vez  ele para.

    numero = int(input(f"\nDigite um número qualquer ({i + 1} de 4): "))#aqui ocorre o incremento .
    numeros.append(numero)
    os.system("cls || clear")

    if numero %2==0:
        pares.append(numero)
    else:
        impares.append(numero)

    print(f"Os Números digitados foram {numeros}")    
    print(f"A Quantidade de pares encontrados foram {pares}")    
    print(f"A Quantidade de impares encontrados foram {impares}")