# Importuojame reikiamus modulius ir sukonfigūruojame duomenų bazę
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import date  # Pridedame šią eilutę

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    author = Column(String, nullable=False)
    year_published = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)

class Reader(Base):
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    reader_id = Column(Integer, ForeignKey('readers.id'), nullable=False)
    borrowed_at = Column(Date, nullable=False)
    return_due_date = Column(Date, nullable=False)

    book = relationship('Book')
    reader = relationship('Reader')

# SQLite pavyzdys
engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)

# Sukuriame sesiją
Session = sessionmaker(bind=engine)
session = Session()

# Pridėti naują knygą su patikrinimu
def add_book(title, author, year_published):
    existing_book = session.query(Book).filter(Book.title == title).first()
    if existing_book:
        print(f"Knyga su pavadinimu '{title}' jau egzistuoja.")
    else:
        new_book = Book(title=title, author=author, year_published=year_published)
        session.add(new_book)
        session.commit()
        print(f"Pridėta knyga: {title}")

# Pridėti naują skaitytoją su patikrinimu
def add_reader(name, email):
    existing_reader = session.query(Reader).filter(Reader.email == email).first()
    if (existing_reader):
        print(f"Skaitytojas su el. paštu '{email}' jau egzistuoja.")
    else:
        new_reader = Reader(name=name, email=email)
        session.add(new_reader)
        session.commit()
        print(f"Pridėtas skaitytojas: {name}")

# Paskolinti knygą skaitytojui
def borrow_book(book_id, reader_id, return_due_date):
    book = session.query(Book).filter(Book.id == book_id).first()
    reader = session.query(Reader).filter(Reader.id == reader_id).first()
    if book and book.available:
        book.available = False
        borrowed_book = BorrowedBook(book_id=book_id, reader_id=reader_id, borrowed_at=date.today(), return_due_date=return_due_date)
        session.add(borrowed_book)
        session.commit()
        print(f"Knyga '{book.title}' paskolinta skaitytojui '{reader.name}'")
    else:
        print("Knyga jau paskolinta arba neegzistuoja.")

# Atnaujinti knygos informaciją
def update_book(book_id, new_title=None, new_author=None, new_year_published=None):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        if new_title:
            book.title = new_title
        if new_author:
            book.author = new_author
        if new_year_published:
            book.year_published = new_year_published
        session.commit()
        print(f"Knygos '{book.title}' informacija atnaujinta.")
    else:
        print("Knyga neegzistuoja.")

# Pašalinti skaitytoją
def delete_reader(reader_id):
    reader = session.query(Reader).filter(Reader.id == reader_id).first()
    if reader:
        print(f"Skaitytojas '{reader.name}' pašalintas.")
        session.delete(reader)
        session.commit()
    else:
        print("Skaitytojas neegzistuoja.")

# Pašalinti knygą
def delete_book(book_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        print(f"Knyga '{book.title}' pašalinta.")
        session.delete(book)
        session.commit()
    else:
        print("Knyga neegzistuoja.")

# Funkcija parodyti visų knygų sąrašą su jų būkle
def show_all_books():
    books = session.query(Book).all()
    for book in books:
        status = "Prieinama" if book.available else "Paskolinta"
        print(f"ID: {book.id}, Pavadinimas: {book.title}, Autorius: {book.author}, Būklė: {status}")

# Funkcija parodyti visų paskolintų knygų sąrašą
def show_borrowed_books():
    borrowed_books = session.query(BorrowedBook).all()
    for borrowed_book in borrowed_books:
        book = session.query(Book).filter(Book.id == borrowed_book.book_id).first()
        reader = session.query(Reader).filter(Reader.id == borrowed_book.reader_id).first()
        if book and reader:  # Patikriname, ar knyga ir skaitytojas nėra NoneType
            print(f"Knyga: {book.title}, Skaitytojas: {reader.name}, Paskolinta: {borrowed_book.borrowed_at}, Grąžinimo terminas: {borrowed_book.return_due_date}")
        else:
            print(f"Paskolinta knyga arba skaitytojas buvo pašalinti. Paskolintos knygos ID: {borrowed_book.id}")

# Testavimas
add_book("Altorių šešėly", "Vincas Mykolaitis-Putinas", 1933)
add_reader("Simonas", "simonas@example.com")
borrow_book(1, 1, date(2023, 12, 31))
update_book(1, new_title="Naujas knygos pavadinimas")
delete_reader(1)
delete_book(1)
show_all_books()
show_borrowed_books()
