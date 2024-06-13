import os
os.system("cls || clear")

idade=int(input("Digite sua idade"))

if idade >= 0 and idade <=11:
    print(f"Criança")
if idade >= 12 and idade <= 18:
    print(f"Adolescnete")
if  idade >= 19 and idade <= 24:
    print(f"Jovem")
if   idade >= 25 and idade <= 40:
    print(f"Adulto")
if  idade >= 41 and idade <= 60:
    print(f"Meia idade")
elif idade > 60:
    print(f"Idoso")    

