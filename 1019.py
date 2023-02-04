N = int(input())

horas = minutos = segundos = int
tempo = [3600, 60, 1]

for segundo in tempo:
    total = int(N/segundo)
    if segundo >= 3600:
        horas = total
        N = N - segundo*total
    elif segundo >= 60:
        minutos = total
        N = N - segundo*total
    elif segundo >= 0:
        segundos = total
        N = N - segundo*total
    
print(f'{horas}:{minutos}:{segundos}')
