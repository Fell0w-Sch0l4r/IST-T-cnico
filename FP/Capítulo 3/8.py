def primo(x):
    n = x**0.5
    cont = 2
    while cont <= n:
        if x % cont == 0:
            return False
        cont += 1
    return True

print(primo(123456789))