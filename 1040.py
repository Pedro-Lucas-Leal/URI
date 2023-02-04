entrada = input().split()

n1 = float(entrada[0])
n2 = float(entrada[1])
n3 = float(entrada[2])
n4 = float(entrada[3])

p1 = 2
p2 = 3
p3 = 4
p4 = 1

media = ((n1*p1)+(n2*p2)+(n3*p3)+(n4*p4))/(p1+p2+p3+p4)
print(f'Media: {media:.1f}')

if media >= 7: print('Aluno aprovado.')
elif media < 5: print('Aluno reprovado.')
elif media >=5 and media < 7:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame}')
    total = (media + exame) /2
    if total >= 5: print('Aluno aprovado.')
    else: print('Aluno reprovado.')
    print(f'Media final: {total:.1f}')
