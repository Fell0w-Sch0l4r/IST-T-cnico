def amigas(x,y):
    if len(x) == len(y):
        if x == y:
            return True
        dif = 0
        for c in range(len(x)):
            if x[c] != y[c]:
                dif += 1
        if dif / len(x)  * 100 < 10:
            return True
        else:
            return False
    else:
        return False


