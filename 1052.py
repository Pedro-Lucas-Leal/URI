#                                             code 1

num = int(input())
while num < 1 and num > 12: num = int(input())

match num:
    case 1: print('January')
    case 2: print('February')
    case 3: print('March')
    case 4: print('April')
    case 5: print('May')
    case 6: print('June')
    case 7: print('July')
    case 8: print('August')
    case 9: print('September')
    case 10: print('October')
    case 11: print('November')
    case 12: print('December')


#                                             code 2

num = int(input())

while num < 1 and num > 12: num = int(input())


if num == 1: print('January')
if num == 2: print('February')
if num == 3: print('March')
if num == 4: print('April')
if num == 5: print('May')
if num == 6: print('June')
if num == 7: print('July')
if num == 8: print('August')
if num == 9: print('September')
if num == 10: print('October')
if num == 11: print('November')
if num == 12: print('December')
