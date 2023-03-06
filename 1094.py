n = int(input())
c = 0
r = 0
s = 0
for i in range(1, n+1):
    total = input().split()
    Quantia = int(total[0])
    Tipo = total[1]
    while Quantia < 1 or Quantia > 15:
        total = input().split()
        Quantia = int(total[0])
        Tipo = total[1]
    if Tipo == 'C':
        c = c + Quantia
    if Tipo == 'R':
        r = r + Quantia
    if Tipo == 'S':
        s = s + Quantia
todos = c + r + s

print(f'Total: {todos} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {(c/todos) * 100:.2f} %')
print(f'Percentual de ratos: {(r/todos) * 100:.2f} %')
print(f'Percentual de sapos: {(s/todos) * 100:.2f} %')
