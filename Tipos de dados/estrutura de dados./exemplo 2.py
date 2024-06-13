import os
from dataclasses import dataclass
os.system("cls || clear")


#constantes.
QUANTIDADE_ALUNOS=2

#Classe.
class Aluno:
#dataclass
    nome:str
    idade:int

#Vetor=espaço na memória que posso guardar informações.
alunos=[]



for i in range(QUANTIDADE_ALUNOS):
    nome=input("digite seu nome:")
    idade=int("digite sua  idade:")

    aluno=Aluno(nome=nome,idade = idade)
    alunos.append(aluno)

    #exibindo dados para o usuario
    for i in alunos:
        print(f"Nomes:{aluno.nome}") 
        print(f"Idades:{aluno.idade}") 