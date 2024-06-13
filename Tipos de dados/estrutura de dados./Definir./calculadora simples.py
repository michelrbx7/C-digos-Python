import os
os.system("cls || clear")

def cab():
    os.system("cls || clear")
    print("====CALCULADORA SIMPLES====")

def somar(n1,n2):
    return  n1+n2

def subtracao(n1,n2):
    return n1-n2

def divir(n1,n2):
    return n1/n2

def multiplicar(n1,n2):
    return n1*n2
cab()
numeros=[]

while True:
    n = int(input("Digite um Número: "))
    numeros.append(n)
    resposta = input("Deseja inserir mais um numero? (sim/não): ")
    if resposta.lower() != 'sim':
        break

if len(numeros) >= 2:
    n1 = numeros[0]
    n2 = numeros[1]    

soma=somar(n1,n2)
sub=subtracao(n1,n2)
divi=divir(n1,n2)
multi=multiplicar(n1,n2)
cab()

print(f"A soma do primeiro numero e o segundo numero é:{soma}")
print(f"A subtração do primeiro numero e o segundo numero é: {sub}")
print(f"A multiplicação do primeiro numero e o segundo numero é: {multi}")
print(f"A divisão do primeiro numero e o segundo numero é :{divi}")


