import random
options = ['piedra', 'papel', 'tijera']


def options_setter(options):
    j1 = str(input(options).lower())
    j2 = random.choice(options)
    print(j1)
    print(j2)
    return j1, j2


def game(j1, j2):
    if j1 == j2:
        print(f'Empate de {j1} y {j2}')
    elif j1 == 'piedra':
        if j2 == 'papel':
            print(f'Gana la máquina con {j2} contra tu {j1}')
        else:
            print(f'Ganaste con {j1} a la máquina con {j2}')
    elif j1 == 'papel':
        if j2 == 'piedra':
            print(f'Ganaste con {j1} a la máquina con {j2}')
        else:
            print(f'Gana la máquina con {j2} contra tu {j1}')
    elif j1 == 'tijera':
        if j2 == 'piedra':
            print(f'Gana la máquina con {j2} contra tu {j1}')
        else:
            print(f'Ganaste con {j1} a la máquina con {j2}')
    else:
        print('Opción incorrecta')


j1, j2 = options_setter(options)
game(j1,j2)


