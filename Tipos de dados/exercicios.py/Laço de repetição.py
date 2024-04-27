import os
os.system("cls || clear")

produtos= []
for i in range(2):
    produto=str(input(f"Digite o  produto {i+1}:"))
    produtos.append(produto)

    print(f"Lista de compras{produtos}")
    