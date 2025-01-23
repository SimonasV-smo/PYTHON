# 1taks
# 1
#
# user_name = input('Įveskite savo vardą: ')
#
# user_age = int(input('Įveskite savo amžiū: '))
#
# print(f'Sveikas, {user_name}! Tau {user_age} metai.')
#
# name_lenght = len(user_name)
# print(f'Jusu vardas sudaro {name_lenght} simboliai.')
#
# if user_age >= 18:
#     print(f'{user_name} yra pilnametis.')
# else:
#     print(f'{user_name} yra nepilnametis.')
import locale

# # 2task
# kvadratas = 0
# suma = 0
# for skaiciai in range(2, 21, 2):
#      print(f'Lyginis skaicius: {skaiciai}')
#      kvadratas = skaiciai ** 2
#      print(f'Skaiciaus kvadratas: {kvadratas}')
#      suma += skaiciai ** 2
#      print(f'Kvadratu suma: {suma}')
#      print('------')
#
# for num in range(10, 0, -1):
#     print(num)

# # 3 task
#
# words = ['Obuolys', 'Kriaušė', 'Bananas', 'Vyšnia']
# print('|'.join(words))
# zodziai = ['Obuolys', 'Kriausė', 'Bananas', 'Vyšnia']
# indeksas = 1
#
# for zodis in zodziai:
#     if zodziai[-1] != zodis:
#         print(f'{indeksas}) {zodis}', end=', ')
#         indeksas += 1
#     else:
#         print(f'{indeksas} {zodis}')
#
# for word in words: print(word, end='  ')
#
# print('-------------')
# print('-------------')
#
# duomenys = [123, 'Labas', True, 45.6, None]
# for elementas in duomenys:
#     if isinstance(elementas, int):
#         print(elementas * 10)
#     elif isinstance(elementas, str):
#         print(elementas.upper())
#     elif isinstance(elementas, bool):
#         print("True arba False aptikta")
#     elif isinstance(elementas, float):
#         print(round(elementas, 2))
#
# 4task

num_list = [1.234, 3.14159, 2.71828, 0.57721]
res = [round(num, 3) for num in num_list]
print(res)

print('------------')

locale.setlocale(locale.LC_ALL, 'lt_LT')
word_list = ["Žalgiris", "Ąžuolas", "Lietuva", "Vilnius"]
res = sorted(word_list, key=locale.strxfrm)
print(res)

print('------------')

num_list1 = [10, 3, 7, 1, 15]
res = sorted(num_list1, reverse=True)
print(res)
