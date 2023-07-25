import os 
n = int(input("insira um numero:"))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("SenaiJundiai")
    elif i % 3 == 0:
        print("Senai")
    elif i % 5 == 0:
        print("Jundiai")
    else:
        print(i)

        os.system("pause")