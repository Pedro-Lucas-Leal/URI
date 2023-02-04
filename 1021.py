import math
valor = float(input())
while valor < 0 or valor > 1000000.00:
    valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for i in notas:
    total = int(valor/i)
    print(f'{total} nota(s) de R$ {i:.2f}')
    valor = valor - i*total

print('MOEDAS:')
for x in moedas:
    valor = round(valor, 2)
    todo = float(valor/x)
    todo = math.floor(todo)
    print(f'{todo} moeda(s) de R$ {x:.2f}')
    valor = valor - todo*x
