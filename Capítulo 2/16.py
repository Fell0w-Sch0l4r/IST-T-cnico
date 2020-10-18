num = eval(input('Digite o número: '))
nume = num
digit = 0
contador = 0
while num != 0:
    if digit == 0:
        digit += num % 10
    else:
        digit = digit*10 + num % 10
    num //= 10
    contador += 1

nume = nume*10**contador + digit
print(nume)
