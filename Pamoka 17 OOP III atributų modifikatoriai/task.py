# 1 task

class Studentas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self._pazymiai = []

    def prideti_pazymi(self, pazymys):
        if 1 <= pazymys <= 10:
            self._pazymiai.append(pazymys)
        else:
            raise ValueError ('ivestas blogas pazymys. 1<=pazymys<=10')

    def rodyti_vidurki(self):
        if self._pazymiai:
            vidurkis = sum(self._pazymiai) / len(self._pazymiai)
            return vidurkis
        else:
            return 'pazymiai neprideti. negalima apskaiciuoti visdurkio'

class StudentasLyderis(Studentas):
        def __init__(self, vardas, pavarde, bonus_taskai):
            super().__init__(vardas, pavarde)
            self.bonus_taskai = bonus_taskai

        def rodyti_vidurki_su_bonusu(self):
            if self._pazymiai:
                vidurkis = super().rodyti_vidurki() + self.bonus_taskai
                return vidurkis
            else:
                return 'pazymiai neprideti, negalima apskaiciuoti vidurkio'

studentas = Studentas('Jonas', 'Jonaitis')
studentas.prideti_pazymi(8)
studentas.prideti_pazymi(9)
studentas.prideti_pazymi(6)
studentas.prideti_pazymi(4)
print(studentas.rodyti_vidurki())

studentas_lyderis = StudentasLyderis('Ona', 'Jarute', 1)
studentas_lyderis.prideti_pazymi(9)
studentas_lyderis.prideti_pazymi(8)
studentas_lyderis.prideti_pazymi(7)
studentas_lyderis.prideti_pazymi(6)
print(studentas_lyderis.rodyti_vidurki_su_bonusu())



# 2task

class BankoSaskaita:
    def __init__(self, savininkas):
        self.savininkas = savininkas
        self.__balansas = 0

    def gauti_balansa(self):
        return self.__balansas

    def prideti_pinigus(self, suma):
        if suma > 0:
            self.__balansas += suma
        else:
            raise ValueError('Suma turi būti didesnė už 0')

    def nuskaiciuoti_pinigus(self, suma):
        if suma > 0:
            if self.__balansas >= suma:
                self.__balansas -= suma
            else:
                raise ValueError('Nepakankamos lėšos sąskaitoje')
        else:
            raise ValueError('Suma turi būti didesnė už 0')


saskaita = BankoSaskaita('Jonas Jurgutis')
saskaita.prideti_pinigus(250)
print(saskaita.gauti_balansa())

saskaita.nuskaiciuoti_pinigus(50)
print(saskaita.gauti_balansa())

try:
    saskaita.nuskaiciuoti_pinigus(100)
except ValueError as e:
    print(e)
