#                                                                  code 1
import numpy as np

num = float(input())

intervalo1 = np.arange(0, 26, 1)
intervalo2 = np.arange(26, 51, 1)
intervalo3 = np.arange(51, 76, 1)
intervalo4 = np.arange(76, 101, 1)

x = 0

for i in intervalo1:
    if i == num: print('Intervalo [0,25]')
    x = x + 1
for i in intervalo2:
    if i == num: print('Intervalo (25,50]')
    x = x + 1
for i in intervalo3:
    if i == num: print('Intervalo (50,75]')
    x = x + 1
for i in intervalo4:
    if i == num: print('Intervalo (75,100]')
    x = x + 1
    
if x == 0: print('Fora de intervalo')
  
#                                                                   code 2

num = float(input())

intervalo1 = []
intervalo2 = []
intervalo3 = []
intervalo4 = []

for i in range(0, 26):
    intervalo1.append(i)
for i in range(26, 50):
    intervalo2.append(i)
for i in range(50, 75):
    intervalo3.append(i)
for i in range(75, 101):
    intervalo4.append(i)

x = 0

for i in intervalo1:
    if i == num:
        print('Intervalo [0,25]')
        x = x + 1
for i in intervalo2:
    if i == num:
        print('Intervalo (25,50]')
        x = x + 1
for i in intervalo3:
    if i == num:
        print('Intervalo (50,75]')
        x = x + 1
for i in intervalo4:
    if i == num:
        print('Intervalo (75,100]')
        x = x + 1

if x == 0 or x > 100:
    print('Fora de intervalo')
    
#                                                                     code 3

num = float(input())

if num >= 0 and num <= 25: print('Intervalo [0,25]')
elif num > 25 and num <= 50: print('Intervalo (25,50]')
elif num > 50 and num <= 75: print('Intervalo (50,75]')
elif num > 75 and num <= 100: print('Intervalo (75,100]')
else: print('Fora de intervalo')
