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


# seleciona indices de blocos com suas quantidades se for maior que zero retorna a lista
def Lista(indices, items):
    for (indice, items) in zip(indices, item):
        if items != "0" and len(items) < 3:
            lista[indice] = int(items)
            print(indice + " : " + items)
    return lista

def blocosmagicos(lista):
    #escolhe um uma peça aleatoria
    global x2,x1
    x, y = random.choice(list(lista.items())) #separa os campos de peca e quantidade
    if y == 0:
        blocosmagicos(lista)
    else:
        print("bloco", x, y)
        x1 = int(x[0])
        x2 = int(x[2])
        peca.append(x)
        bloco[x] -= 1
    return x1, x2


#Leitura da base de dados em .txt
arq = open("lego.txt", "r")
firstLine = arq.readline()
firstLine = firstLine.split()
#leitura do arquivo e armazena em uma lista
for i,l in enumerate(arq):
    linha.append(l)
#   print(i,"=>",l)
while len(x_axis) < 16 or sum(x_axis) == 16:
    soma=0
    ale = aleatorio(len(linha)-1) # Encontra a cor de forma aleatoria e armazena em um vetor
    print("=>",ale,"len",len(linha))
    item = linha[ale].split()
    print("ale:",ale,"item:",item)
    cor.append(item[0])  # vetor que armazena as cores que forem encontradas
    soma+=1
    size = len(item)
    bloco = Lista(firstLine, item) #Pra que serve a firstline?
    a,l = blocosmagicos(bloco)
#    print(":",a,l)
    y_axis.append(a)
    x_axis.append(l)
print("teste :",a,l)
print("X_AXIS",x_axis,"\n","Y_AXIS",y_axis)
#print(soma)
print(cor)

#Grafico de Barras
for i in range(len(x_axis)):
    plt.bar(x_axis[i], y_axis[i], label="cor[i]", color=cor[i])

plt.legend("")
plt.show()
arq.close()
