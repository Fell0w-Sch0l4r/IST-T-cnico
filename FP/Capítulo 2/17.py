positivas = 0
total = 0

n = int(input('n = '))
for i in range(n+1):
    nota = int(input(f'Nota nº {i}: '))
    if nota >= 10:
        positivas += 1
    total += nota