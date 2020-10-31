def num_para_seq_cod(x):
    if not isinstance(x,int) or x <= 0:
        raise ValueError('Valor é menor que 0 ou não é inteiro')
    num = str(x)
    t = ()
    for c in num:
        if int(c) % 2 == 0:
            if int(c) == 8:
                t += (0,)
            else:
                t += (int(c) + 2,)
        else:
            if int(c) == 1:
                t += (9,)
            else:
                t += (int(c) - 2,)

    return t

print(num_para_seq_cod(123456789))