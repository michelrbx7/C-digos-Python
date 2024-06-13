import os
os.system("cls || clear")
#declarando variaveis
nome= str(input("Digite seu nome:"))
idade=int(input("Digite sua idade:"))
primeiraNota=float(input("Digite o primeiro numero:"))
segundaNota=float(input("Digite a segunda nota:"))
terceiraNota=float(input("Digite a terceira nota:"))

#calculo das três notas
soma= primeiraNota+ segundaNota+terceiraNota
#media sera igual a soma dividida pelas três notas
media=soma/3
os.system("cls || clear")

#exibindo dados para o usuario
print(f"nome do aluno:{nome}")
print(f"idade do aluno:{nome}")
print(f"primeira nota do aluno:{primeiraNota}")
print(f"segunda nota  do aluno:{segundaNota}")
print(f"terceira nota  do aluno:{terceiraNota}")
print(f"media do aluno:{media}")

#estrutua condicional
if media >=7:
    print("APROVADO")
elif media >=5:
    print("RECUPERAÇAO")
else:
    print("REPROVADO")    