#                                                                   code 1

entrada = input().split()

X = float(entrada[0])
Y = float(entrada[1])

if X == 0 and Y == 0: print('Origem')
elif X == 0 and Y != 0: print('Eixo X')
elif X != 0 and Y == 0: print('Eixo Y')
elif X > 0:
    if Y > 0: print('Q1')
    elif Y < 0: print('Q4')
elif X < 0:
    if Y > 0: print('Q2')
    elif Y < 0: print('Q3')

#                                                                       code 2

p = input().split()
x, y = p

x = float(x)
y = float(y)

if x == 0:
    if y == 0:
        print('Origem')
    if y != 0:
        print('Eixo Y')
if y == 0:
    if x != 0:
        print('Eixo X')
if x > 0:
    if y > 0:
        print('Q1')
    if y < 0:
        print('Q4')
if x < 0:
    if y > 0:
        print('Q2')
    if y < 0:
        print('Q3')
