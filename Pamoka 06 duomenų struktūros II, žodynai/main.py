#
#
# person_info = {
#     'name': 'Simonas',
#     'surname': 'Vismontas',
#     'languages': [
#         {
#             'name':'Lithuanian',
#             'level': 100
#         },
#         {
#             'name':'English',
#             'level': 75
#         },
#         {
#             'name': 'Russian',
#             'level': 30
#         },
#     ],
#     'occupation': {
#         'role': 'Full-Stack Developer',
#         'workplace': 'Internet',
#         'students': {
#             'student1': {
#                 'name': 'Darius'
#             },
#             'student2': {
#                 'name': 'Tomas'
#             }
#         }
#     }
# }

# print(person_info.get('name'))

# for key, value in person_info.items():
#     # print(f'Key: {key} value: {value}')
#     if type(value) == dict and value.get('students'):
#         print(value.get('students'))
#         for k, val in value.items():
#             print(f'Key: {k}, value: {val}')

# print(person_info['name'])
# print(person_info['surname'])
# print(person_info['languages'])
# print(person_info['languages'][0])
# print(person_info['languages'][1])

# print(
#     person_info['occupation']['students']['student1']['name']
# )

marke = 'Audi'
modelis = 'A6'
auto = {}

if marke == 'Audi':
    auto['marke'] = marke
auto['modelis'] = modelis
print(auto)

auto['marke'] = 'BMW'
auto['modelis'] = '5'

auto['colors'] = ['red', 'white', 'black']

car_technical_characteristics = {
    'engine': 3.0,
    'interior': 'Leather'
}

auto.update(car_technical_characteristics)
auto.update({
    'year': 2026,
    'eco2000': True
})

print(auto)

del auto['eco2000']
interior = auto.pop('interior')
print(f'Interior: {interior}')
# auto['gas_engine'] = auto.pop('engine')
auto['year'] = 2000
auto['year'] += 5
auto['colors'].append('yellow')
print(auto)



