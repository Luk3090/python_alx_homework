'''


'''


wiek = int(input('Wprowadź wiek: '))
ile = int(input('Ile nocy spędzisz w hotelu: '))

opl_100 = 100
opl_200 = 200
opl_180 = 180
opl_150 = 150
znizka = 0.9

if wiek < 18:
    oplata = opl_100
elif wiek >= 18 and wiek < 65:
    if ile == 1:
        oplata = opl_200
    elif ile >= 2 and ile < 5:
        oplata = opl_180
    else:
        oplata = opl_150
else:
    if ile == 1:
        oplata = opl_200 * znizka
    elif ile >= 2 and ile < 5:
        oplata = opl_180 * znizka
    else:
        oplata = opl_150 * znizka

wynik = ile * oplata
print(f'Klient płaci za noc {oplata} PLN. Za cały pobyt zapłaci {wynik} PLN.')