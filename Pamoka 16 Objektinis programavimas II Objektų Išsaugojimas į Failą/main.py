#
# class Asmuo:
#     def __init__(self, vardas, pavarde, gim_metai):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.gim_metai = gim_metai
#
# class MokinioTevas(Asmuo):
#     def __init__(self, vardas, pavarde, gim_metai, darboviete):
#         super().__init__(vardas, pavarde, gim_metai)
#         self.darboviete = darboviete
#
# tevas = MokinioTevas(vardas="Jonas", pavarde="Petraitis", gim_metai=1975, darboviete="ABC įmonė")
#
# print(tevas.vardas)
# print(tevas.pavarde)
# print(tevas.gim_metai)
# print(tevas.darboviete)
#
# class Mygtukas:
#     def deaktyvuoti(self):
#         print('mygtukas deaktyvuotas')
#
# class RaudonasMygtukas(Mygtukas):
#     def deaktyvuoti(self):
#         super().deaktyvuoti()
#         print('aciu kad dirbote')
#         print('spava pasikeitei i rausva')
#
# red_btn = RaudonasMygtukas()
# red_btn.deaktyvuoti()
#
#
# import pickle
#
# import datetime
#
# class House:
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
#     def get_age(self):
#         now = datetime.datetime.today()
#         current_year = now.year
#         return current_year - self.year
#
#     def __str__(self):
#         return f'Namas {self.year} pastatytas, kaina {self.price}, amzius {self.get_age()}'
#
#
# try:
#     with open('namai.pickle', mode='rb') as f:
#         houses_kaupiklis = pickle.load(f)
# except:
#     houses_kaupiklis = []
# while True:
#     print('1. Show all houses')
#     print('2. Add house')
#     print('3. Remove last house')
#     print('4. Exit')
#     print('\n')
#     try:
#         user_input = int(input('Please choose action number: '))
#     except ValueError:
#         raise ValueError('Please select number from 1 to 4')
#
#
# new_house = House(90_000, 2024)
# houses_kaupiklis.append(new_house)
#
# with open('namai.pickle', mode='wb') as f:
#     pickle.dump(houses_kaupiklis, f)
#
# for h in houses_kaupiklis:
#     print(h)

class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos
        self.__atlyginimas = None
        self.__asmens_kodas = None

    def get_atlyginimas(self):
        if self.__atlyginimas:
            print(self.__atlyginimas)
        else:
            print('Atlyginimas dar nepaskirtas.')

    def set_atlyginimas(self, suma):
        if suma > 0:
            self.__atlyginimas = suma
        else:
            print('Atlyginimas negali būti <0')

    def get_asmens_kodas(self):
        if self.__asmens_kodas:
            print(self.__asmens_kodas)
        else:
            print('Asmens kodas dar nepaskirtas.')

    def set_asmens_kodas(self, asmens_kodas):
        if asmens_kodas > 0:
            self.__asmens_kodas = asmens_kodas
        else:
            print('Asmens kodas negali būti <0')

    def get_darbuotojas_info(self):
        print(f'Vardas: {self.vardas}')
        print(f'Pavarde: {self.pavarde}')
        print(f'Pareigos: {self.pareigos}')
        self.get_atlyginimas()
        self.get_asmens_kodas()
