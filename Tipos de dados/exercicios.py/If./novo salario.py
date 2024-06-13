
import os 
os.system("cls || clear")

salario_atual=float(input("Digite seu salario atual:"))

if  salario_atual <500:
    salarioNovo=salario_atual+(salario_atual*0.15)
    print('Salario com reajuste:''=', salarioNovo )

if salario_atual >=500 and salario_atual<=1000:
     salarioNovo=salario_atual+(salario_atual*0.10)  
     print('Salario com reajuste:''=', salarioNovo )  
    
if salario_atual >1000:
    salarioNovo=salario_atual+(salario_atual*0.05)
    print('Salario com reajuste de''=',salarioNovo)

