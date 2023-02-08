#                                                                    code 1

num = int(input())

match num:
    case 61:
        print('Brasilia')
    case 71:
        print('Salvador')
    case 11:
        print('Sao Paulo')
    case 21:
        print('Rio de Janeiro')
    case 32:
        print('Juiz de Fora')
    case 19:
        print('Campinas')
    case 27:
        print('Vitoria')
    case 31:
        print('Belho Horizonte')
    case _:
        print('DDD nao cadastrado')
    
    #                                                              code 2
    
num = int(input())

if num == 61: print('Brasilia')
elif num == 71: print('Salvador')
elif num == 11: print('Sao Paulo')
elif num == 21: print('Rio de Janeiro')
elif num == 32: print('Juiz de Fora')
elif num == 19: print('Campinas')
elif num == 27: print('Vitoria')
elif num == 31: print('Belho Horizonte')
else: print('DDD nao cadastrado')
