from math import sqrt
num1 = eval(input('Primeiro número: '))
num2 = eval(input('Segundo número: '))
num3 = eval(input('Terceiro número: '))
num4 = eval(input('Quarto número: '))
num5 = eval(input('Quinto número: '))

media = (num1 + num2 + num3 + num4 + num5) / 5
dsvio = ((num1 - media)**2 + (num2 - media)**2 + (num3 - media)**2 + (num4 - media)**2 + (num5 - media)**2) / 4
dsvio = sqrt(dsvio)

print(f'A média dos números é: {media}.')
print(f'O desvio padrão é de {dsvio:.2f}')
