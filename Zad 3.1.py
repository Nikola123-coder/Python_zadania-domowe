'''
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

​

1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,

2. `max` - zwraca większą z dwóch liczb,

3. `srednia` - oblicza średnią z dwóch liczb,

4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)

podpowiedź: wartość PI jest dostępna jako `Math.PI`

5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.

6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.

7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile

8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

​

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik
'''

#1
def ile_metrow (st) -> float:
    '''

    :param st:
    :return:
    '''

    return st/0.3

wynik = ile_metrow(6)
print(wynik)


#2
def wieksza (a, b) -> float:
    '''

    :param a:
    :param b:
    :return:
    '''
    return max(a, b)

wynik = wieksza(5, 23)
print(wynik)

#3
def srednia(a, b) -> float:
    '''

    :param a:
    :param b:
    :return:
    '''
    return (a + b)/2

wynik = srednia(38, 87)
print(wynik)

#4 Pole koła = PI *r**2

import math
math.pi

def pole_kola (r) -> float:
    '''

    :param r:
    :return:
    '''
    return math.pi * r**2


wynik = pole_kola(4.5)
print(wynik)

#5 bmi
def BMI(wzrost, waga) -> float:
    '''

    :param wzrost:
    :param waga:
    :return:
    '''
    return waga/wzrost**2

wynik = BMI(1.80, 83)
print(wynik)

#6 pole trójkąta
#import math
#math.sqrt()

#def pole_trojkata(a, b, c, p) ->float:
 #   '''

 #   :param a:
 #   :param b:
 #   :param c:
 #   :param p:
 #  :return:
 #   '''
#    return math.sqrt(p(p - a)(p - b)(p - c))
#    p = (a + b + c) / 2


#wynik = pole_trojkata(11, 6, 9, (11 + 6 + 9)/2)
#print(wynik)

#7 km na mile
def ile_mil(km) -> float:
    '''

    :param km:
    :return:
    '''
    return km*0.6

wynik = ile_mil(379)
print(wynik)

#8 mile na km
def ile_km(mi) -> float:
    '''

    :param mi:
    :return:
    '''
    return mi*1.6

wynik = ile_km(500)
print(wynik)