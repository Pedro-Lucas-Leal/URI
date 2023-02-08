salario = float(input())

if salario >= 0 and salario <= 2000: print('Isento')
elif salario > 2000 and salario <= 3000: print(f'R$ {(salario - 2000)*(8/100):.2f}')
elif salario > 3000 and salario <= 4500: print(f'R$ {(salario - 3000)*(18/100)+ (1000*(8/100)):.2f}')
elif salario > 4500: print(f'R$ {(salario - 4500)*(28/100) + (1500 * (18/100)) + (1000 * (8/100)):.2f}')
