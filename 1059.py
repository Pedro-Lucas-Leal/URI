num = []
pares = []
for i in range(1, 101):
    num.append(i)
for i in num:
    if i % 2 == 0:
        pares.append(i)
        print(i)
