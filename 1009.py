nome = input()
salarioFixo = float(input())
vendas = float(input())

total = salarioFixo + (vendas*15/100)

print(f'TOTAL = R$ {total:.2f}')
