'''
BMI
BMI = masa/wzrost^2
'''


masa = float(input('Wprowadź wagę w kg: '))
wzrost = float(input('Wprowadź wzrost w cm: '))
wzrost_m = wzrost / 100


wynik = masa / (wzrost_m ** 2)

print(f'Twój wynik BMI to: {wynik:.1f}')

if wynik < 18.5:
    print('Twój współczynnik BMI wskazuje na NIEDOWAGĘ.')
elif wynik >= 18.5 and wynik <= 24.9:
    print('Twój współczynnik BMI jest w NORMIE.')
elif wynik >= 25 and wynik <= 29.9:
    print('Twój współczynnik BMI wskazuje na NADWAGĘ.')
else:
    print('Twój współczynnik BMI wskazuje na OTYŁOŚĆ.')
