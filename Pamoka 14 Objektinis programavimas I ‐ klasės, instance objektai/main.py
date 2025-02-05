# from datetime import datetime


# class House:
#     country = 'LT'
#
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
# house1 = House(199000, 2025)
# house2 = House(165000, 2008)
#
# house1.country = 'LV'
#
# print(
#     house1.country, house1.price, house1.year
# )
# print(
#     house2.country, house2.price, house2.year
# )
#
# class House:
#     country = 'LT'
#
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
#     def __str__(self):
#         print('123')
#
# house_instance1 = House(10_000, 1990)
# house_instance2 = House(12_000, 1920)
#
# print(house_instance1)
# print(house_instance2)
#
# from datetime import datetime
#
# class House:
#     country = 'LT'
#
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
#     def get_age(self):
#         current_year = datetime.today().year
#         return  current_year - self.year
#
# house_instance1 = House(10_000, 1990)
# age = house_instance1.get_age()
# print(age)
#
# house_instance2 = House(5_000_000, 2001)
# age = house_instance2.get_age()
# print(age)
#
# class House:
#     country = 'LT'
#
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
#     def __str__(self):
#         return f'Namas {self.year}, kaina - {self.price}, amzius {self.get_age()}'
#
#     def get_age(self):
#         return datetime.today().year - self.year

# book1 = House(10_000_000, 2024)
# print(book1)


# houses = [
#     House(22_000, 1980),
#     House(15_000, 1970),
#     House(10_000, 1960)
# ]

# for house in houses:
#     print(f'sena kaina: {house.price}')
#     house.price = round(house.price * 1.21)
#     print(f'nauja kaina: {house.price}')
#     print('-' * 40)

# for house in houses:
#     print(house)

from datetime import datetime


class House:
    country = 'LT'

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def __str__(self):
        return f'Namas {self.year} pastatymo, kaina - {self.price}, amžius {self.get_age()}'

    def get_age(self):
        return datetime.today().year - self.year

houses_kaupiklis = []
while True:
    year = int(input('Iveskite metus: '))
    price = int(input('Iveskite kaina: '))

    house_instance = House(price, year)
    houses_kaupiklis.append(house_instance)

    print('Spausdinam ka sukaupem:')
    for house in houses_kaupiklis:
        print(house)
