"""
Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu,
a program wylicza, ile trzeba zapłacić. Zasady są takie:

- nieletni (poniżej 18 roku życia) płacą 100 zł za noc
- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
	- 200 zł za noc, jeśli nocują jedną noc
	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki

Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy,
zapłaci 150 zł za noc z 10% zniżki, czyli 150-15 zł za noc,
czyli 135 zł za noc, czyli 1350 zł.

"""

wiek = int(input("Podaj swój wiek: "))
ilosc_nocy = int(input("Ile nocy spędzisz w hotelu?: "))

if wiek < 18:
    print(f'Cena za pobyt: {100 * ilosc_nocy} PLN')
elif 18 < wiek < 65:
    if ilosc_nocy == 1:
        print(f'Cena za pobyt: {200} PLN')
    elif 2 <= ilosc_nocy < 5:
        print(f'Cena za pobyt: {180 * ilosc_nocy} PLN')
    elif ilosc_nocy >= 5:
        print(f'Cena za pobyt: {150 * ilosc_nocy} PLN')
elif wiek >= 65:
    if ilosc_nocy == 1:
        print(f'Cena za pobyt: {200 - 200 * 1/10} PLN')
    elif 2 <= ilosc_nocy < 5:
        print(f'Cena za pobyt: {(180 - 180 * 1/10) * ilosc_nocy} PLN')
    elif ilosc_nocy >= 5:
        print(f'Cena za pobyt: {(150 - 150 * 1/10) * ilosc_nocy} PLN')