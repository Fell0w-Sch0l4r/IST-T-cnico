def valor(q, j, n):
    if j <= 0 or j >=1 or n < 0 or q < 0:
        return ValueError
    else:
        return q * (1 + j)**n


print(valor(100, 0.03, 4))


def duplicar(q, j):
    x = 1
    while True:
        if valor(q,j,x) >= q * 2:
            return x
        else:
            x += 1


print(duplicar(100,0.03))