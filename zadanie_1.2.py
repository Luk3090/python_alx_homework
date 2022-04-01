"""
Buty do szewca
"""



dzien_tyg = str(input('Wprowadź dzień tygodnia oddania butów: '))
czas_naprawy = int(input('Ile dni będzie trwała naprawa? '))


if dzien_tyg == 'poniedziałek':
    dzien_tyg = 1
elif dzien_tyg == 'wtorek':
    dzien_tyg = 2
elif dzien_tyg == 'środa':
    dzien_tyg = 3
elif dzien_tyg == 'czwartek':
    dzien_tyg = 4
elif dzien_tyg == 'piątek':
    dzien_tyg = 5
elif dzien_tyg == 'sobota':
    dzien_tyg = 6
elif dzien_tyg == 'niedziela':
    dzien_tyg = 7
else:
    print('Podałeś zły dzień tygodnia!')

termin_oddania = (dzien_tyg + czas_naprawy)

if termin_oddania > 7:
    termin_oddania = termin_oddania - 7
else:
    termin_oddania = (dzien_tyg + czas_naprawy)

komenda = 'Buty możesz odebrać w '

if termin_oddania == 1:
    print(f'{komenda}Poniedziałek')
elif termin_oddania == 2:
    print(f'{komenda}Wtorek')
elif termin_oddania == 3:
    print(f'{komenda}Środa')
elif termin_oddania == 4:
    print(f'{komenda}Czwartek')
elif termin_oddania == 5:
    print(f'{komenda}Piątek')
elif termin_oddania == 6:
    print(f'{komenda}Sobota')
elif termin_oddania == 7:
    print(f'{komenda}Niedziela')
else:
    print('Error')