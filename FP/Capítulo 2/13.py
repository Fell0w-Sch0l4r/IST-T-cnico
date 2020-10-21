print('Escreva um numero para eu escrever a tabuada da multiplicação.')
num = eval(input('Número: '))
a=1
while a<11:
    print(f'{num} x {a} = {num * a}')
    a+=1