import math
linhaUm = input().split()

A = float(linhaUm[0])
B = float(linhaUm[1])
C = float(linhaUm[2])

delta = (B*B) - (4*A*C)

if A == 0 or delta < 0:
    print('Impossivel calcular')
else:
    r1 = (-B + math.sqrt(delta))/ (2*A)
    r2 = (-B - math.sqrt(delta))/ (2*A)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
