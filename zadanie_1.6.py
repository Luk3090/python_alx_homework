'''
Założenia
0 - 6 = wiek przedszkolny = 0 pln
7 - 17 = wiek szkolny = 2.28 pln
18 - 64 = wiek dorosły = 3.80 pln
+65 = wiek emerytalny = 1.90 pln


'''
cena = 0
cena_1 = 0
cena_2 = 2.28
cena_3 = 3.80
cena_4 = 1.90

wiek = int(input('Podaj wiek osoby kupującej bilet: '))
ile = int(input('Ile biletów kupuje: '))

if wiek == 0 and wiek < 6:
    cena = cena_1
elif wiek >= 7 and wiek <= 17:
    cena = cena_2
elif wiek >= 18 and wiek <= 64:
    cena = cena_3
elif wiek >= 65:
    cena = cena_4
else:
    wiek = None

wynik = cena * ile

#print(type(wiek))


print(f'Kupujący musi zapłacić za bilety {wynik:.2f} PLN.')