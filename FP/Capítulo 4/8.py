def junta_ordenados(x,y):
    return tuple(sorted(x + y))


print(junta_ordenados((2, 34, 200, 210), (1, 23)))


def junta(x,y):
    i1 = i2 = 0
    res = ()
    while i1 < len(x) and i2 < len(y):
        if x[i1] < y[i2]:
            res += (x[i1],)
            i1 += 1
        elif x[i1] < y[i2]:
            res += (y[i2],)
            i2 += 1
        else:
            res += (x[i1], y[i2])
            i1 += 1
            i2 += 1
    if i1 == len(x):
        res += y[i2:]
    else:
        res += x[i1:]

junta((1,2, 34, 200, 210), (1, 23))