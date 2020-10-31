def ordena_bor(x):
    pos = len(x) - 1
    troca = True
    while troca:
        troca = False
        for c in range(pos):
            if x[c] > x[c + 1]:
                x[c],x[c + 1] = x[c + 1],x[c]
                troca = True
        pos -= 1
    return x


def ordena_shell(x):
    intervalo = len(x) // 2
    while intervalo != 0:
        for c in range(len(x) - intervalo):
            if x[c] > x[c + intervalo]:
                x[c], x[c + intervalo] = x[c + intervalo], x[c]
        intervalo //= 2

    return(x)


def euromilhoes():
    from random import randint
    lista1 = []
    lista2 = []
    for c in range(5):
        a = randint(1,50)
        while a in lista1:
            a = randint(1,50)
        lista1.append(a)

    lista1 = ordena_shell(lista1)

    for c in range(2):
        a = randint(1,12)
        while a in lista2:
            a = randint(1,12)
        lista2.append(a)

    lista2 = ordena_bor(lista2)

    return [lista1,lista2]


print(euromilhoes())