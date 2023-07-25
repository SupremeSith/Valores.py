import os

#VARIAVEL

poligono_selecionado = None #

#MENU

while True: 
    print("=== MENU ===") 
    print("1. Selecionar Polígono")
    print("2. Alterar Valor")
    print("3. Listar")
    print("4. Sair")

#SELEÇÃO DO PRIMEIRO PRINT

    opcao = input("Escolha uma opção: ") #input para seleççao do menu

    if opcao == "1": # (caso o menu seja selecionado )
        poligono_selecionado = input("Digite o nome do polígono: ") #introduza o nome do poligono
        print(f"Polígono '{poligono_selecionado}' selecionado.") 

#SELEÇÃO DO SEGUNDO PRINT 

    elif opcao == "2":
        if poligono_selecionado is None:
            print("Nenhum polígono selecionado.")

        else:

            novo_valor = float(input("Digite o novo valor: "))
            print(f"Valor do polígono '{poligono_selecionado}' alterado para {novo_valor}.")



    elif opcao == "3":
        print("Lista de polígonos:")
        # Adicione aqui o código para listar os polígonos

    elif opcao == "4":
        print("Saindo...")
        break

    else:

        print("Opção inválida. Tente novamente.")
os.system("pause")