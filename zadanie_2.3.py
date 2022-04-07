


lista = []

#while len(lista) == 6:


while len(lista) < 5:
    liczba = int(input('Podaj liczby: '))
    lista.append(liczba)

srednia = sum(lista) / len(lista)
ile = len(lista)
min = min(lista)
max = max(lista)


print(f'Lista ma {ile} elementów.')
print(f'Średnia to: {srednia}')
print(f'Najmniejsza liczba to: {min}')
print(f'Największa liczba to: {max}')