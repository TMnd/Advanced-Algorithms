import sys
from timeit import Timer

#Variavel global
global valorMaximoRecursivo
global valorMaximoMemoization
contDP = 0
contRC = 0
contRCM = 0

#Dynamic programming
def lisDP(num):
    #Tamanho do array inserido
    n = len(num);

    #Array auxiliar com para inicialicar o LIS
    s = len(num) * [1]

    for i in range(1,n):
        for j in range(0, i):
            increment(1) #para verificar o numero de operações
            if num[i] > num[j] and s[i] < s[j] + 1:
                s[i] = s[j] + 1

    return (max(s))

#Recursive Programming *DONE*
def Recursivo(num, o):
    global valorMaximoRecursivo
    global valorMaximoMemoization

    #Tamnho do array inserido
    n = len(num)

    if o==1:
        valorMaximoRecursivo = 1
        _Recursivo(num,n)
        return valorMaximoRecursivo #Devolve o valor maximo da variavel global
    else:
        valorMaximoMemoization = 1
        _Memoirization(num,n)
        return valorMaximoMemoization #Devolve o valor maximo da variavel global


def _Recursivo(num, n):
    global valorMaximoRecursivo

    #Caso base
    if n == 1:
        return 1

    #tamanho temporario calculado na recursao
    tempsize = 1


    # Se num[i-1] for menor que arr[n-1] calcula-se o
    # tamanho temporario
    # Se o valor calculado for maior que o valor na variaval global,
    # esta será substituida.
    for i in range(1, n):
        valor = _Recursivo(num, i)
        increment(2)  # para verificar o numero de operações
        if num[i - 1] < num[n - 1] and valor + 1 > tempsize:
            tempsize = valor + 1

    #Compara o tempsize com o valor da variavel global valorMaximo,
    #actualizando a variavel global caso necessario!
    valorMaximoRecursivo = max(valorMaximoRecursivo, tempsize)

    return tempsize

def _Memoirization(num, n, memo={}):
    global valorMaximoMemoization

    if n == 1:
        return 1

    tempsize = 1

    for i in range(1, n):
        # Caso exista o valor de i na tabela devolve o valor correspondente
        if i in memo:
            valor = memo[i]
        else: #Caso o valor i nao exista na tabela a key é inserida mais o calor correspondente
            increment(3)  # para verificar o numero de operações
            valor = _Memoirization(num, i)
            memo[i] = valor
        if num[i - 1] < num[n - 1] and valor + 1 > tempsize:
            tempsize = valor + 1

    valorMaximoMemoization = max(valorMaximoMemoization, tempsize)

    return tempsize

#PARA CONSEGUIR INCREMENTAR DENTRO DE FUNÇÕES#
def increment(option):
    global contDP, contRC, contRCM
    if option == 1:
        contDP += 1
    elif option == 2:
        contRC += 1
    else:
        contRCM +=1




print("Insira o valor do elemento que vai inserir: (valor inteiro superior a 0)")
print("Exemplo: Numero de valores:8 --- Sequencia: 10 22 9 33 21 50 41 60")
n = int(input())
i = 0
assert(n>0)

num = []
#caso de teste4: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 10, 22, 9, 33, 21, 50]
#caso de teste3: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7]
#Caso de teste2: [10, 22, 9, 33, 21, 50, 41, 60]
#Caso de teste1: [2, 6, 4, 5, 1, 3]

print("Insira os valores para o array:")
while i<n:
    num.append(int(input()))
    i = i + 1

print("---------------------------")
print("Usando dynamic Programming:")
t = Timer(lambda: print(lisDP(num)))
print("Tempo de processamento: %5.5f segundos" % (t.timeit(number=1)))
print("Numero de operações: " + str(contDP))
print("---------------------------")
print("Usando algoritmo recursivo:")
t2 = Timer(lambda: print(Recursivo(num, 1)))
print("Tempo de processamento: %5.5f segundos" % (t2.timeit(number=1)))
print("Numero de operações: " + str(contRC))
print("---------------------------")
print("Usando recursivo recorrendo a memoirization:")
t3 = Timer(lambda: print(Recursivo(num, 2)))
print("Tempo de processamento: %5.5f segundos" % (t3.timeit(number=1)))
print("Numero de operações: " + str(contRCM))
print("---------------------------")

