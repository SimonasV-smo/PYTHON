
# 1. Funkcijos kaip Pirmos Klasės Objektai

def prideti_zenkliuka(tekstas):
    return f'{tekstas}*'

def apversti_sakini(tekstas):
    return tekstas[::-1]

print(apversti_sakini('sis tekstas yra apverstas'))
print(prideti_zenkliuka('siam tekstui reikia zenkliuko'))

def apdoroti_teksta(tekstas, funkcija = None):
    if funkcija:
        tekstas = funkcija(tekstas)
    return tekstas.lower()

def keli_apdorojimai(tekstas, *funkcijos):
    for funkcija in funkcijos:
        tekstas = funkcija(tekstas)
    return tekstas

print(apdoroti_teksta('Sis Tekstas yra mažosiomis raidėmis'))
print(apdoroti_teksta('sis tekstas su funkcija', prideti_zenkliuka))
print(keli_apdorojimai('sis tekstas su keliomis funkcijomis', prideti_zenkliuka, apversti_sakini))