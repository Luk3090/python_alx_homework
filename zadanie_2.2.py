liczba = int(input('Wprowadź liczbę całkowitą, nie większą niż 10: '))
i = 1

while i <= liczba:
    print(' ' * (10 - i), '* ' * i)
    i += 1