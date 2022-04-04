
import random
x = random.randint(0, 100)
y = random.randint(0, 100)
print(x)
print(y)
suma_xy = x + y
suma = int(input('Jaka jest suma liczb? '))

while suma != suma_xy:
    suma = int(input('Jaka jest suma liczb? '))
print('Trafiłeś!')

