n = int(input())
while n < 2 and n > 1000:
    n = int(input())

for i in range(1, 11):
    print(f'{i} x {n} = {i*n}')
