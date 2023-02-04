entrada = input().split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

if A + B > C and A + C > B and B + C > A: print(f'Perimetro = {A+B+C:.1f}')
else: print(f'Area = {((A+B)*C)/2}')
