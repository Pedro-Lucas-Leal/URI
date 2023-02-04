num = int(input())

qnt = [365, 30, 1]
result = []

for tempo in qnt:
    total = int(num/tempo)
    result.append(total)
    num = num - tempo*total

print(f'{result[0]} ano(s)')
print(f'{result[1]} mes(es)')
print(f'{result[2]} dia(s)')
