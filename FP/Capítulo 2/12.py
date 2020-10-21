x = eval(input('Valor de x: '))
n = eval(input('Valor de n: '))
soma = 1
s = 1
while n != 0:
    m = s
    f = 1 #fatorial
    while m != 0:
        f *= m
        m -= 1
    soma += (x**s) / f
    n -= 1
    s += 1

print(f'O valor da soma é {soma}')
