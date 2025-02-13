import sqlite3

# 1. Prisijungimas prie duomenų bazės ir lentelės sukūrimas
def sukurti_lentele():
    conn = None  # Inicializuojame conn kaip None
    try:
        # Prisijungiam prie duomenų bazės (jei jos nėra, ji bus sukurta)
        conn = sqlite3.connect('mokykla.db')
        cursor = conn.cursor()

        # Sukuriame lentelę, jei ji dar neegzistuoja
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS mokykla (
            pavadinimas TEXT,
            adresas TEXT,
            mokiniu_skaicius INTEGER
        )
        ''')

        # Patvirtiname pakeitimus ir uždarome ryšį
        conn.commit()
        print("Lentelė 'mokykla' sėkmingai sukurta arba jau egzistuoja.")
    except sqlite3.Error as e:
        print(f"Klaida kuriant lentelę: {e}")
    finally:
        if conn:
            conn.close()


# 2. Funkcija duomenų įterpimui
def prideti_mokykla(pavadinimas, adresas, mokiniu_skaicius):
    conn = None  # Inicializuojame conn kaip None
    try:
        # Prisijungiam prie duomenų bazės
        conn = sqlite3.connect('mokykla.db')
        cursor = conn.cursor()

        # Įterpiame duomenis į lentelę
        cursor.execute('''
        INSERT INTO mokykla (pavadinimas, adresas, mokiniu_skaicius)
        VALUES (?, ?, ?)
        ''', (pavadinimas, adresas, mokiniu_skaicius))

        # Patvirtiname pakeitimus
        conn.commit()
        print(f"Duomenys sėkmingai įterpti: {pavadinimas}")
    except sqlite3.Error as e:
        print(f"Klaida įterpiant duomenis: {e}")
    finally:
        if conn:
            conn.close()


# 3. Funkcija duomenų skaitymui su filtravimu
def gauti_mokyklas(min_mokiniu_skaicius=None):
    conn = None  # Inicializuojame conn kaip None
    try:
        # Prisijungiam prie duomenų bazės
        conn = sqlite3.connect('mokykla.db')
        cursor = conn.cursor()

        # Formuojame SQL užklausą pagal filtro sąlygą
        if min_mokiniu_skaicius:
            cursor.execute('''
            SELECT * FROM mokykla WHERE mokiniu_skaicius > ?
            ''', (min_mokiniu_skaicius,))
        else:
            cursor.execute('''
            SELECT * FROM mokykla
            ''')

        # Gauname visus rezultatus
        mokyklos = cursor.fetchall()

        # Jei rezultatų nėra, pranešame apie tai
        if not mokyklos:
            print("Nerasta jokių mokyklų.")
            return

        # Atspausdiname rezultatus gražiai suformatuotais sakiniais
        for mokykla in mokyklos:
            print(f"Mokykla: {mokykla[0]}, Adresas: {mokykla[1]}, Mokinių skaičius: {mokykla[2]}")
    except sqlite3.Error as e:
        print(f"Klaida skaitant duomenis: {e}")
    finally:
        if conn:
            conn.close()


# Pagrindinė programos dalis
if __name__ == "__main__":
    # Sukuriame lentelę (jei reikia)
    sukurti_lentele()

    # Įterpiame pradinius duomenis
    prideti_mokykla("Vilniaus progimnazija", "Vilniaus g. 10", 500)
    prideti_mokykla("Kauno gimnazija", "Kauno g. 5", 800)

    # Atspausdiname visus duomenis
    print("\nVisos mokyklos:")
    gauti_mokyklas()

    # Atspausdiname mokyklas su daugiau nei 600 mokinių
    print("\nMokyklos su daugiau nei 600 mokinių:")
    gauti_mokyklas(min_mokiniu_skaicius=600)

# 4. Funkcija mokinių skaičiaus atnaujinimui
def atnaujinti_mokiniu_skaiciu(pavadinimas, naujas_mokiniu_skaicius):
    conn = None  # Inicializuojame conn kaip None
    try:
        # Prisijungiam prie duomenų bazės
        conn = sqlite3.connect('mokykla.db')
        cursor = conn.cursor()

        # Atnaujiname mokinių skaičių nurodytai mokyklai
        cursor.execute('''
        UPDATE mokykla
        SET mokiniu_skaicius = ?
        WHERE pavadinimas = ?
        ''', (naujas_mokiniu_skaicius, pavadinimas))

        # Patvirtiname pakeitimus
        conn.commit()
        print(f"Mokyklos '{pavadinimas}' mokinių skaičius sėkmingai atnaujintas į {naujas_mokiniu_skaicius}.")
    except sqlite3.Error as e:
        print(f"Klaida atnaujinant mokinių skaičių: {e}")
    finally:
        if conn:
            conn.close()


# Pagrindinė programos dalis
if __name__ == "__main__":
    # Sukuriame lentelę (jei reikia)
    sukurti_lentele()

    # Įterpiame pradinius duomenis
    prideti_mokykla("Vilniaus progimnazija", "Vilniaus g. 10", 500)
    prideti_mokykla("Kauno gimnazija", "Kauno g. 5", 800)

    # Atspausdiname visus duomenis
    print("\nVisos mokyklos:")
    gauti_mokyklas()

    # Atspausdiname mokyklas su daugiau nei 600 mokinių
    print("\nMokyklos su daugiau nei 600 mokinių:")
    gauti_mokyklas(min_mokiniu_skaicius=600)

    # Atnaujiname mokinių skaičių
    atnaujinti_mokiniu_skaiciu("Vilniaus progimnazija", 600)

    # Patikriname, ar atnaujinimas buvo sėkmingas
    print("\nVisos mokyklos po atnaujinimo:")
    gauti_mokyklas()