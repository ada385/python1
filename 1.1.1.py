liczba = int(input('Podaj liczbe: '))
czy_pierwsza = True

for i in range(2, liczba):
    if liczba % i == 0:
        czy_pierwsza = False

if czy_pierwsza:
    print('pierwsza')

else:
    print('nie jest')

