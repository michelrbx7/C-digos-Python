import os
os.system("cls || clear")

print("\n==solicitando dados===")
nomeProduto=str(input("Digite o nome do produto"))
quantidadeProduto=int(input("Digite a quantidade do produto"))
precoProduto=float(input("Digite o valor do produto: "))




if quantidadeProduto <= 5:
    desconto = 0.02

elif quantidadeProduto <=10:
        desconto = 0.03
else:
        desconto = 0.05

subTotal=precoProduto * quantidadeProduto
totalPagar = subTotal -(subTotal * desconto)

print("\n--- exibindo resultados===")
print(f"Nome do produto:{nomeProduto}")
print(f"Preço do produto:{precoProduto}")
print(f"quantidadedo produto:{quantidadeProduto}")
print(f"total a pagar:{totalPagar}")



