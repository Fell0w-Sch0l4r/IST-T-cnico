def explode(num):
    if type(num) == int:
        t = ()
        for c in range(len(str(num))):
            t += (num % 10,)
            num //= 10
        return t[::-1]
    else:
        raise ValueError('explode: argumento não inteiro')


def filtra_pares(t):
    tupla = ()
    for c in t:
        if c % 2 == 0:
            tupla += (c,)
    return tupla


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


def algarismos_pares(x):
    tupla = explode(x)
    tupla = filtra_pares(tupla)
    num = implode(tupla)
    return num


print(algarismos_pares(6643399766641))
