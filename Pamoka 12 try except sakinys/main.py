
# # Pagrindinis try-except pavyzdys
#
# ivestis = '4'
# try:
#     skaicius = int(ivestis)
#     res = skaicius / 0  # šis veiksmas sukels klaidą
# except Exception as e:
#     print("Mes crashinom, tačiau suvaldėm crashą")
#     print(e.__class__)  # išspausdina klaidos klasę
#     print(e)  # išspausdina klaidos pranešimą
#
# print("Programa tęsia darbą")

# # Konkrečių klaidų (Exceptionų) gaudymas
#
# while True:
#
#     ivestis1 = input("Įveskite sveiką skaičių ")
#     ivestis2 = input("Įveskite daliklį ")
#
#     try:
#         skaicius = int(ivestis1)
#         daliklis = int(ivestis2)
#         res = skaicius / daliklis
#         print(f'rezultatas: {res}')
#     except ValueError:
#         print("Mes crashinom su ValueError")
#         print("Paleiskite programą išnaujo ir ivestis padarykit kad tai būtų sveikas skaičius")
#     except ZeroDivisionError:
#         print("Mes crashinom su ZeroDivisionError")
#         print("Pakeiskite daliklį iš 0 į kitą")
#
#     print("Programa tęsia darbą")

# try-except-else-finally struktūra
#             Pavyzdys: else ir finally naudojimas

try:
    res = 100 / 0
except ZeroDivisionError:
    print("Dalyba iš 0 negalima")
else:
    print('Gerb. useri, stai jusu rezultatas : {res}')

            # Pavyzdys: Naudojant finally

while True:
    ivestis = input("Įveskite float skaičių")
    try:
        float_skaicius = float(ivestis)
        print("Įvestis tinkama", float_skaicius)
        break
    except ValueError:
        print("Įvestis NETINKAMA, pakartokite!!!")
    finally:
        print("Manęs niekaip neatsikratysit - FINALLY komanda")

print("Programa tęsia darbą")

def create_user(user_data: dict):
    print('User created!')

users_to_create = {
    'user1': {'name': 'Darius', 'aka': 123456789},
    'user2': {'name': 'Tomas', 'aka': 123456789123489},
    'user3': {'name': 'Adomas', 'aka': 12345678123412349},
}

created_users = {}
for user_key, user_info in users_to_create.items():
    try:
        create_user(user_info)
    except Exception as e:
        print(e)
    finally:
        created_users[user_key] = user_info
        print(f'User {user_key} already created with values {user_info}')