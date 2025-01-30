
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

# Konkrečių klaidų (Exceptionų) gaudymas

while True:

    ivestis1 = input("Įveskite sveiką skaičių ")
    ivestis2 = input("Įveskite daliklį ")

    try:
        skaicius = int(ivestis1)
        daliklis = int(ivestis2)
        res = skaicius / daliklis
        print(f'rezultatas: {res}')
    except ValueError:
        print("Mes crashinom su ValueError")
        print("Paleiskite programą išnaujo ir ivestis padarykit kad tai būtų sveikas skaičius")
    except ZeroDivisionError:
        print("Mes crashinom su ZeroDivisionError")
        print("Pakeiskite daliklį iš 0 į kitą")

    print("Programa tęsia darbą")

# # try-except-else-finally struktūra
#             # Pavyzdys: else ir finally naudojimas
#
# try:
#     res = 100 / 0
# except ZeroDivisionError:
#     print("Dalyba iš 0 negalima")
# else:
#     print(res)
#
#             # Pavyzdys: Naudojant finally
#
# while True:
#     ivestis = input("Įveskite float skaičių")
#     try:
#         float_skaicius = float(ivestis)
#         print("Įvestis tinkama", float_skaicius)
#         break
#     except ValueError:
#         print("Įvestis NETINKAMA, pakartokite!!!")
#     finally:
#         print("Manęs niekaip neatsikratysit - FINALLY komanda")
#
# print("Programa tęsia darbą")