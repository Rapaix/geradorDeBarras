import matplotlib.pyplot as plt
import random


count = 0
cor = []
lista = {}
peca = []
soma = 0
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
#            print(indice + " : " + items)
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

def equal(var1,var2):
    if var1 == var2:
        return True
    else:
        return False

#Leitura da base de dados em .txt
arq = open("lego.txt", "r")
firstLine = arq.readline()
firstLine = firstLine.split()
#leitura do arquivo e armazena em uma lista
for i,l in enumerate(arq):
    linha.append(l)


#while sum(x_axis) <= 16 or len(x_axis) < 16:
ale = aleatorio(len(linha)-1) # Encontra a cor de forma aleatoria e armazena em um vetor
item = linha[ale].split()
cor.append(item[0])  # vetor que armazena as cores que forem encontradas
size = len(item)
bloco = Lista(firstLine, item) #Pra que serve a firstline?
a,l = blocosmagicos(bloco)
print(a,l)
x_axis.append(a)
y_axis.append(l)
y, x =  blocosmagicos(bloco)
print("x::",x)
print(x_axis[soma])
if x_axis[soma] == x:
    print("antes",y_axis)
    y_axis[soma]+= y
    print("depois",y_axis)
else:

soma+=1
print("**"*5)
print("Y_AXIS",y_axis,"\n","X_AXIS",x_axis)
print("soma",soma)
print("cor",cor)
print("Peca",peca)

#Grafico de Barras
for i in range(len(x_axis)):
    plt.bar(x_axis[i], y_axis[i], label="cor[i]", color=cor[i])

plt.legend("")
plt.show()
arq.close()


