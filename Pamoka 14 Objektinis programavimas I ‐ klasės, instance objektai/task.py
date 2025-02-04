#
# # 1 task
#
# class Car:
#     manufacturer = 'Audi'
#
# print(Car.manufacturer)
#
# class Bike:
#     manufacturer = 'Ducati'
#
# print(Bike.manufacturer)
#
# print('-' * 25)
#
# # 2task
#
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
# book1 = Book('1984', 'George Orwell', 1949 )
# book2 = Book('Everything Is F*cked', 'Mark Manson', 2019)
#
# print(
#     f'Knyga: "{book1.title}", autorius: {book1.author}, prasyta: {book1.year} metais.'
# )
# print(
#     f'Knyga: "{book2.title}", autorius: {book2.author}, prasyta: {book2.year} metais.'
# )
#
# print('-' * 25)
#
# # 3task
#
# class Book:
#     publisher = 'Penguin'
#
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
# book1 = Book('1984', 'George Orwell', 1949 )
# book2 = Book('Everything Is F*cked', 'Mark Manson', 2019)
#
# print(
#     f'Knyga: "{book1.title}", autorius: {book1.author}, leidejas : {Book.publisher}.'
# )
# print(
#     f'Knyga: "{book2.title}", autorius: {book2.author}, leidejas: {Book.publisher}.'
# )
#
# 4 task



class Book:
    publisher = 'Penguin'

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book_instance1 = Book('1984', 'George Orwell', 1949 )
book_instance2 = Book('Everything Is F*cked', 'Mark Manson', 2019)

print(book_instance1)
print(book_instance2)

print('-' * 25)

# 5task

from datetime import datetime

class Book:
    publisher = 'Penguin'

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_book_age(self):
        current_year = datetime.today().year
        return current_year - self.year

book_instance1 = Book('1984', 'George Orwell', 1949 )
age = book_instance1.get_book_age()
print(age)

book_instance2 = Book('Everything Is F*cked', 'Mark Manson', 2019)
age = book_instance2.get_book_age()
print(age)

print('-' * 25)

# 6task



class Book:
    publisher = 'Penguin'

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_book_age(self):
        current_year = datetime.today().year
        return current_year - self.year

book_instance1 = Book('1984', 'George Orwell', 1949 )
age = book_instance1.get_book_age()
print(f'Knyga <{book_instance1.title}> yra <{age}> metu senumo.')

book_instance2 = Book('Everything Is F*cked', 'Mark Manson', 2019)
age = book_instance2.get_book_age()
print(f'Knyga <{book_instance2.title}> yra <{age}> metu senumo.')

print('-' * 25)