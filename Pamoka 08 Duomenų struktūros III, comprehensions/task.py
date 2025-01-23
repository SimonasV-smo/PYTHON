#
# # 1task
#
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# kaupiklis = [elem * 2 for elem in num_list]
# print(kaupiklis)
#
# print('---------')
#
# kaupiklis1 = [elem ** 2 for elem in num_list]
# print(kaupiklis1)
#
# print('---------')
#
# price_list = [10, 15, 20, 25, 30]
# doller = [round(eu * 1.1, 1) for eu in price_list]
# print(doller)
#
# print('---------')
#
# message = [f'Kaina : {eu} EUR' for eu in price_list]
# print(message)

# # 2 task
#
# num_list = [1, 2, 3, 4, 5]
# kaupiklis = [[elem, elem ** 2, elem ** 3, elem % 2 == 0] for elem in num_list]
# print(kaupiklis)
#
# print('---------')
#
# num_list1 = [5, 8, 12, 18, 25, 30, 35, 40]
# kaupiklis1 = [elem for elem in num_list1 if elem > 20]
# print(kaupiklis1)
#
# print('---------')
#
# kaupiklis2 = [elem for elem in num_list1 if elem % 5 == 0]
# print(kaupiklis2)
#
# print('---------')
#
# kaupiklis3 = ['Lyginis' if elem % 2 == 0 else 'nelyginis' for elem in num_list1]
# print(kaupiklis3)
#

# 3 task

raides = ['A', 'B', 'C']
skaiciai = ['1', '2', '3']
#
# rez = [raid + skaic for raid in raides for skaic in skaiciai]
# print(rez)
#
# print('----------')
#
# rez2 = []
# for raid in raides:
#     for skaic in skaiciai:
#         index_sum = raides.index(raid) + int(skaic)
#         print(f"Raidė: {raid}, Skaičius: {skaic}, Indeksas: {raides.index(raid)}, Suma: {index_sum}")
#         if index_sum > 3:
#             rez2.append(raid + str(skaic))
#
# print(rez2)

# print('----------')
#
# rez3 = [raid.lower() + str(skaic) for raid in raides for skaic in skaiciai if int(skaic) % 2 == 0]
# print(rez3)

print('----------')

listas = [1, 2, 3, 2, 1, 4, 5, 5]

set_rez = {num for num in listas}
print(set_rez)

print('----------')

tuple_rez = tuple(num + 1 for num in listas)
print(tuple_rez)

print('----------')

dict_rez = {num: num}