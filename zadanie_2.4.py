
import random
x = random.randint(0, 999)

typ = int(input('Podaj swoją liczbę od 0 do 999: '))
i = 0
if x == typ:
    i += 1
    print('Trafiłeś!')
    print(f'Trafiłeś za {i}!')
else:
    i += 1
    while typ != x:
        if typ < x:
            i += 1
            print('Podaj większą liczbę.')
            typ = int(input('Podaj swoją liczbę od 0 do 999: '))
        else:
            i += 1
            print('Podaj mniejszą liczbę.')
            typ = int(input('Podaj swoją liczbę od 0 do 999: '))
    print('Trafiłeś!')
    print(f'Trafiłeś za {i} razem!')


