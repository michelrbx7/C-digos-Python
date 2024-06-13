import os
os.system("cls || clear")

salario_atual = float(input("Digite seu salario atual: "))

if salario_atual < 500:
    percentual_reajuste = 0.15
elif salario_atual <= 1000:
    percentual_reajuste = 0.10
else:
    percentual_reajuste = 0.05

salario_novo = salario_atual + (salario_atual * percentual_reajuste)
print('Salario com reajuste: ', salario_novo)