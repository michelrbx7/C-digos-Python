import os

os.system("cls || clear")


#constantes.
QUANTIDADE_ALUNOS=2

#Vetor=espaço na memória que posso guardar informações.
nomes=[]
idades=[]


for i in range(QUANTIDADE_ALUNOS):
    nome=input("digite seu nome:")
    idade=int("digite sua  idade:")

    #alocando nome e idade nas listas.
    nomes.append(nome)
    idades.append(idade)

    #exibindo dados para o usuario
    for i in range(QUANTIDADE_ALUNOS):
        print(f"Nomes:{nomes[i]}") 
        print(f"Idades:{idades[i]}") 