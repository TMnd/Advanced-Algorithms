import string
import random
import os

#variavel global
data=[]
contador = 0
dezpercentagem=[]
cincopercentagem=[]

def povoar():
    global data
    f = open("ficheiroaver.txt")
    lines = f.readlines()
    aux =str(lines[0])
    data = aux.split(" ")

def gerar(num):
    try:
        os.remove("ficheiroaver.txt")
    except OSError:
        pass
    string.letters = 'aaabcdeeefghiiijklmnooopqrstuuuvwxyz'
    file = open('ficheiroaver.txt', 'w+')
    for x in range (0,num):
        #print(random.choice(string.letters))
        file.write(random.choice(string.letters) + " ")
        #file.write(random.choice(string.ascii_lowercase) + " ")
    file.close()

def freqVerdadeira(dados, returnMisga):
    aux = {}
    returnaux = {}
    for i in dados:
        if i in aux:
            aux[i]+=1
        else:
            aux[i] = 1
    for w in returnMisga:
        for i in aux:
            if w==i:
                returnaux[w] = aux[w]
    return returnaux

def frequencia(dados, k):
    n = 0  # conta o nº de iterações
    table = {}
    for i in dados:
        n += 1
        if i in table:
            table[i] += 1
        elif len(table) < k - 1:
            table[i] = 1
        else:
            for j in list(table):
                table[j] -= 1
                if table[j] == 0:
                    table.pop(j)
    return table

def Dezperc(e):
    global dezpercentagem
    totalFreq = 0
    for i in e:
        totalFreq+=e[i]
    CalcDez = totalFreq*(10/100)
    for i in e:
        if e[i] >= CalcDez:
            #print(str(i) + "-" + str(e[i]))
            dezpercentagem.append(str(i) + " - " + str(e[i]))

    if len(dezpercentagem)>0:
        print(dezpercentagem)
    else:
        print("Não havia letras maior que 10%")

def Cincoperc(e):
    global cincopercentagem
    totalFreq = 0
    for i in e:
        totalFreq+=e[i]
    CalcCinco = totalFreq*(5/100)
    for i in e:
        if e[i] >= CalcCinco:
            #print(str(i) + "-" + str(e[i]))
            cincopercentagem.append(str(i) + " - " + str(e[i]))

    if len(cincopercentagem)>0:
        print(cincopercentagem)
    else:
        print("Não havia letras maior que 5%")

print("Insira o numero maximo de elementos a gerar:")
n= int(input())
print("Insira o valor de k:")
k= int(input())
gerar(n)
povoar()
data = list(filter(None, data)) #tirar o maldito null no fim
print("Array de frequencias")
teste = frequencia(data,k)
print(teste)
print("Frequencias totais")
print(freqVerdadeira(data,teste))
print("Lista de letras com mais de 10%")
Dezperc(teste)
print("Lista de letras com mais de 5%")
Cincoperc(teste)