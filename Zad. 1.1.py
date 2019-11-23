'''
Napisz program, który prosi użytkownika (przez `input()`), żeby podał,
ile kosztuje kilo ziemniaków. Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za pięć kilo ziemniaków.

Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
ile kosztuje kilo ziemniaków i ile kilo chce kupić. Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za te ziemniaki.

Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić,
ile kosztuje kilo bananów i ile kilo bananów chce kupić.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
I niech program sprawdzi i powie,
za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.

'''

cena_za_kg_ziemniaków = float(input("Podaj ile kosztuje kilogram ziemniaków: "))
ile_kg_ziemniaków = int(input("Podaj ile kg ziemniaków chcesz kupić: "))
cena_za_kg_bananów = float(input("Podaj ile kosztuje kilogram bananów: "))
ile_kg_bananów = int(input("Podaj ile kg bananów chcesz kupić: "))

#cena_za_5kg_ziemniaków = cena_za_kg_ziemniaków * 5 - do części I zadania
#suma = cena_za_kg_ziemniaków * ile_kg_ziemniaków - do części II zadania

#print(f'Cena za 5kg ziemniaków wynosi: {cena_za_5kg_ziemniaków}') - do części I zadania

suma_1 = cena_za_kg_ziemniaków * ile_kg_ziemniaków
suma_2 = cena_za_kg_bananów * ile_kg_bananów

suma = suma_1 + suma_2
print(f'Do zapłaty: {suma}')

if suma_1 > suma_2:
    print("Ziemniaki są droższe")
elif suma_2 > suma_1:
    print("Banany są droższe")
else:
    print("Cena bananów i ziemniaków jest taka sama")