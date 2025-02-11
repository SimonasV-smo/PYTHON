#
# # 1. Funkcijos kaip Pirmos Klasės Objektai
#
# def prideti_zenkliuka(tekstas):
#     return f'{tekstas}*'
#
# def apversti_sakini(tekstas):
#     return tekstas[::-1]
#
# print(apversti_sakini('sis tekstas yra apverstas'))
# print(prideti_zenkliuka('siam tekstui reikia zenkliuko'))
#
# def apdoroti_teksta(tekstas, funkcija = None):
#     if funkcija:
#         tekstas = funkcija(tekstas)
#     return tekstas.lower()
#
# def keli_apdorojimai(tekstas, *funkcijos):
#     for funkcija in funkcijos:
#         tekstas = funkcija(tekstas)
#     return tekstas
#
# print(apdoroti_teksta('Sis Tekstas yra mažosiomis raidėmis'))
# print(apdoroti_teksta('sis tekstas su funkcija', prideti_zenkliuka))
# print(keli_apdorojimai('sis tekstas su keliomis funkcijomis', prideti_zenkliuka, apversti_sakini))

# 2. Dekoratoriai

def sekimo_dekoratorius(funkcija):
    def apvalkalas(*args, **kwargs):
        print(f'Vykdoma funkcija : {funkcija.__name__}')
        res = funkcija(*args, **kwargs)
        print('Funkcija baigta.')
        return res
    return apvalkalas

@sekimo_dekoratorius
def dauginti(a, b):
    return a * b

@sekimo_dekoratorius
def dalinti(a, b):
    if b == 0:
        return 'dalyba is nulio negalima'
    return a / b

print("Dauginimo testas:")
rezultatas1 = dauginti(5, 3)
print(f"Rezultatas: {rezultatas1}\n")

print("Dalybos testas:")
rezultatas2 = dalinti(10, 2)
print(f"Rezultatas: {rezultatas2}\n")

print("Dalybos iš nulio testas:")
rezultatas3 = dalinti(8, 0)
print(f"Rezultatas: {rezultatas3}")