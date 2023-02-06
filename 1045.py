entrada = input().split()

entrada.sort(reverse=True, key=float)

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

if A >= (B + C):
    print('NAO FORMA TRIANGULO')
else:
    if (A*A) == (B*B) + (C*C):
        print('TRIANGULO RETANGULO')
    if (A*A) > (B*B) + (C*C):
        print('TRIANGULO OBTUSANGULO')
    if (A*A) < (B*B) + (C*C):
        print('TRIANGULO ACUTANGULO')
    if A == B and A == C:
        print('TRIANGULO EQUILATERO')
    elif A == B != C or A == C != B or B == C != A:
        print('TRIANGULO ISOSCELES')
