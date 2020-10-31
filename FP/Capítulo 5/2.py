def remove_multiplos(lista,num):
    nova = []
    for c in lista:
        if c%num!=0:
            nova.append(c)
    return nova


print(remove_multiplos([2, 3, 5, 9, 12, 33, 34, 45], 3))