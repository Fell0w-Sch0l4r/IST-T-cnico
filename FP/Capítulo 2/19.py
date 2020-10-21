nota = 114.91

n_50 = 0
if nota // 50 != 0:
    n_50 = nota // 50
    nota -= n_50*50
    round(nota,2)

n_20 = 0
if nota // 20 != 0:
    n_20 = nota // 20
    nota -= n_20*20

n_10 = 0
if nota // 10 != 0:
    n_10 = nota // 10
    nota -= n_10*10

n_5 = 0
if nota // 5 != 0:
    n_5 = nota // 5
    nota -= n_5*5

n_2 = 0
if nota // 2 != 0:
    n_2 = nota // 2
    nota -= n_2*2

n_1 = 0
if nota // 1 != 0:
    n_1 = nota // 1
    nota -= n_1*1

n_050 = 0
if nota // 0.5 != 0:
    n_050 = nota // 0.5
    nota -= n_050*.5

n_020 = 0
if nota // 0.2 != 0:
    n_020 = nota // 0.2
    nota -= n_020*.2


n_010 = 0
if nota // 0.1 != 0:
    n_010 = nota // 0.1
    nota -= n_010*.1


n_005 = 0
if nota // 0.05 != 0:
    n_005 = nota // 0.05
    nota -= n_005*.05


n_002 = 0
if nota // 0.02 != 0:
    n_002 = nota // 0.02
    nota -= n_002*.02


n_001 = 0
if nota // 0.01 != 0:
    n_001 = nota // 0.01
    nota -= n_001*.01

print(f'{n_50} nota(s) de €50'
      f'\n{n_20} nota(s) de €20'
      f'\n{n_10} nota(s) de €10'
      f'\n{n_5} nota(s) de €5'
      f'\n{n_2} moeda(s) de €2'
      f'\n{n_1} moeda(s) de €1'
      f'\n{n_050} moeda(s) de €0.50'
      f'\n{n_020} moeda(s) de €0.20'
      f'\n{n_010} moeda(s) de €0.10'
      f'\n{n_005} moeda(s) de €0.05'
      f'\n{n_002} moeda(s) de €0.02'
      f'\n{n_001} moeda(s) de €0.01')