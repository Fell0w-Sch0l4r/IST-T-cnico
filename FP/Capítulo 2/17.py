positivas = 0
total = 0

nota = eval(input('Nota (-1 para parar): '))
while nota != -1:
    if nota > 20 or nota < 0:
        print('Nota inválida')
    total = total + 1
    if nota >= 10:
        positivas = positivas + 1
    nota = eval(input('Nota (-1 para parar): '))
percentagem = (100 * positivas) / total
print('Houve',positivas,'notas positivas que representa',percentagem,'% dos alunos.')
