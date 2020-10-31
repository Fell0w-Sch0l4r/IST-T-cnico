def elemento_matriz(matriz,linha,coluna):
    if linha<len(matriz) and coluna<len(matriz[linha]):
        return matriz[linha][coluna]
    else:
        raise ValueError('elemento_matriz:índice inválido')


m = [[1, 2, 3], [4, 5, 6]]
print(elemento_matriz(m,4,1))