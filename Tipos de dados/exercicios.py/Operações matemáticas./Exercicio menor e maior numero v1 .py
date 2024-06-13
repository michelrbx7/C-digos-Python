import os
os.system("cls || clear")

primeiroNumero=int(input("Digite o primeiro numero"))
segundoNumero=int(input("Digite o segundo numero"))

soma = primeiroNumero+ segundoNumero
media = primeiroNumero + segundoNumero/2
produto =primeiroNumero * segundoNumero

print(f"primeiro numero:{primeiroNumero}")
print(f"segundo numero:{segundoNumero}")
print(f"A Soma :{soma}")
print(f"o produto:{produto}")

maiorNumero=max(primeiroNumero,segundoNumero)
menorNumero=min(primeiroNumero,segundoNumero)

os.system("cls || clear")
print("=====\n exibindo resultados=====")
print(f"Primeiro Numero:{primeiroNumero}")
print(f"Segundo Numero:{segundoNumero}")
print(f"soma:{soma}")
print(f"media:{media}")
print(f"produto:{produto}")
print(f"Maior Numero{maiorNumero}")
print(f"Menor Numero{menorNumero}")