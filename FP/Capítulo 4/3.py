def implode(a):
    b = 0
    for c in a:
        if type(c) != int:
            raise ValueError('implode: elemento não inteiro')
        elif b == 0:
            b += c
        else:
            b = b * 10 ** (len(str(c))) + c
    return b


print(implode((1, 2, 3, 999, 5, 6, 7)))
