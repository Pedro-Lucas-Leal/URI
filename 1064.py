num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
num6 = float(input())
i = 0
total = 0

if num1 > 0:
    i = i + 1
    total = total + num1
if num2 > 0:
    i = i + 1
    total = total + num2
if num3 > 0:
    i = i + 1
    total = total + num3
if num4 > 0:
    i = i + 1
    total = total + num4
if num5 > 0:
    i = i + 1
    total = total + num5
if num6 > 0:
    i = i + 1
    total = total + num6

media = total / i
print(f'{i} valores positivos')
print(f'{media:.1f}')
