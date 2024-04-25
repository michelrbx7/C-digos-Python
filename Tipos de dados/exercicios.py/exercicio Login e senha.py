import os 
os.system("cls || clear")

login=str(input("Digite o login: "))
senha=int(input("Digite sua senha: "))


if login == "michel" and senha ==123:
    print("bem vindo")
else:
    print("login ou senha invalidos")    