n = int(input())
i = 0
while i < n:
    num = int(input())
    if num < 0:
        if num % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
    elif num == 0:
        print('NULL')
    else:
        if num % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    i += 1
