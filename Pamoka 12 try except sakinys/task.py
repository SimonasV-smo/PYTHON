
# # 2
#
# def dalinti(a: (int, float), b: (int, float)) -> (float, str):
#     try:
#         return a / b
#     except Exception as e:
#         return 'Dalyba is nulio negalima'
#
# # dalinti = lambda a, b: a/b
#
# print(dalinti(10, 2))
# print(dalinti(5, 0))
# print(dalinti(8, 4))

# # 3
#
# while True:
#     skaicius1 = input('Iveskite sveika skaiciu: ')
#     skaicius2 = input('Iveskite dalikli: ')
#
#     try:
#         skaicius = int(skaicius1)
#         daliklis = int(skaicius2)
#         res = skaicius / daliklis
#         print(f'{skaicius} / {daliklis} = {res}')
#     except ValueError:
#         print('Ivestas ne skaicius...')
#         print('Prasome paleisti programa is naujo ir ivesti sveika skaiciu :)')
#     except ZeroDivisionError:
#         print('Dalyba is 0 negalima...')
#         print('Prasome pakeisti daliki is 0 i betkuri kita :)')
#
#     print('-' *20)

# # 4
#
# while True:
#     skaicius = input('Iveskite skaiciu: ')
#     try:
#         int_skaicius = int(skaicius)
#         print('Ivestas skaicius tinkamas')
#     except ValueError:
#         print('Ivestas ne skaicius, perkraukite ir naudokite skaiciu.')
#         break
#     else:
#         print(f'Konversija sekminga: {int_skaicius}')
#     finally:
#         print('programa baige darba')

# # 5
#
#
#
# def amziaus_tikrinimas(amzius):
#     if amzius < 0:
#         raise ValueError('amzius negali buti neigiamas')
#     elif amzius >= 18:
#         print('Vartotojas pilnametis')
#     else:
#         print('Varotojas nepilnametis')
#
# amziaus_tikrinimas(15)
# amziaus_tikrinimas(20)
# amziaus_tikrinimas(-5)
