num = []

for i in range(1, 101):
    n = int(input())
    num.append(n)

print(f'{max(num)}')
print(f'{num.index(max(num))+1}')
