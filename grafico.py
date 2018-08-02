import matplotlib.pyplot as plt
import random
import numpy as np

count = 0
cor = []
lista = {}
peca = []
soma = 1
y_axis = []
x_axis = []
linha = []
qtds = []

# funcao de randomizar
def aleatorio(a):
    numero = random.randint(0, a)
    return numero


# seleciona indices de blocos com suas quantidades se for maior que zero retorna a lista
def Lista(indices, items):
    print(cor)
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
        #print("bloco", x, y)
        #x1 = int(x[0])
        x2 = int(x[2])
        peca.append(x)
        bloco[x] -= 1
        x1 = bloco[x]
    return x2, x1


#Leitura da base de dados em .txt
arq = open("lego.txt", "r")
firstLine = arq.readline()
firstLine = firstLine.split()
#leitura do arquivo e armazena em uma lista
for i,l in enumerate(arq):
    linha.append(l)

num = aleatorio(15)
while soma < num:
    ale = aleatorio(len(linha)-1)# Encontra a cor de forma aleatoria e armazena em um vetor
    item = linha[ale].split()
    if item[0] in cor:
        break
    else:
        cor.append(item[0])  # vetor que armazena as cores que forem encontradas
        bloco = Lista(firstLine, item) #Pra que serve a firstline?
        l, qtd = blocosmagicos(bloco)
        x_axis.append(soma)
        y_axis.append(l)
        print("qtd",qtd)
        if qtd > 0:
            cont = 0
            ale = aleatorio(qtd)
            while  qtd != ale:
                y_axis[soma-1]+= l
                qtd -= 1
                cont+=1
                if y_axis[soma-1] >= num:
                    break
            qtds.append(cont)
        soma += 1
#Area de Testes
print("**"*5)
print("Y_AXIS",y_axis,"\n","X_AXIS",x_axis)
print("soma",soma)
print("cor",cor)
print("Peca",peca)

#Grafico de Barras
plt.style.use('dark_background')

fig, ax = plt.subplots()
for i in range(len(x_axis)):
    plt.bar(x_axis[i], y_axis[i],align= 'center', label="cor[i]", color=cor[i])
p = np.arange(len(peca))+1
plt.xticks(p,peca)
plt.legend("")
plt.show()
arq.close()


