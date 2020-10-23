def primo(x):
    n = x**0.5
    cont = 2
    while cont <= n:
        if x % cont == 0:
            return False
        cont += 1
    return True



def n_esimo_primo(n):
    x = 0
    cont = 0
    while cont != n:
        x += 1
        if primo(x):
            cont += 1
    return x

print(n_esimo_primo(19))

