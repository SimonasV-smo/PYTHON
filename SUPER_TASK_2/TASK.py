import sqlite3

def sukurti_duomenu_baze():
    conn = sqlite3.connect('mokykla.db')
    cursor = conn.cursor()

    # Sukuriame mokinių lentelę
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mokiniai (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vardas TEXT NOT NULL,
        pavarde TEXT NOT NULL,
        klase TEXT,
        vidurkis REAL
    )
    ''')

    # Sukuriame mokytojų lentelę
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mokytojai (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vardas TEXT NOT NULL,
        pavarde TEXT NOT NULL,
        dalykas TEXT
    )
    ''')

    conn.commit()
    conn.close()