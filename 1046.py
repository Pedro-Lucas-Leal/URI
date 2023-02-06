entrada = input().split()
comeco = int(entrada[0])
final = int(entrada[1])

if comeco == final: print('O JOGO DUROU 24 HORA(S)')
else:
    if comeco < final:
        print(f'O JOGO DUROU {abs(comeco - final)} HORA(S)')
    else:
        print(f'O JOGO DUROU {abs(comeco - 24 - final)} HORA(S)')
