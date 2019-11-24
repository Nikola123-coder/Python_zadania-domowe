'''
Napisz trzy programy, które dla podanych liczb:
wzrostu w cm i masy ciała w kg obliczą i wypiszą współczynnik BMI,
oraz podsumowanie informujące o stanie/zaleceniach.
(Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).
Programy mają różnić się sposobem interakcji z użytkownikiem.
'''

masa_ciała = int(input("Podaj swoją masę ciała (kg): "))
wzrost = float(input("Podaj swój wzrost (m): "))

współczynnik_BMI = masa_ciała/wzrost ** 2
print(f'Twoje BMI wynosi: {współczynnik_BMI}')

if współczynnik_BMI < 18.5:
    print("Niedowaga. Musisz przytyć")
elif 18.5 < współczynnik_BMI < 25:
    print("Waga prawidłowa")
elif 25 < współczynnik_BMI < 30:
    print("Nadwaga. Musisz schudnąć")
else:
    print("Otyłość. Udaj się do lekarza i dietetyka")
