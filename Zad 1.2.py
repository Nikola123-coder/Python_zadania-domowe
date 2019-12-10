'''
Napisz taki program: użytkownik ma podać,
w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1, wtorek to dzień 2 itp.).
Ma też podać, ile dni będzie trwała naprawa.

Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
Jeśli tak będzie ci wygodniej, możesz założyć,
że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.

'''

print("Pon = 1, wt = 2, śr = 3, czw = 4, pt = 5, sob = 6, ndz = 7")
dzień_oddania_butów = int(input("Buty zostały oddane do szewca w dniu: "))
czas_naprawy = int(input("Ile dni będzie trwała naprawa: "))

if czas_naprawy > 7:
    print("Nie ma takiej możliwości!")

if czas_naprawy <= 7:
    if dzień_oddania_butów + czas_naprawy == 8:
        print(1)
    elif dzień_oddania_butów + czas_naprawy == 9:
        print(2)
    elif dzień_oddania_butów + czas_naprawy == 10:
        print(3)
    elif dzień_oddania_butów + czas_naprawy == 11:
        print(4)
    elif dzień_oddania_butów + czas_naprawy == 12:
        print(5)
    elif dzień_oddania_butów + czas_naprawy == 13:
        print(6)
    elif dzień_oddania_butów + czas_naprawy == 14:
        print(7)
    else:
        print(f'Buty będą gotowe do odbioru: {dzień_oddania_butów + czas_naprawy}')



