def filtra_pares(t):
    tupla = ()
    for c in t:
        if c % 2 == 0:
            tupla += (c,)
    return tupla


print(filtra_pares((2, 5, 6, 7, 9, 1, 8, 8)))