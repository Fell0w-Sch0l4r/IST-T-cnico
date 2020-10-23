from math import floor


def chao(x):
    return int(x) if x > 0 else int(x) - 1


def semana(x):
    if x == 0:
        return 'Sábado'
    elif x == 1:
        return 'Domingo'
    elif x == 2:
        return 'Segunda'
    elif x == 3:
        return 'Terça'
    elif x == 4:
        return 'Quarta'
    elif x == 5:
        return 'Quinta'
    elif x == 6:
        return 'Sexta'
    else:
        return ValueError


def ano_do_seculo(x):
    return x % 100


def dia_da_semana(dia, m, ano):
    k = ano_do_seculo(ano)
    j = chao(ano / 100)

    h = (dia + chao(13 * (m + 1) / 5) + k + chao(k / 4) + chao(j / 4) - 2 * j) % 7

    return semana(h)


print(dia_da_semana(2, 2, 2020))

# Exercício inacabado