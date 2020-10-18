num_inve = 0
num = eval(input('Escreva um número inteiro positivo: '))
while True:
   digit = num % 10
   num //= 10

   if num_inve == 0:
       num_inve = digit
   else:
       num_inve = num_inve * 10 + digit
   if num == 0:
       break

print(f'O número é: {num_inve}')
