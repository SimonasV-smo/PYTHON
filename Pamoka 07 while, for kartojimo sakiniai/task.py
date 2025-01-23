#
# # 1 task
#
# sum = 0
#
# while True:
#     user_input = input('iveskite skaiciu nuo 1 iki 10: ')
#     if not user_input.isdigit():
#         print("ivestas neskaicius arba ne intervalo dalis")
#         continue
#
#     number = int(user_input)
#     if number < 1 or number > 10:
#         print('blogas intervalas.')
#         continue
#     if number == 5:
#         print(f'ivedete {number} ciklo pabaiga.')
#         break
#     sum += number
#     print(f'skaiciu neskaiciaujant 5 suma: {sum}')

# # 2task
#
# skaiciai = [5, 7, 15, 6, 3, 20, 12]
#
# for skaicius in skaiciai:
#     if skaicius > 10:
#         break
#     if skaicius % 2 == 0 or skaicius % 5 == 0:
#         print(skaiciai)
#
# skaiciai1 = [-10, -5, 0, 5, 10, 15, 20]
#
# teigiama_suma = 0
# neigiama_suma = 0
# maksimalus = skaiciai1[0]
# minimalus = skaiciai1[0]
#
# for skaicius1 in skaiciai1:
#     if skaicius1 > 0:
#         teigiama_suma += skaicius1
#     elif skaicius1 < 0:
#         neigiama_suma += skaicius1
#     if skaicius1 > maksimalus:
#         maksimalus = skaicius1
#     if skaicius1 < minimalus:
#         minimalus = skaicius1
#
# print(f'teigiamu skaiciu sum: {teigiama_suma}')
# print(f'neigiamu skaiciu sum: {neigiama_suma}')
# print(f'didziausias skaicisu: {maksimalus}')
# print(f'maziausiais skaicius: {minimalus}')

# 3task

list = [1, 3, 5, 7, 8, 10, 11]

for elem in list:
    if elem % 2 == 0:
        print(f'pirmas lyginis skaicius yra: {elem}')
        break
    else:
        print(f'{elem} nera lyginis')

