"""
Założenia:

- 0-6   - wiek przedszkolny - cena biletu: 0

- 7-17  - wiek szkolny      - cena biletu: 2.28

- 18-64 - wiek dorosły      - cena biletu: 3.80

- +65   - wiek emerytalny   - cena biletu: 1.90

Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.

Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić.
Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.
"""

wiek = int(input("Ile masz lat?: "))
ilosc_biletow = int(input("Ile chcesz kupić biletów?: "))

if 0 <= wiek <= 6:
    print(f'Cena wynosi: {0}')
elif 7 <= wiek <= 17:
    print(f'Cena wynosi: {2.28 * ilosc_biletow: .2f}')
elif 18 <= wiek <= 64:
    print(f'Cena wynosi: {3.80 * ilosc_biletow: .2f}')
else:
    print(f'Cena wynosi: {1.90 * ilosc_biletow: .2f}')


