l1 = int(input('Podaj liczbe 1: '))
symbol = input('Podaj symbol operacji arytmetycznej (+, -, /, *, **): ')
l2 = int(input('Podaj liczbe 2: '))

if symbol == '+':
    wynik = l1 + l2
    
elif symbol == '-':
    wynik = l1 - l2

elif symbol == '*':
    wynik = l1 * l2

elif symbol == '/':
    if l2 == 0:
        wynik = 'Nie mozna dzielic przez zero'

    else:
        wynik = l1 / l2

elif symbol == '**':
    wynik = l1 ** l2  

else:
    wynik = 'Nieprawidlowy symbol'

print(wynik)








