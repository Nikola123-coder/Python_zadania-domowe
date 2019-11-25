"""
Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
(np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą,
oblicza pole powierzchni trójkąta o takich bokach.

Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).

Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:

```
import math

x = math.sqrt(10)
```

"""

liczba_pierwsza = int(input("Podaj pierwszą liczbę: "))
liczba_druga = int(input("Podaj drugą liczbę: "))
liczba_trzecia = int(input("Podaj trzecią liczbę: "))

