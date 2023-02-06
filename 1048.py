salario = float(input())

if salario > 0 and salario <= 400:
    percentual = '15 %'
    reajuste = 15/100 * salario
elif salario > 400 and salario <= 800:
    percentual = '12 %'
    reajuste = 12/100 * salario
elif salario > 800 and salario <= 1200:
    percentual = '10 %'
    reajuste = 1/10 * salario
elif salario > 1200 and salario <= 2000:
    percentual = '7 %'
    reajuste = 7/100 * salario
elif salario > 2000:
    percentual = '4 %'
    reajuste = 4/100 * salario
total = salario + reajuste
print(f'Novo salario: {total:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual}')
