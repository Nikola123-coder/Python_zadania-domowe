"""
Napisz program, który wczytuje liczbę całkowitą,
a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`.
Np. dla parametru 3 powinno się wypisać:

```

    *

  * * *

* * * * *

```
"""




while True:
    wprowadzone_dane = int(input("Podaj liczbę całkowitą: "))

    if wprowadzone_dane != int:
        print("Nieprawidłowa liczba")
        continue

    liczba_calkowita = int(wprowadzone_dane)

    if liczba_calkowita == 0:
        print(' ')

    if liczba_calkowita > 0:
        print('*'* liczba_calkowita)




