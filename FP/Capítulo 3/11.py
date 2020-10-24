def inverte(x):
    digit = 0
    while x != 0:
        digit = digit*10 + x % 10
        x //= 10
    return digit


def digito(num,x):
    '''
    Encontra o dígito selecionado
    :param num: Número
    :param x: Posição do digito
    :return: Dígito Selecionado
    '''
    digits = 0
    num2 = num
    while num2 !=0:
        num2 //= 10
        digits += 1
    while digits != x:
        num //= 10
        digits -= 1
    return num % 10




def misterio(n):
    if 111 <= n <= 999 and abs(digito(n,1) - digito(n,3) > 1):
        ni = inverte(n)
        ns = abs(n - ni)
        nsi = inverte(ns)
        return ns + nsi

    else:
        return 'Condições não verificadas'

print(misterio(452))

'''b) Desde que o número respeite as condições, o resultado será sempre 1089'''