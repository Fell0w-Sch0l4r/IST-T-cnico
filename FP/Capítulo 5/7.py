def escreve_matriz(x):
    for c in x:
        for t in c:
            print(t,end=' ')
        print()


def multiplica_matriz(a,b):
    if len(m1[0]) != len(b):
        raise ValueError('A multiplicação das matrizes não é possível.')
    else:
        nova = []
        for d in range(len(a)):
            nova.append([])
            for c in range(len(b[0])):
                num = 0
                for t in range(len(b)):
                    num += a[d][t] * b[t][c]
                nova[d].append(num)
        return nova

m1 = [[1,2,3],[4,5,6]]
m2 = [[1,2,7],[3,4,7],[5,6,7]]
m3 = [[1],[2],[3]]

escreve_matriz(multiplica_matriz(m1, m2))

'''
Nesta função para multiplicar matrizes usei três 'for(s)'.
O primeiro for controla a linha da matriz a, o segundo controla as colunas da matriz b e o terceiro
controla a quantidade de multiplicações feitas que depende do número de linhas existentes nas matriz b.
'''