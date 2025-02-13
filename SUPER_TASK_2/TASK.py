import sqlite3

# 1. Sistemos Funkcionalumas

def sukurti_duomenu_baze():
    with sqlite3.connect('mokykla.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS mokiniai (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vardas TEXT NOT NULL,
            pavarde TEXT NOT NULL,
            klase TEXT,
            vidurkis REAL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS mokytojai (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vardas TEXT NOT NULL,
            pavarde TEXT NOT NULL,
            dalykas TEXT
        )
        ''')

# 2. Struktūra

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

class Mokinys(Asmuo):
    def __init__(self, vardas, pavarde, klase=None, vidurkis=None):
        super().__init__(vardas, pavarde)
        self.klase = klase
        self.vidurkis = vidurkis

    def __str__(self):
        return f"Mokinys: {self.vardas} {self.pavarde}, Klasė: {self.klase}, Vidurkis: {self.vidurkis}"

class Mokytojas(Asmuo):
    def __init__(self, vardas, pavarde, dalykas=None):
        super().__init__(vardas, pavarde)
        self.dalykas = dalykas

    def __str__(self):
        return f"Mokytojas: {self.vardas} {self.pavarde}, Dalykas: {self.dalykas}"

def log_operation(func):
    def wrapper(*args, **kwargs):
        print(f"Vykdoma operacija: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 3. Realizacija

@log_operation
def prideti_mokini(vardas, pavarde, klase=None, vidurkis=None):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis)
            VALUES (?, ?, ?, ?)
            ''', (vardas, pavarde, klase, vidurkis))
    except sqlite3.Error as e:
        print(f"Klaida įterpiant mokinį: {e}")

@log_operation
def prideti_mokytoja(vardas, pavarde, dalykas=None):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO mokytojai (vardas, pavarde, dalykas)
            VALUES (?, ?, ?)
            ''', (vardas, pavarde, dalykas))
    except sqlite3.Error as e:
        print(f"Klaida įterpiant mokytoją: {e}")

def gauti_mokinius():
    try:
        with sqlite3.connect('mokykla.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM mokiniai')
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Klaida gaunant mokinius: {e}")
        return []

def gauti_mokytojus():
    try:
        with sqlite3.connect('mokykla.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM mokytojai')
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Klaida gaunant mokytojus: {e}")
        return []

@log_operation
def atnaujinti_mokinio_klase(mokinio_id, nauja_klase):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
            UPDATE mokiniai
            SET klase = ?
            WHERE id = ?
            ''', (nauja_klase, mokinio_id))
    except sqlite3.Error as e:
        print(f"Klaida atnaujinant mokinio klasę: {e}")

@log_operation
def pasalinti_mokini(mokinio_id):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM mokiniai WHERE id = ?', (mokinio_id,))
    except sqlite3.Error as e:
        print(f"Klaida pašalinant mokinį: {e}")

def ieskoti_mokinio_pagal_varda(vardas):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM mokiniai WHERE vardas = ?', (vardas,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Klaida ieškant mokinio: {e}")
        return []

# 4. Užduoties Etapai

class MokinysIterator:
    def __init__(self, mokiniai):
        self.mokiniai = mokiniai

    def __iter__(self):
        return iter(self.mokiniai)

if __name__ == "__main__":
    sukurti_duomenu_baze()

    prideti_mokini("Jonas", "Jonaitis", "10A", 9.5)
    prideti_mokini("Ona", "Onaitė", "9B", 8.7)
    prideti_mokytoja("Petras", "Petraitis", "Matematika")

    mokiniai = gauti_mokinius()
    for mokinys in mokiniai:
        print(mokinys)

    print("\nIeškomas mokinys 'Jonas':")
    ieskoti_mokinio_pagal_varda("Jonas")

    atnaujinti_mokinio_klase(1, "11A")

    print("\nMokinių sąrašas su iteratoriumi:")
    mokinys_iterator = MokinysIterator(mokiniai)
    for mokinys in mokinys_iterator:
        print(mokinys)