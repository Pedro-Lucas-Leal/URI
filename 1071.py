x = int(input())
y = int(input())

total = 0
lista = [x, y]
lista.sort()
X = lista[0]
Y = lista[1]

for i in range(X+1, Y):
    if i % 2 != 0:
        total = total + i
print(total)
