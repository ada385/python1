liczba = int(input('Podaj liczbe: '))

for i in range(2, liczba+1):
    if liczba % i == 0:
       
        czy_pierwsza = True

        for j in range(2, i):
            if i % j == 0:
                czy_pierwsza = False

        if czy_pierwsza:
            print(i)