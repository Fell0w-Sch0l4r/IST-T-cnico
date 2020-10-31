def lista_codigos(x):
    uni = []
    for c in x:
        uni.append(ord(c))
    return uni


print(lista_codigos('bom dia'))