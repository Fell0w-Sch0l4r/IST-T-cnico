'''print('Vou pedir-lhe dois numeros')
x = int(input('Escreva o primeiro número, x = '))
y = int(input('Escreva o segundo número, y = '))

print(f'O valor de ({x} + {y}) X ({x} - {y}) é: {(x + y) * (x - y)}')'''

a = int(input('Distância percorrida em Km: '))

b = int(input('Tempo em minutos:'))

print(f'A velocidade média é:'
      f'\n{a/(b/60):.2f} km/h'
      f'\n{ (a*100) / (b*60):.2f} m/s ')


