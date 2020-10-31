def valor(q, j, n):
    if j <= 0 or j >= 1 or n < 0 or q < 0:
        raise ValueError
    else:
        return q*(1 + j)**n


print(valor(100, 0.03, 4))


def duplicar(q, j):
    n = 1
    while valor(q, j, n) <= q * 2:
        n += 1
    return n


print(duplicar(100,0.03))