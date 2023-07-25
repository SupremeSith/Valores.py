x = 1 
while x == 1:

    a = int(input("insira o valor desejado:"))

    while a > 0:

        print (a)

        a -= 1

    if a == 0:

        print ("Contagem Finalizada")
        
    y = input("Deseja sair Agora?  \n s - sim \n n -não \n")

    if y == "s":

        x =2 

    else:

        print("Opção Invalida")
import os

#WHILE DE FECHAMENTO

x = 0

#VARIÁVEIS

list = []
name = []

rg = 0
alt = 0
lis = 0
sair = 0

#MENU DE INTRODUÇÃO

while x == 0:
    print("Bem vindo ao software de saltos!")
    print("[1] Registrar")
    print("[2] Alterar")
    print("[3] Listar")
    print("[4] Sair")
    z = int(input ("Digite a opção desejada: "))
    if z == 1:
        rg = 1
    if z == 2:
        alt = 1
    if z == 3:
        lis = 1
    if z == 4:
        x = 1


y = input("Deseja sair Agora?  \n s - sim \n n -não \n")

if y == "s":
        x =2 
else:

        print("Opção Invalida")