def reconhece(x):
    carat = 'ABCD1234'
    numeros = '1234'
    if x[0] in numeros:
        return False
    for d,c in enumerate(x):
        if c not in carat:
            return False
        elif c!=x[-1] and c in numeros and x[d+1] not in numeros:
            return False
    return True

print(reconhece('ABC12C'))

"""
O programa começa por verificar se o primeiro carácter perntence a (1234) e, se pertencer, a função retorna logo falso.
Depois verifica se cada caracter está presente em (ABCD1234).
No caso do caracter estiver em (1234) e o seu sucessor não, então retorna logo false.
"""