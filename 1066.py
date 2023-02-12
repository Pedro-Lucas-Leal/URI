num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

p = 0
i = 0
pos = 0
neg = 0

if num1 % 2 == 0:
    p = p + 1
    if num1 > 0: pos += 1
    elif num1 < 0: neg += 1
else:
    i = i + 1
    if num1 > 0: pos += 1
    elif num1 < 0: neg += 1

if num2 % 2 == 0:
    p = p + 1
    if num2 > 0: pos += 1
    elif num2 < 0: neg += 1
else:
    i = i + 1
    if num2 > 0: pos += 1
    elif num2 < 0: neg += 1
if num3 % 2 == 0:
    p = p + 1
    if num3 > 0: pos += 1
    elif num3 < 0: neg += 1
else:
    i = i + 1
    if num3 > 0: pos += 1
    elif num3 < 0: neg += 1
if num4 % 2 == 0:
    p = p + 1
    if num4 > 0: pos += 1
    elif num4 < 0: neg += 1
else:
    i = i + 1
    if num4 > 0: pos += 1
    elif num4 < 0: neg += 1
if num5 % 2 == 0:
    p = p + 1
    if num5 > 0: pos += 1
    elif num5 < 0: neg += 1
else:
    i = i + 1
    if num5 > 0: pos += 1
    elif num5 < 0: neg += 1

print(f'{p} valor(es) par(es)')
print(f'{i} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')
