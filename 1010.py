produto1 = input().split()
codUm = int(produto1[0])
quantidadeUm = int (produto1[1])
valorUm= float(produto1[2])

produto2 = input().split()
codDois = int(produto2[0])
quantidadeDois = int(produto2[1])
valorDois = float(produto2[2])

total = (quantidadeUm * valorUm) + (quantidadeDois * valorDois)

print(f'VALOR A PAGAR: R$ {total:.2f}')
