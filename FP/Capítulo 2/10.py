num = eval(input('Digite o número: '))
b=0
while num != 0:
    if num % 2 != 0:
        b = b*10 + num % 10
        num //= 10
    else:
        num //= 10

c = 0
while b != 0:
    c = c * 10 + b % 10
    b //= 10

print(c)