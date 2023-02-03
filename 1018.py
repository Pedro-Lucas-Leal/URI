#                                                                            code 1

valor = int(input())
while valor > 1000000:
    valor = int(input())

cem = cinquenta = vinte = dez = cinco = dois = um = 0

while valor >= 100:
    valor = valor - 100
    cem = cem + 1

while valor >= 50:
    valor = valor - 50
    cinquenta = cinquenta + 1

while valor >= 20:
    valor = valor - 20
    vinte = vinte + 1

while valor >= 10:
    valor = valor - 10
    dez = dez + 1

while valor >= 5:
    valor = valor - 5
    cinco = cinco + 1

while valor >= 2:
    valor = valor - 2
    dois = dois + 1

while valor >= 1:
    valor = valor - 1
    um = um + 1

print(valor)
print(cem, 'nota(s) de R$ 100,00')
print(cinquenta, 'nota(s) de R$ 50,00')
print(vinte, 'nota(s) de R$ 20,00')
print(dez, 'nota(s) de R$ 10,00')
print(cinco, 'nota(s) de R$ 5,00')
print(dois, 'nota(s) de R$ 2,00')
print(um, 'nota(s) de R$ 1,00')

#                                                                        code 2

valor = int(input())
while valor > 1000000:
    valor = int(input())
print(valor)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    total = int(valor / nota)
    print(f'{total} nota(s) de R$ {nota},00')
    valor = valor - total*nota
