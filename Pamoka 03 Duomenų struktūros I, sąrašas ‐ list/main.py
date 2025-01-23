#
# # Create empty list
# sarasas = []
# print(type(sarasas))
# print(sarasas)
#
# # data to add to list
# men1 = 'sausis'
# men2 = 'vasaris'
#
# # use .append() to add element to the end of the list
# sarasas.append(men1)
# print(sarasas)
#
# sarasas.append(men2)
# print(sarasas)
#
# sarasas.append('kovas')
# print(sarasas)
#
# # .insert() add element to list by index
# sarasas.insert(0, 'balandis')
# sarasas.insert(-1, 'balandis')
# print(sarasas)
#
# sarasas.insert(2, 'birzelis')
# print(sarasas)
#
# # indexes in list
# print(sarasas[1])
# print(sarasas[1:])
# print(sarasas[1:3])
# print(sarasas[::2])
#
# # user.remove() to remove first element from list by object
# sarasas.remove('balandis')
# print(sarasas)
#
# # user.pop() to remove first element from list by object and index
# sarasas.pop()
# print(sarasas)
#
# ismestas = sarasas.pop(1)
# print(ismestas)
# print(sarasas)
#
# del sarasas[-1]
# print(sarasas)
#
from Tools.scripts.nm2def import export_list

# menesiai = ['sausis', 'vasaris', 'kovas', 'balandis']
#
# for elementas in menesiai:
#     print(elementas)
#     print(elementas.upper())
#     print('***')

# skaiciai = [10, 7, 50 , 11]

# suma = 0
# for elem in skaiciai:
#     print(suma)
#     suma += elem
#     print(suma)
#
#     print(suma)
#
# skaiciai = [10, 5, 50, 111]
# tuscias = []
#
# # len - listo ilgis, elementu skaicius
# print(len(skaiciai))
# print(len(tuscias))
#
# stringas = 'ABC'
# print(len(stringas))
#
# # sum - elementu suma
# print(sum(skaiciai))
# print(sum(tuscias))
#
# # max - didziausias skaicius
# print(max(skaiciai))
#
# # min - maziausiais skaicius
# print(min(skaiciai))

# month = ['sausis', 'vasaris', 'kovas', 'balandis', 'geguze', 'birzelis']
#
# print(
#     month[4][1:5:2]
# )
#
# print(
#     month[4][1:5:2].upper()
# )

# # indeksavimas
# print(month[0])
# print(month[2])
# print(month[-1])
#
# print('---------------')
#
# # slicinimas
# print(month[1:4])
# print(month[1:3 + 1])
# print(month[1:])
# print(month[:5])
#
# print('---------------')
#
# # zingsniai
# print(month[::3])
# print(month[::-1])
# print(month[::-2])
#
# print('---------------')
#
#
# months = ('sausis', 'vasaris', 'kovas', 'balandis', 'geguze', 'sausis', 'birzelis')
# print(id(months))
# print(id(months))
# months = months + ('lapkritis', 'gruodis')
# print(months)
# print(id(months))
# print(type(months))

# print(months[1])
# print(months[2])
# print(months[-1])
#
# print(months[1:3])
# print(months[3:5])

# del monts[-1]
# months[1] = 'spalis'

# print(months.index('kovas'))
# print(months.count('sausis'))

# months_str = 'sausis vasaris kovas'
# print(months_str)
#
# print('---------')
#
# months_list = months_str.split(' ')
# print(months_list)
# print('---------')
#
# months_list2 = months_str.split('i')
# print(months_list2)
#
# print('---------')
#
# joined_str = ', '.join(months_list)
# print(joined_str)
#
# print('---------')
#
# x_list = ['Adomas']
# print(', '.join(x_list))

numb1 = 100
numb2 = 500
numb3 = 100

print(numb1 < numb2)
print(numb1 > numb2)
print(numb1 == numb3)
print(numb1 != numb3)

