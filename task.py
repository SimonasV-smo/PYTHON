
from sqlalchemy import Column, create_engine, Integer, String, Float
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:///mokykla.db')
Base = declarative_base()


class Mokinys(Base):
    __tablename__ = 'mokinys'

    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)


class Mokytojas(Base):
    __tablename__ = 'mokytojas'

    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    dalykas = Column(String)


Base.metadata.create_all(engine)

from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Sukuriame duomenų bazę
engine = create_engine('sqlite:///mokykla.db')
Base = declarative_base()

# Modeliai
class Mokinys(Base):
    __tablename__ = 'mokinys'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)

class Mokytojas(Base):
    __tablename__ = 'mokytojas'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    dalykas = Column(String)

# Sukuriame lenteles
Base.metadata.create_all(engine)

# Sukuriame sesiją
Session = sessionmaker(bind=engine)
session = Session()

# Funkcija, kuri patikrina, ar mokinys jau yra duomenų bazėje
def ar_mokinys_yra(vardas, pavarde):
    return session.query(Mokinys).filter_by(vardas=vardas, pavarde=pavarde).first() is not None

# def ar_mokinys_yra(vardas, pavarde):
#     mokiniai = session.query(Mokinys).all()
#     for row in mokiniai:
#         if row.vardas == vardas and row.pavarde == pavarde:
#             return True

# Pridedame mokinius, jei jų dar nėra
mokiniai = [
    ("Jonas", "Jonaitis", 5),
    ("Petras", "Petraitis", 6),
    ("Asta", "Astaitė", 7)
]

for vardas, pavarde, klase in mokiniai:
    if not ar_mokinys_yra(vardas, pavarde):
        session.add(Mokinys(vardas=vardas, pavarde=pavarde, klase=klase))

# Pridedame mokytojus
mokytojai = [
    Mokytojas(vardas="Rasa", pavarde="Rasaitė", dalykas="Matematika"),
    Mokytojas(vardas="Tomas", pavarde="Tomaitis", dalykas="Fizika")
]

session.add_all(mokytojai)

# Išsaugome pakeitimus
session.commit()

# Funkcija mokinių sąrašo išvedimui
def spausdinti_mokinius():
    mokiniai = session.query(Mokinys).all()
    for mokinys in mokiniai:
        print(f"{mokinys.vardas} {mokinys.pavarde}, klasė: {mokinys.klase}")

# Funkcija mokytojų sąrašo išvedimui
def spausdinti_mokytojus():
    mokytojai = session.query(Mokytojas).all()
    for mokytojas in mokytojai:
        print(f"{mokytojas.vardas} {mokytojas.pavarde}, dėsto: {mokytojas.dalykas}")

# Testuojame funkcijas
print("Mokiniai:")
spausdinti_mokinius()

print("\nMokytojai:")
spausdinti_mokytojus()

from models import Mokinys, Mokytojas, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import MultipleResultsFound, NoResultFound

Session = sessionmaker(bind=engine)
session = Session()

def delete_student_by_id(student_id):
    student = session.get(Mokinys, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f'Mokinys su ID {student_id} pašalintas.')
    else:
        print(f'Mokinys su ID {student_id} nerastas.')

def delete_teacher_by_id(teacher_id):
    teacher = session.get(Mokytojas, teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f'Mokytojas su ID {teacher_id} pašalintas.')
    else:
        print(f'Mokytojas su ID {teacher_id} nerastas.')

def delete_graduated_students():
    graduated_students = session.query(Mokinys).filter_by(klase=12).all()
    for student in graduated_students:
        session.delete(student)
    session.commit()
    print(f'Visi 12 klasės mokiniai pašalinti.')

def find_student_by_name(name):
    try:
        student = session.query(Mokinys).filter_by(vardas=name).one()
        print(student)
    except NoResultFound:
        print(f'Mokinys su vardu {name} nerastas.')
    except MultipleResultsFound:
        print(f'Rasta daugiau nei viena įrašų su vardu {name}.')

def find_students_by_lastname_initial(letter):
    students = session.query(Mokinys).filter(Mokinys.pavarde.ilike(f'{letter}%')).all()
    for student in students:
        print(student)

def find_teachers_by_name_endswith(letter):
    teachers = session.query(Mokytojas).filter(Mokytojas.vardas.ilike(f'%{letter}')).all()
    for teacher in teachers:
        print(teacher)

from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import MultipleResultsFound, NoResultFound

Base = declarative_base()

class Mokinys(Base):
    __tablename__ = 'mokiniai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)

class Mokytojas(Base):
    __tablename__ = 'mokytojai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)

engine = create_engine('sqlite:///school.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def delete_student_by_id(student_id):
    student = session.get(Mokinys, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f'Mokinys su ID {student_id} pašalintas.')
    else:
        print(f'Mokinys su ID {student_id} nerastas.')

def delete_teacher_by_id(teacher_id):
    teacher = session.get(Mokytojas, teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f'Mokytojas su ID {teacher_id} pašalintas.')
    else:
        print(f'Mokytojas su ID {teacher_id} nerastas.')

def delete_graduated_students():
    graduated_students = session.query(Mokinys).filter_by(klase=12).all()
    for student in graduated_students:
        session.delete(student)
    session.commit()
    print(f'Visi 12 klasės mokiniai pašalinti.')

def find_student_by_name(name):
    try:
        student = session.query(Mokinys).filter_by(vardas=name).one()
        print(student)
    except NoResultFound:
        print(f'Mokinys su vardu {name} nerastas.')
    except MultipleResultsFound:
        print(f'Rasta daugiau nei viena įrašų su vardu {name}.')

def find_students_by_lastname_initial(letter):
    students = session.query(Mokinys).filter(Mokinys.pavarde.ilike(f'{letter}%')).all()
    for student in students:
        print(student)

def find_teachers_by_name_endswith(letter):
    teachers = session.query(Mokytojas).filter(Mokytojas.vardas.ilike(f'%{letter}')).all()
    for teacher in teachers:
        print(teacher)

def list_students_by_class():
    students = session.query(Mokinys).order_by(Mokinys.klase).all()
    for student in students:
        print(student)

def count_students_per_class():
    class_counts = session.query(Mokinys.klase, func.count(Mokinys.id)).group_by(Mokinys.klase).all()
    for klase, count in class_counts:
        print(f'Klasė {klase}: {count} mokiniai')

def average_students_per_class():
    total_students = session.query(func.count(Mokinys.id)).scalar()
    total_classes = session.query(func.count(func.distinct(Mokinys.klase))).scalar()
    avg_students = total_students / total_classes if total_classes else 0
    print(f'Vidutinis mokinių skaičius klasėje: {avg_students:.2f}')


delete_student_by_id(3)
delete_teacher_by_id(2)
delete_graduated_students()
find_student_by_name("Jonas")
find_students_by_lastname_initial("P")
find_teachers_by_name_endswith("s")
list_students_by_class()
count_students_per_class()
average_students_per_class()