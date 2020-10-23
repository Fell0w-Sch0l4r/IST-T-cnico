def bissexto(ano):
    if (ano % 4 ==0 and ano % 100 != 0) or ano % 400 == 0:
        return True
    else:
        return False

def dia_mes(x,y):
    if x == 'jan':
        return 31
    elif x == 'fev':
        if bissexto(y):
            return 29
        else:
            return 28
    elif x == 'mar':
        return 31
    elif x == 'abr':
        return 30
    elif x == 'mai':
        return 31
    elif x == 'jun':
        return 30
    elif x == 'jul':
        return 31
    elif x == 'ago':
        return 31
    elif x == 'set':
        return 30
    elif x == 'out':
        return 31
    elif x == 'nov':
        return 30
    elif x == 'dez':
        return 31
    else:
        return 'ValueError: Mês não existe'

print(dia_mes('MAR',2016))