dist = eval(input('Distância percorrida: Km '))
temp = eval(input('Tempo: min '))

print(f'A velocidade média é de {(dist/temp)*60:.2f}km/h ou {(dist/temp)*(100/6):.2f}m/s')