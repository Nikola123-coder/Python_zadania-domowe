"""
Przy pomocy `input()` zapytaj użytkownika co chce kupić,
jaką ilość towaru chce kupić i jaka jest jego cena.
Wyświetl odpowiedni komunikat.

Przykład:
Co chcesz kupić? - ziemniaki
Podaj cenę towaru - 5
Podaj ilość towaru - 10

Za ziemniaki, który chcesz kupić, zapłacisz 50 zł

"""

towar = input("Co chcesz kupić?: ")
cena_towaru = float(input("Cena towaru za sztukę?: "))
ilosc_towaru = int(input("Ile sztuk?: "))

suma = cena_towaru * ilosc_towaru

print(f'Cena za towar wynosi: {suma: .2f} PLN')


