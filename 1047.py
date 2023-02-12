entrada = input().split()
horaInicial = int(entrada[0])
minutoInicial = int(entrada[1])
horaFinal = int(entrada[2])
minutoFinal = int(entrada[3])

if horaInicial == horaFinal and minutoInicial == minutoFinal:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif horaInicial == horaFinal and minutoInicial < minutoFinal:
    print(f'O JOGO DUROU 0 HORA(S) E {minutoFinal - minutoInicial} MINUTO(S)')
else:
    if horaInicial < horaFinal:
        resultadoHora = horaFinal - horaInicial
    else:
        resultadoHora = (24 - horaInicial) + horaFinal
    if minutoInicial > minutoFinal:
        resultadoMinuto = (60 - minutoInicial) + minutoFinal
        resultadoHora = resultadoHora - 1
    else:
        resultadoMinuto = minutoFinal - minutoInicial
    print(
        f'O JOGO DUROU {resultadoHora} HORA(S) E {resultadoMinuto} MINUTO(S)')
