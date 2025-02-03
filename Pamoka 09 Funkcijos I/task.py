
# # 1 task\\Ivadas i funkcija
#
# user_name = input('Jusu vardas: ')
# def sveikink():
#     for i in range(5):
#         print(f'Labas, {user_name}. Smagu tave matyti!')
#
# sveikink()

# # 2 task\\ Argumentai ir return reiksmes
#
# x = int(input('Pirmas daugiklis: '))
# y = int(input('Atras daugiklis: '))
#
# def sudaugink(x, y):
#     rez = x * y
#     print('rezultatas = ', rez )
# sudaugink(x, y)

# # 3. Funkcijos su keliais argumentais
# # task 3
#
# def trys_sveikinimai(vardas1, vardas2, vardas3):
#     sveikinimas = f'Labas, {vardas1}! Labas, {vardas2}! Labas, {vardas3}!'
#     return sveikinimas
#
# res = trys_sveikinimai('Simonas', 'Antanas', 'Jurgis')
# print(res)
#
# print('-----------')
#
# # 4. Numatytosios reikšmės ir keyword argumentai
# # Užduotis 4:
#
# def sveikink_su_pavadinimu(vardas, pavadinimas='bičiuli'):
#     sveikinimas = f'Sveikas, {vardas}! Ka veiki, {pavadinimas}?'
#     return sveikinimas
#
# res = sveikink_su_pavadinimu('Simonas')
# print(res)

# Loginiai jungikliai funkcijose
# Užduotis 5:

def skaiciuoti_sumos_tipa(x, y, tik_teigiama=False):
    suma = x + y
    if tik_teigiama:
        return max(suma, 0)
    return suma


print(skaiciuoti_sumos_tipa(5, 10))
print(skaiciuoti_sumos_tipa(-5, -10))
print(skaiciuoti_sumos_tipa(-5, -10, True))
print(skaiciuoti_sumos_tipa(5, -10, True))

# Docstringai funkcijose
# Užduotis 6:

def vidurkis(num):
    """
    Apskaičiuoja ir grąžina sąrašo skaičių vidurkį.

    Argumentai:
    num (list): Sąrašas skaičių, kurių vidurkį norite apskaičiuoti.

    Grąžinama reikšmė:
    float: Skaičių vidurkis.

    Pastabos:
    Jei sąrašas yra tuščias, grąžinama reikšmė yra 0.0.
    """
    if not num:
        return 0.0
    suma = sum(num)
    avg = suma / len(num)
    return avg

print(vidurkis([10.5, 20.25, 30.75, 40.0, 50.5]))
print(vidurkis([-10.5, 20.75, -30.0, 40.25]))
print(vidurkis([]))

# Type hints ir anotacijos
# Užduotis 7:

def prideti_prie_galo(tekstas: str, zodis: str) -> str:
    """
    Prideda žodį prie sakinio galo.

    Argumentai:
    tekstas (str): Sakinys, prie kurio reikia pridėti žodį.
    zodis (str): Žodis, kurį reikia pridėti prie sakinio galo.

    Grąžinama reikšmė:
    str: Sakinys su pridėtu žodžiu gale.
    """
    return tekstas + " " + zodis


sakinys1 = prideti_prie_galo('Aš mokausi programavimo', 'dabar')
print(sakinys1)

sakinys2 = prideti_prie_galo('Jis mėgsta skaityti knygas', 'visada')
print(sakinys2)
