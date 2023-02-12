N = int(input())
lista = []
dentro = 0
fora = 0

for i in range (1, N +1):
    num = int(input())
    lista.append(num)
for i in lista:
    if i >= 10 and i <= 20: dentro += 1
    else: fora += 1
    
print(f'{dentro} in')
print(f'{fora} out')
