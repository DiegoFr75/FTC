#cria uma matriz
def criaMatriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

#Exibe uma matriz
def printMatriz(matriz):
    for i in matriz:
        print(i)

#Multiplica duas matrizes
def produtoMatriz(matrizA, matrizB):
    if (len(matrizA[0]) == len(matrizB)):
        novaMatriz = criaMatriz(len(matrizA),len(matrizB[0]))

        for k1 in range(len(matrizA)):
            for k2 in range(len(matrizB[0])):
                temp = 0
                for i in range(len(matrizA[0])):
                    temp = temp+matrizA[k1][i]*matrizB[i][k2]
                novaMatriz[k1][k2] = temp
        return novaMatriz
    else:
        print("Produto inválido")

#Retorna a transposta de uma matriz
def matrizTransposta(matriz):
    nova_matriz = criaMatriz(len(matriz[0]),len(matriz))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            nova_matriz[j][i] = matriz[i][j]
    return nova_matriz

#Recebe o dicionário como string e transforma em dicionário usável

dictionaryString = input()
dictionaryString = dictionaryString.replace('"',"")
dictionaryString = dictionaryString.replace("{","")
dictionaryString = dictionaryString.replace("}","")
dictionaryString = dictionaryString.replace(" ","")
dictionaryString = dictionaryString.replace(":"," ")
dictionaryString = dictionaryString.replace("],"," ",1)
dictionaryString = dictionaryString.replace(","," ",2)
dictionaryString = dictionaryString.split(" ")


listaTuplas = []
list_of_keys = []
v=0

for k in range(4):
    linha =[]
    for j in range(2):
        if(v%2==0):
            linha.append(dictionaryString[v])
            list_of_keys.append(dictionaryString[v])
        else:
            if(v==1 or v==3):
                linha.append(int(dictionaryString[v]))
            else:
                temp = dictionaryString[v].replace("[","")
                temp = temp.replace("]","")
                temp = temp.replace(","," ")
                temp = temp.split(" ")
                linhaLista =[]
                if(v==5):
                    for i in range(len(temp)):
                        try:
                            linhaLista.append(int(temp[i]))
                        except ValueError:
                            linhaLista.append(temp[i])
                    linha.append(linhaLista)
                else:
                    tempAtual=0
                    for i in range(int(dictionaryString[1])):
                        novaLinha = []
                        for p in range(2):
                            novaLinha.append(int(temp[tempAtual]))
                            tempAtual = tempAtual+1
                        linhaLista.append(novaLinha)
                    linha.append(linhaLista)
        v= v+1
    listaTuplas.append(linha)


dictionary = dict(listaTuplas)
number_Of_Words = (int)(input())

#verifica se existe estados finais
if not( '' in dictionary[list_of_keys[3]]):

    list_Of_Words =[]
    for i in range(number_Of_Words):
        inputTemp = input()
        list_Of_Words.append(inputTemp)

    matrizPi = []
    matrizEta = []
    matrizA = []
    matrizB = []

    #Cria matrizPi
    for i in range(dictionary[list_of_keys[0]]):
        linha = []
        for j in range(1):
            if (i == dictionary[list_of_keys[1]]):
                linha.append(1)
            else:
                linha.append(0)
        matrizPi.append(linha)

    #Cria matrizEta
    for i in range(dictionary[list_of_keys[0]]):
        linha = []
        for j in range(1):
            if (i in dictionary[list_of_keys[2]]):
                linha.append(1)
            else:
                linha.append(0)
        matrizEta.append(linha)


    #Cria matrizA
    for i in range(dictionary[list_of_keys[0]]):
        linha = []
        for j in range(dictionary[list_of_keys[0]]):
            linha.append(0)
        matrizA.append(linha)
        matrizA[i][dictionary[list_of_keys[3]][i][0]] = 1


    #Cria matrizB
    for i in range(dictionary[list_of_keys[0]]):
        linha = []
        for j in range(dictionary[list_of_keys[0]]):
            linha.append(0)
        matrizB.append(linha)
        matrizB[i][dictionary[ list_of_keys[3]][i][1] ] = 1

    #Calcula o resultado das operações com matrizes
    for i in range(number_Of_Words):
        if (list_Of_Words[i][0] == "a"):
            matrizResultante = matrizA
        else:
            matrizResultante = matrizB

        for k in range(len(list_Of_Words[i])):
            if((list_Of_Words[i][k]== "a") and (k!=0) ):
                matrizResultante = produtoMatriz(matrizResultante,matrizA)
            else:
                if((list_Of_Words[i][k] == "b") and (k!=0) ):
                    matrizResultante = produtoMatriz(matrizResultante, matrizB)
        matrizResultante = produtoMatriz(matrizTransposta(matrizPi),matrizResultante)
        matrizResultante = produtoMatriz(matrizResultante,matrizEta)
        if(matrizResultante[0][0]) == 1:
            print("ACEITA")
        else:
            print("REJEITA")
else:
    for f in range(number_Of_Words):
        print("REJEITA")