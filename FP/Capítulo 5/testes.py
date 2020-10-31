def remove_multiplos(lisst, x):
    x = lisst[x]
    lista = []
    for c in lisst:
        if c % x != 0 or c == x:
            lista.append(c)
    return lista



def crivo(n):
    lista = range(2, n+1)
    from math import sqrt
    num = 0
    while lista[num] < sqrt(n):
        lista = remove_multiplos(lista, num)
        num += 1
    return lista



def pro_bin(ll,n):
    prim = 0
    ult = len(ll) - 1
    while prim <= ult:
        meio = (prim + ult) // 2
        if n == ll[meio]:
            return True
        elif ll[meio] < n:
            prim = meio + 1
        else:
            ult = meio - 1
    return False

def le_elementos():
    x = input('Digita os números separados por espaço:')
    i = 0
    num = ''
    elementos = []
    for d,c in enumerate(x):
        if c != ' ' and c!= '0':
            num += c
            if d == len(x)-1:
                elementos.append(eval(num))
        if d!=0 and c == ' ' and x[d-1] != ' ':
            elementos.append(eval(num))
            num = ' '
    print(elementos)


def le_elementos_l():
    x = input('n ')
    elementos = []
    i = 0
    while True:
        while i<len(x) and x[i] == ' ':
            i+=1
        num = ''
        while i<len(x) and x[i] != ' ':
            num+= x[i]
            i+=1
        elementos.append(eval(num))
        if i == len(x):
            return elementos

def ordena_bor(x):
    maior = len(x)-1
    troca = True
    while troca:
        troca = False
        for c in range(maior):
            if x[c]>x[c+1]:
                x[c],x[c+1] = x[c+1],x[c]
                troca = True
        maior -= 1


#ordena_bor([4377,74745,342342,6787,4552,787,122,112,1,2,3,4,5,6,7,9,8,7,5,4,8,78,45,57])


def shellsort(x):
    inter = len(x) // 2
    troca = True
    while troca:
        troca = False
        for c in range(len(x)-inter):
            if x[c] > x[c+inter]:
                x[c],x[c+inter] = x[c+inter],x[c]
                troca = True
        inter //= 2

#shellsort([4377,74745,342342,6787,4552,787,122,112,1,2,3,4,5,6,7,9,8,7,5,4,8,78,45,57])



