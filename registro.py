import os

def registro_participante(participantes):
    name = input("Digite o nome do participante a ser registrado: ")
    z = int(input("Digite quantos saltos o participante fez: "))
    val = []
    for num in range(z):
        num = float(input("Digite a distancia do salto: "))
        val.append(num)
    participantes[name] = val
    os.system("cls")
    print("Participante registrado com sucesso!")

participantes = {}
x = 0
while True:
    print("Bem-Vindo ao Software de saltos!!!  \n1- Registro   \n2- Alterar   \n3- Listar   \n4- Sair")
    s = int(input("Digite a opção do Menu Inicial: "))

    if s == 1:
        x = 1
        os.system("cls")
        registro_participante(participantes)

    elif s == 2:
        pass

    elif s == 3:
        pass

    elif s == 4:
        print("O programa foi encerrado:")
        break

    else:
        print("Opção inválida!")
        
        elif s == 3 and x == 0:
        print("Você ainda não cadastrou nenhum Competidor")
        elif s == 3 and x != 0:
        os.system("cls")
        for name, saltos in paticipantes.items():
                soma_saltos = 0
                qtd_saltos = 0
                for salto in saltos:
                    soma_saltos += salto
                    qtd_saltos += 1
                media = soma_saltos / qtd_saltos
                print(f"{name}: {saltos}, Média: {media}")
                os.system("pause")


os.system("pause")