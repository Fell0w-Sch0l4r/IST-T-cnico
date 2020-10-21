a = 1234567
b = ''
while a != 0:
    if a % 2 == 0:
        b += '0'
        a //= 2
    else:
        b += '1'
        a //= 2

print(b)