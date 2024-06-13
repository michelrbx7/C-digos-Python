#limpar terminal
import os
os.system("cls || clear")
#declarando as variaveis
nome=str(input("Digite seu Nome:"))
idade=int(input("Digite sua Idade:"))
primeiroNumero=int(input("Digite o primeiro numero"))
segundoNumero=int(input("Digite o segundo Numero"))

#montando esquema de calculos 
soma= primeiroNumero + segundoNumero
multiplicacao= primeiroNumero * segundoNumero
subtracao= primeiroNumero - segundoNumero
divisao= primeiroNumero / segundoNumero

os.system("cls || clear")
#exibindo os dados fornecidos
print(f"Nome do aluno:{nome}")
print(f"Idade do aluno:{idade}")
print(f"primeiro numero:{primeiroNumero}")
print(f"segundo numero:{segundoNumero}")
print(f"A Soma :{soma}")
print(f"A Multiplicação:{multiplicacao}")
print(f"A Subtração:{subtracao}")
print(f"A Divisão:{divisao}")