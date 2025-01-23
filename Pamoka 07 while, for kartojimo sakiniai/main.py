#
# a = True
# while a:
#     print('123')
#     break

# objektas = [1, 2, 3, 4, 5]
# for elementas in objektas:
#     if elementas == 2:
#         continue
#     print(elementas)

# while True:
#     user_input = input('Provide number: ')
#     if user_input == 'stop':
#         break
#     print(f'Your number {user_input}')

# while True:
#     print('kartojimo pradzia')
#     print('1. sis meniu punktas nedaro nieko \n'
#           '2. iseitis is kartojimo bloko\n'
#           '3. vel parodyti meniu')
#     pasirinkimas = input('pasirinkimas: ')
#     if pasirinkimas == '2':
#         break
#     elif pasirinkimas == '3':
#         continue
#     else:
#         print('nieko nebuvo pasirinkta')
#     print('kartojimo pabaiga')

# while True:
#     print('1. atlikti skaičiaus daugybą\n2. išeiti')
#     pasirinkimas = input()
#     if pasirinkimas == '2':
#         break
#     if pasirinkimas == '1':
#         # daugyba tesis, kol nebus paspausta q
#         while True:
#             print('Įvesti skaičių daugybai iš 100 arba q - grįžti')
#             ivestis = input()
#             if ivestis == 'q':
#                 break
#             elif not ivestis.isdigit():
#                 print('Įvestas ne skaičius!!!')
#                 continue
#             skaicius = int(ivestis) * 100
#             print('Daugybos iš 100 rezultatas -', skaicius)

listas = ['sausis','vasaris', 'kovas', 'balandis', 'geguze', 'birzelis']

for elem in listas:
    if elem == 'balandis':
        break
    print(elem)

print('-----------')

for elem in listas:
    if elem == 'sausis':
        continue
    print(elem)

print('-----------')

obj = {'product1': {'amount': 200}, 'product2': {'amount': 0}, 'product3': {'amount': 2}}

for key, value in obj.items():
    if value['amount'] < 1:
        continue

#
# for skaicius in range(1, 5):
#     if skaicius ==
