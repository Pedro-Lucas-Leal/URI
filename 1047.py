#                                                                        code 1

entrada = input().split()
horaInicial = int(entrada[0])
minutoInicial = int(entrada[1])
horaFinal = int(entrada[2])
minutoFinal = int(entrada[3])

if horaInicial == horaFinal and minutoInicial == minutoFinal:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    if horaInicial < horaFinal:
        resultadoHora = horaFinal - horaInicial
    else:
        resultadoHora = abs(horaFinal - 24 - horaInicial)
    if minutoInicial > minutoFinal:
        resultadoMinuto = abs(minutoInicial - 60 - minutoFinal)
        resultadoHora = resultadoHora - 1
    else:
        resultadoMinuto = minutoFinal - minutoInicial
    print(f'O JOGO DUROU {resultadoHora} HORA(S) E {resultadoMinuto} MINUTOS(S)')
