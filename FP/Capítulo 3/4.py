def area_circulo(x):
    '''
    Função que calcula a área do círculo.
    :param x: raio
    :return: Área do círculo
    '''
    return (x**2) * 3.14

def area_coroa(r1,r2):
    if r1 > r2:
        return ValueError
    else:
        return area_circulo(r2) - area_circulo(r1)

print(area_coroa(2,3))