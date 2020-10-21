num = eval(input('Digite o número: '))
digit = 0
while num != 0:
    digit += num % 10
    num //= 10
print(f'A soma dos digitos de {num} é igual a {digit}.')