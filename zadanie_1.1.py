"""
Interakcja i proste obliczenia.
"""


kilo_ziem = float(input ('Ile kosztuje kilogram ziemniaków? '))
print('*' * 30)
print(f'Za 5 kilogramów ziemniaków musisz zapłacić: {kilo_ziem * 5} PLN')
ile_chce_kupic_ziem = float(input ('Ile kilogramów ziemniaków chcesz kupić? '))
print('*' * 30)
wynik_ziem = ile_chce_kupic_ziem * kilo_ziem
print(f'Za {ile_chce_kupic_ziem} kg. ziemniaków zapłacisz: {wynik_ziem} PLN')
print('*' * 30)
#banany
kilo_bana = float(input ('Ile kosztuje kilogram bananów? '))
print('*' * 30)
ile_chce_kupic_ba = float(input ('Ile kilogramów bananów chcesz kupić? '))
print('*' * 30)
wynik_ba = ile_chce_kupic_ba * kilo_bana
print(f'Za {ile_chce_kupic_ba} kg. bananów zapłacisz: {wynik_ba} PLN')
print('*' * 30)
print(f'Razem za wszystko zapłacisz {wynik_ziem + wynik_ba}')
print('*' * 30)
if wynik_ziem > wynik_ba:
    print('Więcej zapłacisz za ziemniaki, niż za banany.')
elif wynik_ziem < wynik_ba:
    print('Więcej zapłacisz za banany, niż za ziemniaki.')
else:
    print('Za oba produkty zapłacisz równą kwotę.')
print('*' * 30)