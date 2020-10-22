valor = eval(input('Digite o valor: €'))

nota = (valor) * 100

n_50 = 0
if nota // 5000 != 0:
    n_50 = nota // 5000
    nota -= n_50*5000


n_20 = 0
if nota // 2000 != 0:
    n_20 = nota // 2000
    nota -= n_20*2000

n_10 = 0
if nota // 1000 != 0:
    n_10 = nota // 1000
    nota -= n_10*1000

n_5 = 0
if nota // 500 != 0:
    n_5 = nota // 500
    nota -= n_5*500

n_2 = 0
if nota // 200 != 0:
    n_2 = nota // 200
    nota -= n_2*200

n_1 = 0
if nota // 100 != 0:
    n_1 = nota // 100
    nota -= n_1*100

n_050 = 0
if nota // 50 != 0:
    n_050 = nota // 50
    nota -= n_050*50

n_020 = 0
if nota // 20 != 0:
    n_020 = nota // 20
    nota -= n_020*20


n_010 = 0
if nota // 10 != 0:
    n_010 = nota // 10
    nota -= n_010*10


n_005 = 0
if nota // 5 != 0:
    n_005 = nota // 5
    nota -= n_005*5


n_002 = 0
if nota // 2 != 0:
    n_002 = nota // 2
    nota -= n_002*2


n_001 = 0
if nota // 1 != 0:
    n_001 = nota // 1
    nota -= n_001*1

print(f'{valor} equivale a:')

print(f'{n_50} nota(s) de €50')
print(f'\n{n_20} nota(s) de €20')
print(f'\n{n_10} nota(s) de €10')
print(f'\n{n_5} nota(s) de €5')
print(f'\n{n_2} moeda(s) de €2')
print(f'\n{n_1} moeda(s) de €1')
print(f'\n{n_050} moeda(s) de 50 cêntimos')
print(f'\n{n_020} moeda(s) de 20 cêntimos')
print(f'\n{n_010} moeda(s) de 10 cêntimos')
print(f'\n{n_005} moeda(s) de 5 cêntimos')
print(f'\n{n_002} moeda(s) de 2 cêntimos')
print(f'\n{n_001} moeda(s) de 1 cêntimos')