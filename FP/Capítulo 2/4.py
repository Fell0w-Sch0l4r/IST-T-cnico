segundo = eval(input('Escreva o número de segundos: '))
seg = segundo
dia = int(seg / 86400)
seg = (seg / 86400) - dia

hora = int(seg * 24)
seg = (seg * 24) - hora

min = int(seg * 60)
seg = (seg * 60) - min

sec = int(seg * 60)

print(f'{segundo} segundos correspondem a {dia} dia(s), {hora} hora(s), {min} minuto(s) e {sec} segundo(s).')