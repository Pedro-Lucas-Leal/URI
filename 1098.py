i = 0
j = 1

while i <= 2:
    i = round(i,1)
    j = round(j,1)
    print(f'I={i} J={j}')
    print(f'I={i} J={j+1}')
    print(f'I={i} J={j+2}')
    i = round(i, 1) + 0.2
    j = round(j, 1) + 0.2
