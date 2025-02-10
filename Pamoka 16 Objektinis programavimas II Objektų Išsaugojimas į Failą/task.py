#
# # 3 komponavimas
#
# class Variklis:
#     def __init__(self, galia):
#         self.galia = galia
#
#     def startuoti(self):
#         print(f'Variklis veikia su galia: {(self.galia)} arklio galių.')
#
# variklis = Variklis(180)
# variklis.startuoti()
# print('-' * 25)
#
# class Automobilis:
#     def __init__(self, marke, modelis, variklis):
#         self.marke = marke
#         self.modelis = modelis
#         self.variklis = variklis
#
#     def vaziuot(self):
#         print(f'{self.marke} {self.modelis} pradeda važiuoti.')
#         self.variklis.startuoti()
#
#
# variklis1 = Variklis(250)
# automobilis1 = Automobilis('Mercedes-Benz', "SL600", variklis1)
#
# variklis2 = Variklis(200)
# automobilis2 = Automobilis('BMW', "530", variklis2)
#
# automobilis1.vaziuot()
# print('-' * 25)
# automobilis2.vaziuot()

# 4 task
#
# class Asmuo:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#
# class Darbuotojas(Asmuo):
#     def __init__(self, vardas, amzius, pareigos):
#         super().__init__(vardas, amzius)
#         self.pareigos = pareigos
#
#     def __str__(self):
#         return f"Vardas: {self.vardas}, Amžius: {self.amzius}, Pareigos: {self.pareigos}"
#
#
# darbuotojas = Darbuotojas('Simonas', 26, 'Programuotojas')
# print(darbuotojas)
#
# # 5 task
#
# class TransportoPriemone:
#     def judeti(self):
#         print('Transporto priemone juda.')
#
# class Dviratis(TransportoPriemone):
#     def judeti(self):
#         print('Dviratis vaziuoja pedalais')
#
# transportas = TransportoPriemone()
# dviratis = Dviratis()
#
# transportas.judeti()
# dviratis.judeti()