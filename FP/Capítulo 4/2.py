def explode(num):
    if type(num) == int:
        t = ()
        for c in range(len(str(num))):
            t += (num % 10,)
            num //= 10
        return t[::-1]
    else:
        raise ValueError('explode: argumento não inteiro')

print(explode(6643399766641))
