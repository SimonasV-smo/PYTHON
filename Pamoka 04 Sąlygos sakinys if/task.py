

# 2task

# skaicius1 = int(input("iveskite pirma skaiciu: "))
# skaicius2 = int(input("iveskite anra skaiciu: "))
#
# print(skaicius1 > skaicius2)
# print(skaicius1 < skaicius2)
# print(skaicius1 == skaicius2)
#
#
# skaicius = int(input("iveskite skaiciu: "))
#
# print(skaicius % 2 == 0)
# print(skaicius % 2 != 0)
#
# zodziai = ["katė", "šuo", "namas", "automobilis", "kompiuteris"]
#
# ivestas = input("iveskite zodi: ")
#
# print(ivestas in zodziai)

# 3task

# amzius = int(input("iveskite amziu: "))
#
# if amzius >= 18:
#     print("Pilnametis")
# else:
#     print("Nepilnametis")
#
# temp = int(input("iveskite temperatura: "))
#
# if temp < 0:
#     print("Salta")
# if 20 >= temp >= 0:
#     print("vidutiniska")
# if temp > 20:
#     print("silta")

# 4 task

# balas = int(input("iveskite bala nuo 0 iki 10: "))
#
# if 0 <= balas <= 4:
#     print("Nepatenkinamas")
# elif 5 <= balas <= 7:
#     print("vidutinis")
# elif 8 <= balas <= 10:
#     print("puikus")
# else:
#     print("error, write up to 10")
#
# pasirinikimas = input("pasirinkite metu laika: ")
#
# if pasirinikimas == 'ziema':
#     print("gruodis, sausis, vasaris")
# elif pasirinikimas == 'pavasaris':
#     print("kovas, balandis, geguze")
# elif pasirinikimas == 'vasara':
#     print("birzelis, liepa, rugpjutis")
# elif pasirinikimas == 'ruduo':
#     print("rugsejis, spalis, lapkritis")
# else:
#     print("pasirinktas ne metu laikas.")

# 5task
#
# user_num1 = int(input("pirmas skaicius: "))
# user_num2 = int(input("antras skaicius: "))
#
# if user_num1 > 0 and user_num2 > 0:
#     print("abu skaiciai yra teigiami")
# else:
#     print("vienas is operatoriu neigiamas.")
#
# if user_num1 < 0 or user_num2 < 0:
#     print("vienas is operatoriu neigiamas.")
# else:
#     print("abu operatoriai teigiami.")
#
# autos = ["BMW", "Audi", "Mersedes-benz"]
# make = ["M3", "RS6", "GT"]
#
# user_auto = input("pasirinkite automobilio marke: ")
#
# if user_auto in autos :
#     print(f"pasirinkimas {user_auto} yra sarase.")
# else:
#     print(f"pasirinkimo {user_auto} nera sarase.")
#
# user_make = input("pasirinkite modeli: ")
#
# if user_make in make :
#     print(f"pasirinkimas {user_make} yra vokisku automobiliu sarase")
# else:
#     print(f"pasirinkimas {user_make} nera sportiniame automobiliu sarase.")

# 6task

# num = float(input('iveskite skaiciu: '))
# rez = 'teigiamas' if num >= 0 else 'neigiamas'
# print(rez)

# user_input = str(input("iveskite teksta: "))
#
# if user_input.istitle():
#     print('prasideda didziaja raide')
# else:
#     print('prasieda mazaja raide')

# 7task
# 1

# user_input = str(input("iveskite teksta: "))
#
# if user_input.istitle():
#     print('prasideda didziaja raide')
# else:
#     print('prasieda mazaja raide')
#
# if user_input.isupper():
#     print('sudaryta is didziuju raidziu')
# else:
#     print('sudaryta is mazuju raidziu')

# 2

user_input = str(input('jusu teksto dalis: '))

if user_input.startswith('S'):
    print('tekstas prasideda "S" raide ')
else:
    print('tekstas prasideda kita raide.')

if user_input.isupper():
    print('tekstas sudarytas didziosiomis raidemis.')
else:
    print('tekstas sudarytas mazosiomis raidemis.')