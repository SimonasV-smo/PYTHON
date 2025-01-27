
# # 1 task\\Ivadas i funkcija
#
# user_name = input('Jusu vardas: ')
# def sveikink():
#     for i in range(5):
#         print(f'Labas, {user_name}. Smagu tave matyti!')
#
# sveikink()

# 2 task\\ Argumentai ir return reiksmes

x = int(input('Pirmas daugiklis: '))
y = int(input('Atras daugiklis: '))

def sudaugink(x, y):
    rez = x * y
    print('rezultatas = ', rez )
sudaugink(x, y)
