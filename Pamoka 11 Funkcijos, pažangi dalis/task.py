#
# # 2task
#
# def sudeti_skaicius(*args):
#     return sum(args)
#
# print(sudeti_skaicius(5, 10, 15))        # 30
# print(sudeti_skaicius(100, 200, 300, 400)) # 1000
#
# # 3task
#
# def sveikinti_vardus(*args):
#     sveikinimai = []
#     for vardas in args:
#         sveikinimai.append(f'Sveiki, {vardas}!')
#     return '\n'.join(sveikinimai)
#
# print(sveikinti_vardus("Jonas", "Asta", "Mantas"))
#
# # 4task
#
# def pakelti_laipsniu(n, *args):
#     rezultatai = []
#     for sk in args:
#         rezultatai.append(sk ** n)
#     return rezultatai
#
#
# print(pakelti_laipsniu(2, 2, 3, 4))  # [4, 9, 16]
# print(pakelti_laipsniu(3, 1, 2, 3))  # [1, 8, 27]

#
# def spausdinti_zinute(kartai, *args, pabaiga = '!'):
#     for i in args:
#         for _ in range(kartai):
#             print(f'{i}{pabaiga}')
#
# spausdinti_zinute(3, 'Labas', 'Kaip gyvas', pabaiga='?')
# spausdinti_zinute(2, 'Laba diena', 'prasome iseiti is privacios valdos', pabaiga='!!!')
#
# def dauginti_skaicius(n, *args):
#     rezultatai = [n * sk for sk in args]
#     return rezultatai
#
# # Funkcijos iškvietimai
# print(dauginti_skaicius(2, 1, 2, 3))  # [2, 4, 6]
# print(dauginti_skaicius(3, 4, 5, 6))  # [12, 15, 18]
# print(dauginti_skaicius(10, 7, 8, 9)) # [70, 80, 90]
#
#
# def rodyti_duomenis(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k}: {v}")
#
# # Pavyzdys:
# rodyti_duomenis(vardas="Jonas", amzius=25)
# rodyti_duomenis()  # Nieko nespausdins, bet nebus ir tuščio "Nėra duomenų" pranešimo.
#
#
# def registruoti_naudotoja(vardas, el_pastas, **kwargs):
#     if '@' not in el_pastas:
#         raise ValueError("Netinkamas el. paštas")
#
#     duomenys = {'vardas': vardas.strip(), 'el_pastas': el_pastas.lower()}
#     if kwargs:
#         duomenys.update(kwargs)
#
#     print("Užregistruota:", duomenys)
#     return duomenys
#
#
# # Pavyzdys:
# registruoti_naudotoja("Asta", "asta@mail.com", miestas="Vilnius")
# registruoti_naudotoja("Marius", "marius@domain.com")  # Be papildomų duomenų
#
#
# def atspausdinti_lista(listas, **kwargs):
#     if not isinstance(listas, (list, tuple)):
#         raise TypeError("Reikalingas sąrašas arba tuple")
#
#     stilius = kwargs.pop('style', 'normal')
#
#     if stilius == 'bullet':
#         print("\n".join(f"• {x}" for x in listas), **kwargs)
#     elif stilius == 'numbered':
#         print("\n".join(f"{i}. {x}" for i, x in enumerate(listas, 1)), **kwargs)
#     else:
#         print(" ".join(map(str, listas)), **kwargs)
#
#
# # Pavyzdžiai:
# sarasas = ["Labas", "Pasauli"]
# atspausdinti_lista(sarasas, sep=" - ")
# atspausdinti_lista(sarasas, style="bullet")
# atspausdinti_lista(sarasas, style="numbered")
