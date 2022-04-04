

co = str(input('Co chcesz kupić? '))
cena = float(input('Jaka jest cena towaru? '))
ile = float(input('Podaj ilość towaru: '))

wynik = cena * ile
print(f'Za {ile} kg {co} zapłacisz {wynik:.2f} PLN')
