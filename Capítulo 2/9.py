a = 0
while True:
   b = eval(input('Escreva um dígito\n(-1 para terminar):'))

   if b < 0:
       break

   if a == 0:
       a = b
   else:
       a = a * 10 + b

print(f'O número é: {a}')
