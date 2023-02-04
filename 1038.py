#                                                                       code 1

linha = input().split()

cod1 = int(linha[0])
qtd = int(linha[1])

match cod1:
    case 1:
        preco = 4
    case 2:
        preco = 4.5
    case 3:
        preco = 5
    case 4:
        preco = 2
    case 5:
        preco = 1.5

total = preco * qtd

print(f'Total: R$ {total:.2f}')

#                                                                        code 2

linha = input().split()

cod1 = int(linha[0])
qtd = int(linha[1])

precos = [4, 4.5, 5, 2, 1.5]

for i in precos:
    if precos.index(i) == cod1 - 1: preco = i

total = preco * qtd

print(f'Total: R$ {total:.2f}')
