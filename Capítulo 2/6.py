num1 = eval(input('Primeiro número: '))
num2 = eval(input('Segundo número: '))
num3 = eval(input('Terceiro número: '))

if num1>num2 and num1>num3:
    print(f'O maior número é o {num1}')
elif num2>num1 and num2>num3:
    print(f'O maior número é o {num2}')
else:
    print(f"O maior número é o {num3}")