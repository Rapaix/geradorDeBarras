import matplotlib.pyplot as plt
import random
import numpy as np

count = 0
cor = []
lista = {}
peca = []
soma = 0
color = ['r','b','g','c','y']
y_axis = []
x_axis = []
linha = []
# funcao de randomizar
def aleatorio(a):
    numero = random.randint(0, a)
    # print(":",numero)
    return numero


# seleciona indices de blocos com suas quantidades se for maior que zero
def Lista(indices, items):
    for (indice, items) in zip(indices, item):
        if items != "0" and len(items) < 3:
            lista[indice] = int(items)
            print(indice + " : " + items)
    return lista

def blocosmagicos(lista):
    #escolhe um uma peça aleatoria
    x, y = random.choice(list(lista.items())) #separa os campos de peca e quantidade
    if y == 0:
        blocosMagicos(lista)
    else:
        print("bloco", x, y)
        x1 = int(x[0])
        x2 = int(x[2])
        y_axis.append(x1)
        peca.append(x)
        bloco[x] -= 1
    return x1,x2


#Leitura da base de dados em .txt
arq = open("legon.txt", "r")
firstLine = arq.readline()
firstLine = firstLine.split()
#leitura do arquivo e armazena em uma lista
for i,l in enumerate(arq):
    linha.append(l)
#   print(i,"=>",l)
while len(x_axis) < 16:
    ale = aleatorio(len(linha))
    item = linha[ale].split()
    print(item)

    # Encontra a cor de forma aleatoria e armazena em um vetor
    # verifica o numero aleatorio()
    cor.append(item[0])  # vetor que armazena as cores que forem encontradas
    print(cor[soma])
    size = len(item)
    aleatorio(size)
    bloco = Lista(firstLine, item)
    soma+=1
    a,l = blocosmagicos(lista)
    y_axis.append(a)
    x_axis.append(l)
print("teste :",a,l)
print("X_AXIS",x_axis)
print("*****")

#print(x_axis,y_axis)
#print(soma)


#Grafico de Barras
for i in range(len(x_axis)):
    plt.bar(x_axis[i], y_axis[i], label="cor[i]", color="b")

plt.legend("")
plt.show()

#print(count) # numero de linhas


arq.close()
