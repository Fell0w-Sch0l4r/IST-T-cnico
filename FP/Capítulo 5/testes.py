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

le_elementos_l()