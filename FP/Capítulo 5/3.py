def soma_cumulativa(x):
    nova = []
    for t in range(len(x)):
        num = 0
        for c in range(t+1):
            num+=x[c]
        nova.append(num)
    return nova



soma_cumulativa([1, 2, 3, 4, 5])