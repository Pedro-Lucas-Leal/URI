entrada = input().split()

A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])

valores = [A, B, C]
lido = valores.copy()
valores.sort()

for x in range (len(valores)):
    print (valores[x])

print('')

for x in range(len(valores)):
    print(lido[x])
