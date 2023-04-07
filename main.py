import numpy as np 
import os
import time


#função para carregar as informações do arquivo
def carregarMapa(arquivo):
    with open(arquivo, "r") as c:
        linhas, colunas, numeroBombas = map(int, c.readline().split())
        campo = np.zeros((linhas, colunas), dtype=int)

        for linha in c:
            x, y = map(int, linha.split())
            campo[x,y] = -1
    
    return campo, numeroBombas
    #print(linhas, colunas, numeroBombas)
    #print(campo)

#Conta as bombas adjacentes as coordenadas escolhidas
def contarBombas(campo, descobertos):
    linhas, colunas = campo.shape

    for i in range(linhas):
        for j in range(colunas):
           
            if campo[i, j] != -1:
                numBombas_adjacente = 0

                for x in range(max(i-1, 0), min(i+2, linhas)):
                    for y in range(max(j-1, 0), min(j+2, colunas)):
                        if campo[x, y] == -1:
                            numBombas_adjacente += 1
                campo[i, j] = numBombas_adjacente

#mostra as casas sem bombas adjacentes
def casasEmBrancoAdjacentes(campo, descobertos, x, y):
    linhas, colunas = campo.shape

    # Marca a casa como descoberta
    descobertos[x, y] = True

    # Percorre todas as casas adjacentes à casa atual
    for i in range(max(x-1, 0), min(x+2, linhas)):
        for j in range(max(y-1, 0), min(y+2, colunas)):
            # Verifica se a casa é válida e não tem bombas adjacentes
            if campo[i, j] == 0 and not descobertos[i, j]:
                # Mostra a casa e continua percorrendo recursivamente
                imprimirMapa(campo, descobertos)
                casasEmBrancoAdjacentes(campo, descobertos, i, j)

#Função para imprimir o mapa
def imprimirMapa(campo, descobertas):
    linhas, colunas = campo.shape

    print("  ", end="")
    for j in range(colunas):
        print(f"{j:2}", end="")
    print()
    

    for i in range(linhas):
        print(f"{i:2}|", end="")
        for j in range(colunas):
            if descobertas[i, j]:
                if campo[i,j] == 0:
                    print("-", end=" ")
                elif campo[i, j] == -1:
                    print('💣', end=" ")
                elif campo[i,j] == 1:
                    print("1", end=" ")
                elif campo[i,j] == 2:
                    print("2", end=" ")
                elif campo[i,j] == 3:
                    print("3", end=" ")
                elif campo[i,j] == 4:
                    print("4", end=" ")
                else:
                    print(f"{campo[i,j]:2}", end=" ")
            else:
                print('#', end=' ')

        print(f'|{i:2}')

    
    print("  ", end="")

    for j in range(colunas):
        print(f'{j:2}', end='')
    print()


#função principal do jogo
def campoMinado():
    campo, numeroBombas = carregarMapa("campo.txt")
    linhas, colunas = campo.shape
    descobertos = np.zeros((linhas, colunas), dtype=int)
    
    gameOver = False

    print("========================================")
    print("              BEM VINDO                 ")
    print("========================================")
    print("Desenvolvedor: Luiz Augusto Cugnier Neto")
    time.sleep(2)
    os.system("cls")
    

    while (not gameOver):
        imprimirMapa(campo, descobertos)
        
        
        x = int(input("Digite a linha: "))
        y = int(input("Digite a coluna: "))

        if descobertos[x,y]:
            print("Campo ja descoberto")
            time.sleep(1)
            os.system("cls")
            continue


        if campo[x,y] == -1:
            contarBombas(campo, descobertos)
            imprimirMapa(campo, np.ones((linhas, colunas), dtype=bool))
            print("Você Perdeu!!!")
            gameOver = True
        else:
            descobertos[x, y] = True
            contarBombas(campo, descobertos)
            casasEmBrancoAdjacentes(campo, descobertos, x, y)
            os.system("cls")
   
        if np.count_nonzero(descobertos == False) == np.sum(campo == 0) - np.sum(campo == -1):
            imprimirMapa(campo, np.ones((linhas, colunas), dtype=bool))
            print("Você ganhou!!!")
            gameOver = True

        

campoMinado()