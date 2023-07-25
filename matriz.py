#valores do enunciado 
meus_valores = [3,1,4,6,2,5]

#matriz da lista
matriz = {}

#formação do tamanho da matriz 
for i in range(4):
    for v in range(4):
        matriz[(i, v)] =0 

#valores e posições iniciais da matriz 
matriz[( 3, 1)] = meus_valores[0]

matriz[(1, 2)] = meus_valores[ 1]

matriz[(0, 0)] = meus_valores[2]

matriz[(0, 3)] = meus_valores[3]

matriz [(2, 2 )] = meus_valores[4]

matriz [(3, 3)] = meus_valores[5]

#determinação de valores da matriz
for i in range(4):

#print dos valores + posições iniciais da matriz
    for v in range(4):

#ao imprimir o resultado será o número de acordo a ser pedido pela coordenada da matriz (ignore os zeros)
          print(matriz[(i, v)])
          print()