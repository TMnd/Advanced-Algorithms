import random
from timeit import Timer
from builtins import print

arrayNumeros=[]

#Carregar numeros aleatorios para memoria
def loadfiletoarray(nomeFich):
    file = open(nomeFich, "r")

    print("Inserir os elementos para memoria...")
    lines = file.readlines()
    for line in lines:
        arrayNumeros.append(int(line))
    file.close()

#Procura linear
def linearSearch(numSearch):
    x = 1
    for numero in arrayNumeros:
        if numero == int(numSearch):
            return "Encontrou o elemento " + numSearch + " em " + str(x) + " tentativas"
        x+=1
    return "O elemento desejado nao se encontra no ficheiro/array"

#Gerador de numeros
def rollnumber(lenArray):
    roll = random.randint(0, lenArray-1)
    return roll

#Randomized Search las Vegas
#def randomSearchLasVegas(numsearch, tamanhomax):
#    x = 1
#    while 1:
#        result = rollnumber(tamanhomax)
#        if(arrayNumeros[result]==int(numsearch)):
#
#            return "Encontrou o valor " + numSearch +" em " + str(x) + " tentativas"
#        x+=1

#Randomized Search Monte carlo
def randomSearchMonteCarlo(numsearch, maxtentativas, tamanhomax):
    x = 1
    while x<maxtentativas:
        result = rollnumber(tamanhomax)
        if(arrayNumeros[result]==int(numsearch)):
            return "Encontrou o valor " + numSearch + " em " + str(x) + " tentativas"
        x+=1
    return "Falhou em produzir um resultado"


#Main
print("Exemplo de input: C:\\Users\\joaoa\\Desktop\\RandomizedSearch_JoãoAmaral_65772\\SequenciaDeInteiros\\aleatorios10000.txt")
nomeFich = input('Insira o caminho para o ficheiro pretendido: ')

loadfiletoarray(nomeFich)

print("Tamanho do array: " + str(len(arrayNumeros)))

numSearch = input('Insira o numero desejado: ')
nrTentativa = input('Insira o numero de vezes que o algoritmo MC irá correr: ')

print("Resultados:")
print("---------------------------")
print("Pesquisa Linear: ")
t = Timer(lambda: print(str(linearSearch(numSearch))))
print("Tempo de processamento: %5.5f segundos" % (t.timeit(number=1)))
print("---------------------------")
print("Pesquisa random (Monte Carlo): ")
t3 = Timer(lambda: print(str(randomSearchMonteCarlo(int(numSearch), int(nrTentativa), int(len(arrayNumeros))))))
print("Tempo de processamento: %5.5f segundos" % (t3.timeit(number=1)))
print("---------------------------")
