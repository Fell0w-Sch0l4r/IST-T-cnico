def escreve_matriz(x):
    for c in x:
        for t in c:
            print(t,end=' ')
        print()


def soma_mat(a,b):
    matriz = []
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError('soma:matriz: soma das matrizes não é possível')
    else:
        for c in range(len(a)):
            matriz.append([])
            for t in range(len(a[c])):
                matriz[c].append(a[c][t] + b[c][t])
    return matriz

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
escreve_matriz(soma_mat(m1, m2))
