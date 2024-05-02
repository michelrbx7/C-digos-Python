import os
os.system("cls || clear")

numero=int(input("\nDigite um numero inteiro"))

if numero<0:
    print(f"O Numero é negativo")
if numero>0:
    print(f"O Numero é positivo")
if numero==0:
    print(f"O numero é neutro")