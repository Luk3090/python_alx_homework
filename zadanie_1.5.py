import math

a = float(input('Wprowadź bok \'a\': '))
b = float(input('Wprowadź bok \'b\': '))
c = float(input('Wprowadź bok \'c\': '))


while a + b <= c or a + c <= b or b + c <= a:
        print("Suma dwóch boków jest mniejsza lub równa trzeciemu boku. \nPodaj właściwe wartości.")
        a = float(input('Wprowadź bok \'a\': '))
        b = float(input('Wprowadź bok \'b\': '))
        c = float(input('Wprowadź bok \'c\': '))

p = (a + b + c) / 2
print(p)
pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f'Pole trójkąta jest równe {pole:.3f}')