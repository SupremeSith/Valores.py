import os

#VARIAVEIS
mi = 0
np = 0
dc = 0
md = 0
s = 0 
mi1 = 0
np1 = 0
dc1 = 0
md1 = 0
trava1 = 0
trava2 = 0
trava3 = 0

#MENU INICIAL
while s == 0:

    while mi == 0:
        os.system("cls")
        print("Escolha uma opção")
        print("[1] Numero primo")
        print("[2] Decrescente")
        print("[3] Mediana")
        print("[4] Sair")
        x = int(input(""))

        if x == 1:
            np1 = 1
            mi = 1
        elif x == 2:
            dc1 = 1
            mi = 1
        elif x == 3:
            md1 = 1
            mi = 1
        elif x == 4:
            s = 1
            mi = 1
        else:
            print("Opção invalida")
            os.system("pause")

#/////////////////////////////////////////////////////////////
#NUMERO PRIMO
    if np1 == 1:
        np = 1
        np1 = 0

    while np == 1:
        os.system("cls")
        print("Escolha uma opção")
        print("[1] Logica")
        print("[2] Refazer")
        print("[3] Voltar")
        x = int(input(""))    

        if x == 1: #inicia logica dos numeros primos
            if trava1 == 0:
                print("Iniciou a logica dos numeros primos")
                trava1 = 1
                os.system("pause")
            else:
                print("Já foi executada a logica do programa")
                os.system("pause")
        
        
        elif x == 2:
            if trava1 == 1:
                print("Refez a logica dos numeros primos")
                os.system("pause")
            else:
                print("Ainda não foi executada a logica do programa")
                os.system("pause")
        
        
        elif x == 3:
            print("voltar")   
            os.system("pause")  
            np = 0
            mi = 0
        
        
        else:
            print("Opção invalida")
            os.system("pause")

#///////////////////////////////////////////////////////////////////////
#DECRESCENTE

    if dc1 == 1:
        dc = 1
        dc1 = 0

    while dc == 1:
        os.system("cls")
        print("Escolha uma opção")
        print("[1] Logica")
        print("[2] Refazer")
        print("[3] Voltar")
        print("[4] sair")
        x = int(input(""))    

        if x == 1: #inicia logica dos Decresce te
            if trava2 == 0:
                print("Iniciou a logica dos numeros decrescentes")
                trava2 = 1
                os.system("pause")
            else:
                print("Já foi executada a logica do programa")
                os.system("pause")
        
        
        elif x == 2:
            if trava2 == 1:
                print("Refez a logica dos numeros Decresncentes")
                os.system("pause")
            else:
                print("Ainda não foi executada a logica do programa")
                os.system("pause")
        
        
        elif x == 3:
            print("voltar")   
            os.system("pause")  
            dc = 0
            mi = 0

        elif x == 4:
            print("Sair")   
            os.system("pause")  
            dc = 0
            s = 1
        
        
        else:
            print("Opção invalida")
            os.system("pause")

#///////////////////////////////////////////////////////////////////////
#MEDIANA

    if md1 == 1:
        md = 1
        md1 = 0

    while md == 1:
        os.system("cls")
        print("Escolha uma opção")
        print("[1] Logica")
        print("[2] Refazer")
        print("[3] Voltar")
        x = int(input(""))    

        if x == 1: #inicia logica da Mediana
            if trava3 == 0:
                print("Iniciou a logica da mediana")
                trava3 = 1
                os.system("pause")
            else:
                print("Já foi executada a logica do programa")
                os.system("pause")
        
        
        elif x == 2:
            if trava3 == 1:
                print("Refez a logica da mediana")
                os.system("pause")
            else:
                print("Ainda não foi executada a logica do programa")
                os.system("pause")
        
        
        elif x == 3:
            print("voltar")   
            os.system("pause")  
            md = 0
            mi = 0
        
        
        else:
            print("Opção invalida")
            os.system("pause")