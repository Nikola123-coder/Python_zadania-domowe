"""
Zakładamy, że 1 ludzki rok, to 5 lat psich.

Za pomocą konsoli wczytaj imię i wiek psa.

Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.

Przykład:
Podaj imię psa - Burek
Podaj wiek psa - 3

Gdyby Burek był człowiekiem, miałby 15 lat.

"""

imie_psa = input("Podaj imię psa: ")
wiek_psa_w_latach_ludzkich = int(input("Podaj wiek psa: "))

wiek_psa = wiek_psa_w_latach_ludzkich * 5

print(f'Gdyby {imie_psa} był człowiekiem miałby {wiek_psa} lat')
