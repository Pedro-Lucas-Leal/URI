import math
num1 = input().split()
num2 = input().split()

x1 = float(num1[0])
y1 = float(num1[1])
x2 = float(num2[0])
y2 = float(num2[1])

distancia = math.sqrt(((x2-x1)*(x2 -x1)) + ((y2-y1) * (y2-y1)))

print(f'{distancia:.4f}')
