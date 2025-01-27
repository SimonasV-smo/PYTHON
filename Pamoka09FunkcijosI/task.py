
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