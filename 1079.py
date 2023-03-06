n = int(input())
for i in range (1, n + 1):
    num = input().split()
    A = float(num[0])
    B = float(num[1])
    C = float(num[2])
    print(f'{((A*2)+(B*3)+(C*5))/(2+3+5):.1f}')
