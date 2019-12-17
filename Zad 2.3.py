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

liczby = []

while len(liczby) < 8:
    liczba = int(input("Podaj liczbę: "))
    liczby.append(liczba)

print(liczby)
print(f'Ilość liczby: {len(liczby)}')

srednia = sum(liczby)/len(liczby)
print(f'Suma liczb: {sum(liczby)}')
print(f'Średnia liczb: {srednia}')

print(f'Minimum: {min(liczby)}')
print(f'Minimum: {max(liczby)}')

