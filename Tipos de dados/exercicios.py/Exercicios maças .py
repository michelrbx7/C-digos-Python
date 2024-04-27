import os
os.system("cls || clear")

qtdMaca=float(input(f"Quantos kilos de maça deseja comprar?"))
precoMaca=1.30


if qtdMaca < 12:
   precoMaca=1.30
if qtdMaca >=12:
    precoMaca=1.00

totalCompra=qtdMaca*precoMaca

print(f"Quantidade de maças comprardas foram:{qtdMaca}")
print(f"O Total da compra foi de :{totalCompra}")




   





