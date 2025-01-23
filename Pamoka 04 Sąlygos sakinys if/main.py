# salygos
#
# numb1 = 100
# numb2 = 500
# numb3 = 100
#
# char = 'A'
# text = 'ABCD'
# text2 = 'QWER'
#
# name = 'John'
# names_list = ['Donald', 'Darius', 'Ona']
#
# print(
#     name in names_list
# )

#
# print(
#     char in text
# )
# print(
#     char in text2
# )
# print(
#     '0' in text
# )
# a = numb1 == numb2
# print(type(a))
# print(type(a) is bool)
# print(type(numb1) is bool)
#
# print(type(numb1))
# print(type(numb1) is int)

# print(numb1 < numb2)
# print(numb1 > numb2)
# print(numb1 == numb3)
# print(numb1 != numb3)
# print(numb1 >= numb3)
# print(numb1 <= numb2)


# num1 = 100
# num2 = 500
# num3 = 300
#
# if num2 > num3 > num1:
#     print(f"{num1} yra mazesnis uz {num2}")
# else:
#     print('else')

# num1 = 100
# num2 = 500
# num3 = 300
#
# if num1 < num2 and num1 == 100:
#     print("true")
#
# if num1 < num2 or num1 == 100:
#     print("true")
#
# if not True:
#     print("true")

# auto = 'Audi'
# autos_ger = ['BMW', 'Audi', 'Mercedes']
# autos_it = ['Ferrari', 'Lamborghini']
# auto_sport = ['BMW', 'Ferrari']
#
# if (auto in autos_ger or auto in autos_it) and auto in auto_sport:
#
#     print(f'{auto} yra vokiskas arba italiskas sportinis automobilis.')
#
# num4 = 9
# rez = ''
# if num4 % 2 == 0:
#     rez = 'Lygus'
# else:
#     rez = 'nelygus'
# print(rez)
#
# print('-------------')
# num4 = 8
# rez = 'lygus' if num4 % 2 == 0 else ('nelygus')
# print(rez)
#
# # 'lygus' jei true kitu atveju 'nelygus'

miestas1 = 'Vilnius'
miestas2 = 'Kaunas'
#
# print(miestas1.istitle())
#
# if miestas1.istitle():
#     print('vartotojas ivede miesto pavadinima.')
#
# print(miestas2.isupper())

print(miestas1.startswith('V'))
print(miestas2.startswith('V'))

ak = '39803272685'
user_gender = ''
if ak.startswith('3'):
    user_gender = 'Vyras'
elif ak.startswith('4'):
    user_gender = 'Moteris'
else:
    print('Neteisingas AK')

