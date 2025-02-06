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

class Mygtukas:
    def deaktyvuoti(self):
        print('mygtukas deaktyvuotas')

class RaudonasMygtukas(Mygtukas):
    def deaktyvuoti(self):
        super().deaktyvuoti()
        print('aciu kad dirbote')
        print('spava pasikeitei i rausva')

red_btn = RaudonasMygtukas()
red_btn.deaktyvuoti()