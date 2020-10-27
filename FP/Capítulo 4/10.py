def codifica(x):
    par = ''
    impar = ''
    for c in range(len(x)):
        if c % 2 == 0:
            par += x[c]
        else:
            impar += x[c]
    return par + impar







def descodifica(x):
    impar = ''
    par = ''
    if len(x) % 2 == 0:
        par = x[:len(x)//2]
        impar = x[len(x)//2:]
    else:
        par = x[:len(x) // 2 + 1]
        impar = x[len(x) // 2 + 1:]

    a = ''
    for c in range(len(x) // 2):
        a += par[c] + impar[c]
        if len(par) != len(impar) and par[c+1] == par[-1]:
            a += par[c+1]
    return a

print(codifica(input('Digite o seu nome para descodifica-lo: ')))
print(descodifica('ÂglRdloGmsCgzne oof oe aia'))