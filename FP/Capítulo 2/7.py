hora_sema = eval(input('Horas de trabalho durante a semana: '))
salario_hora = eval(input('Salário por hora: €'))
salario = 0
if hora_sema<40:
    salario = hora_sema * salario_hora
else:
    salario = hora_sema * salario_hora * 2

print(f'O ordenado semanal é de €{salario}')