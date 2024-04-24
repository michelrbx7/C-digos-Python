import os
os.system("cls || clear")

nome= str(input("Digite seu nome"))
idade=int(input("Digite sua idade"))
primeiraNota=float(input("Digite o primeiro numero"))
segundaNota=float(input("Digite a segunda nota"))

soma= primeiraNota+ segundaNota
media=soma/2

print(f"nome do aluno:{nome}")
print(f"idade do aluno:{nome}")
print(f"primeira nota do aluno:{primeiraNota}")
print(f"segunda nota  do aluno:{segundaNota}")
print(f"media do aluno:{media}")