'''
Napisz program, który odczytuje od użytkownika wiele liczb.

Program powinien wyliczyć i na końcu wypisać następujące statystyki:

​
- liczba podanych liczb (ile sztuk),

- suma,

- średnia,

- minimum

- maksimum
'''

suma = None
srednia = None
minimum = None
maximum = None

while True:
    dane_wejsciowe = int(input("Podaj liczbę: "))
    if dane_wejsciowe == "koniec":
        break

    if dane_wejsciowe.lstrip().isdecimal() is False:
        print("Niepoprawna wartość!")
        continue

    liczba = int(dane_wejsciowe)

    if minimum is None or liczba < minimum:
        minimum = liczba

    if maximum is None or liczba > maximum:
        maximum = liczba

    if suma is None or sum(liczba):
        print(f'Suma wynosi: {sum(liczba)}')


