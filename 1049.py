#                                                                 code 1

vertebrado = input()
tipo = input()
comida = input()

match vertebrado:
    case 'vertebrado':
        match tipo:
            case 'ave':
                match comida:
                    case 'carnivoro':
                        print('aguia')
                    case 'onivoro':
                        print('pomba')
            case 'mamifero':
                match comida:
                    case 'onivoro':
                        print('homem')
                    case 'herbivoro':
                        print('vaca')
    case 'invertebrado':
        match tipo:
            case 'inseto':
                match comida:
                    case 'hematofago':
                        print('pulga')
                    case 'herbivoro':
                        print('lagarta')
            case 'anelideo':
                match comida:
                    case 'hematofago':
                        print('sanguessuga')
                    case 'onivoro':
                        print('minhoca')
    
    #                                                                  code 2
    
vertebrado = input()
tipo = input()
comida = input()

if vertebrado == 'vertebrado' and tipo == 'ave' and comida == 'carnivoro': print('aguia')
elif vertebrado == 'vertebrado' and tipo == 'ave' and comida == 'onivoro': print('pomba')
elif vertebrado == 'vertebrado' and tipo == 'mamifero' and comida == 'onivoro': print('homem')
elif vertebrado == 'vertebrado' and tipo == 'mamifero' and comida == 'herbivoro': print('vaca')
elif vertebrado == 'invertebrado' and tipo == 'inseto' and comida == 'hematofago': print('pulga')
elif vertebrado == 'invertebrado' and tipo == 'inseto' and comida == 'herbivoro': print('lagarta')
elif vertebrado == 'invertebrado' and tipo == 'anelideo' and comida == 'hematofago': print('sanguessuga')
elif vertebrado == 'invertebrado' and tipo == 'anelideo' and comida == 'onivoro': print('minhoca')
