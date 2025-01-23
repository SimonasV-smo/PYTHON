
# # task 1
#
#
# school_info = {
#     'name': 'Gabijos gimnazija',
#     'mokytojas1_vardas': 'Jonas',
#     'mokytojas1_pavarde': 'Jonaitis',
#     'mokytojas1_mokomas_dalykas': 'Fizika',
#     'mokytojas2_vardas': 'Aldona',
#     'mokytojas2_pavarde': 'Aldoniene',
#     'mokytojas2_mokomas_dalykas': 'Chemija',
#     'mokytojas3_vardas': 'Jurga',
#     'mokytojas3_pavarde': 'Spurga',
#     'mokytojas3_mokomas_dalykas': 'Daile',
#     'mokiniu_skaicius': 1500,
# }
#
# # Išspausdinkite pirmo mokytojo vardą ir mokomą dalyką
# print(f"Pirmo mokytojo vardas: {school_info['mokytojas1_vardas']}, jo mokomas dalykas {school_info['mokytojas1_mokomas_dalykas']}")
#
# # Patikrinkite, ar mokykloje yra daugiau nei 500 mokinių
# if school_info['mokiniu_skaicius'] > 500:
#     print("Mokykloje yra daugiau nei 500 mokinių.")
# else:
#     print("Mokykloje yra 500 arba mažiau mokinių.")
#
#
# print('----------------')
# # 2
#
#
# company = {
#     "name": "TechCorp",
#     "employee1_name": "Jurgis",
#     "employee1_role": "Junior Developer",
#     "employee1_salary": 1100,
#     "employee2_name": "Agata",
#     "employee2_role": "Graphic Designer",
#     "employee2_salary": 2500,
#     "employee3_name": "Tadas",
#     "employee3_role": "Manager",
#     "employee3_salary": 4000,
#     "location": "Klaipeda",
#     "industry": "IT"
# }
#
#
# print(f"Vardas: {company['employee1_name']}, Pareigos: {company['employee1_role']}")
# print(f"Vardas: {company['employee2_name']}, Pareigos: {company['employee2_role']}")
# print(f"Vardas: {company['employee3_name']}, Pareigos: {company['employee3_role']}")
#
#
# average_salary = (company["employee1_salary"] + company["employee2_salary"] + company["employee3_salary"]) / 3
# print(f"Vidutinis atlyginimas: {round(average_salary, 2)}")
#
#
# if "location" in company:
#     print(f"Įmonės vieta: {company['location']}")
# else:
#     print("Raktas 'location' nėra žodyne.")
#
# print('----------------')
# # 3
#
#
#
# biblioteka = {
#     "knyga1_pavadinimas": "1984",
#     "knyga1_autorius": "George Orwell",
#     "knyga1_kopijos": 3,
#     "knyga2_pavadinimas": "To Kill a Mockingbird",
#     "knyga2_autorius": "Harper Lee",
#     "knyga2_kopijos": 5,
#     "knyga3_pavadinimas": "The Great Gatsby",
#     "knyga3_autorius": "F. Scott Fitzgerald",
#     "knyga3_kopijos": 2,
#     "vieta": "Kaunas",
#     "darbo_valandos_pradzia": "8:00",
#     "darbo_valandos_pabaiga": "20:00"
# }
#
#
# print(f"Knygos pavadinimas: {biblioteka['knyga1_pavadinimas']}, autorius: {biblioteka['knyga1_autorius']}")
# print(f"Knygos pavadinimas: {biblioteka['knyga2_pavadinimas']}, autorius: {biblioteka['knyga2_autorius']}")
# print(f"Knygos pavadinimas: {biblioteka['knyga3_pavadinimas']}, autorius: {biblioteka['knyga3_autorius']}")
#
#
# kopiju_sarasas = [biblioteka['knyga1_kopijos'], biblioteka['knyga2_kopijos'], biblioteka['knyga3_kopijos']]
# maziausia_kopiju = min(kopiju_sarasas)
# if maziausia_kopiju == biblioteka['knyga1_kopijos']:
#     print(f"Knyga su mažiausiai kopijų: {biblioteka['knyga1_pavadinimas']}")
# elif maziausia_kopiju == biblioteka['knyga2_kopijos']:
#     print(f"Knyga su mažiausiai kopijų: {biblioteka['knyga2_pavadinimas']}")
# else:
#     print(f"Knyga su mažiausiai kopijų: {biblioteka['knyga3_pavadinimas']}")

# 4task
import pprint
store = {
    'name': 'E-Shop',
    'categories': ['Electronics', 'Books', 'Clothing'],
    'products': [
        {'name': 'Laptop', 'price': 1000, 'stock': 10},
        {'name': 'Book', 'price': 20, 'stock': 50},
        {'name': 'T-shirt', 'price': 15, 'stock': 100}
    ],
    'rating': 4.5
}

store['categories'].remove('Clothing')
pprint.pprint(store['categories'])

for product in store['products']:
    if product['price'] > 50:
        product['price'] *= 0.95
    if product['name'] == 'Laptop':
        product['stock'] = 15
pprint.pprint(store['products'])

if store['rating'] < 4.6:
    store['rating'] += 0.1
pprint.pprint(store['rating'])

