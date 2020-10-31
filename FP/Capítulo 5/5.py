def escrever_matriz(x):
    for c in x:
        for t in c:
            print(t,end=' ')
        print()

escrever_matriz([[1, 2, 3], [4, 5, 6]])