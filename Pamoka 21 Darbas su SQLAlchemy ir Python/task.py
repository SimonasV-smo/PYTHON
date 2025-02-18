from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, distinct, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Mokytojas(Base):
    __tablename__ = 'mokytojai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    dalykas = Column(String)
    mokiniai = relationship('Mokinys', back_populates='mokytojas')

class Mokinys(Base):
    __tablename__ = 'mokiniai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(String)
    mokytojas_id = Column(Integer, ForeignKey('mokytojai.id'))
    mokytojas = relationship('Mokytojas', back_populates='mokiniai')

# Sukuriame duomenų bazę
engine = create_engine('sqlite:///mokykla.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_mokytojas(vardas, pavarde, dalykas):
    """Patikrina ar mokytojas egzistuoja, jei ne – prideda."""
    existing_mokytojas = session.query(Mokytojas).filter_by(vardas=vardas, pavarde=pavarde, dalykas=dalykas).first()
    if existing_mokytojas is None:
        new_mokytojas = Mokytojas(vardas=vardas, pavarde=pavarde, dalykas=dalykas)
        session.add(new_mokytojas)
        session.commit()
        return new_mokytojas
    return existing_mokytojas

def add_mokinys(vardas, pavarde, klase, mokytojas_vardas, mokytojas_pavarde, dalykas):
    """Prideda mokinį ir susieja su mokytoju."""
    mokytojas = add_mokytojas(mokytojas_vardas, mokytojas_pavarde, dalykas)
    existing_mokinys = session.query(Mokinys).filter_by(vardas=vardas, pavarde=pavarde, klase=klase).first()
    if existing_mokinys is None:
        new_mokinys = Mokinys(vardas=vardas, pavarde=pavarde, klase=klase, mokytojas=mokytojas)
        session.add(new_mokinys)
        session.commit()

# Pridedami mokytojai
mokytoju_duomenys = [
    ("Jonas", "Petraitis", "Matematika"),
    ("Asta", "Jankauskienė", "Lietuvių kalba"),
    ("Petras", "Kazlauskas", "Fizika"),
]
for vardas, pavarde, dalykas in mokytoju_duomenys:
    add_mokytojas(vardas, pavarde, dalykas)

# Pridedami mokiniai su mokytojais
mokiniai_duomenys = [
    ("Tomas", "Jonaitis", "10A", "Jonas", "Petraitis", "Matematika"),
    ("Ieva", "Kazlauskaitė", "6A", "Asta", "Jankauskienė", "Lietuvių kalba"),
    ("Mantas", "Petrauskas", "11B", "Petras", "Kazlauskas", "Fizika"),
]
for duomenys in mokiniai_duomenys:
    add_mokinys(*duomenys)

# Patikrinimas ar viskas įterpta
mokytojai = session.query(Mokytojas).all()
mokiniai = session.query(Mokinys).all()
print("Mokytojai:")
for mokytojas in mokytojai:
    print(f"{mokytojas.id}: {mokytojas.vardas} {mokytojas.pavarde} - {mokytojas.dalykas}")

print("\nMokiniai:")
for mokinys in mokiniai:
    print(f"{mokinys.id}: {mokinys.vardas} {mokinys.pavarde} ({mokinys.klase}) - {mokinys.mokytojas.vardas} {mokinys.mokytojas.pavarde}")

# Funkcija išvedanti mokinius pagal klasę (didėjančia tvarka)
def get_mokiniai_sorted_by_klase():
    mokiniai = session.query(Mokinys).order_by(Mokinys.klase).all()
    for mokinys in mokiniai:
        print(f"{mokinys.vardas} {mokinys.pavarde} - {mokinys.klase}")

# Funkcija suskaičiuojanti mokinių skaičių kiekvienoje klasėje
def count_mokiniai_per_klase():
    result = session.query(Mokinys.klase, func.count(Mokinys.id)).group_by(Mokinys.klase).all()
    for klase, count in result:
        print(f"Klasė {klase}: {count} mokiniai")

# Papildomas iššūkis: vidutinis mokinių skaičius klasėje
def average_mokiniai_per_klase():
    result = session.query(func.count(Mokinys.id) / func.count(distinct(Mokinys.klase))).scalar()
    print(f"Vidutinis mokinių skaičius klasėje: {result:.2f}")

# Iškviečiame funkcijas
get_mokiniai_sorted_by_klase()
count_mokiniai_per_klase()
average_mokiniai_per_klase()

