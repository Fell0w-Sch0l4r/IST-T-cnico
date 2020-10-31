def seq_racman(x):
    a = range(0,x+1)
    lista = []
    for n in a:
        if n == 0:
            lista.append(0)
        elif (n - 1) > n:
            lista.append((n - 1) - n)
        else:
            lista.append((n - 1) + n)


seq_racman(15)