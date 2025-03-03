from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import date

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
    if existing_reader:
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

# Rodyti visų knygų sąrašą su jų būkle
def show_all_books():
    books = session.query(Book).all()
    for book in books:
        status = "Prieinama" if book.available else "Paskolinta"
        print(f"ID: {book.id}, Pavadinimas: {book.title}, Autorius: {book.author}, Būklė: {status}")

# Rodyti visų paskolintų knygų sąrašą
def show_borrowed_books():
    borrowed_books = session.query(BorrowedBook).all()
    for borrowed_book in borrowed_books:
        book = session.query(Book).filter(Book.id == borrowed_book.book_id).first()
        reader = session.query(Reader).filter(Reader.id == borrowed_book.reader_id).first()
        if book and reader:
            print(f"Knyga: {book.title}, Skaitytojas: {reader.name}, Paskolinta: {borrowed_book.borrowed_at}, Grąžinimo terminas: {borrowed_book.return_due_date}")
        else:
            print(f"Paskolinta knyga arba skaitytojas buvo pašalinti. Paskolintos knygos ID: {borrowed_book.id}")

# Rodyti skaitytojo paskolintų knygų istoriją
def show_reader_history(reader_id):
    borrowed_books = session.query(BorrowedBook).filter(BorrowedBook.reader_id == reader_id).all()
    if borrowed_books:
        for borrowed_book in borrowed_books:
            book = session.query(Book).filter(Book.id == borrowed_book.book_id).first()
            if book:
                print(f"Knyga: {book.title}, Paskolinta: {borrowed_book.borrowed_at}, Grąžinimo terminas: {borrowed_book.return_due_date}")
    else:
        print("Skaitytojas neturi paskolintų knygų.")

# Rodyti, kiek laiko knyga jau yra paskolinta
def show_borrowed_duration(book_id):
    borrowed_book = session.query(BorrowedBook).filter(BorrowedBook.book_id == book_id).first()
    if borrowed_book:
        borrowed_duration = (date.today() - borrowed_book.borrowed_at).days
        print(f"Knyga jau paskolinta {borrowed_duration} dienų.")
    else:
        print("Knyga nėra paskolinta.")

# Konsolės sąsaja
def main_menu():
    while True:
        print("\n--- Bibliotekos Sistema ---")
        print("1. Pridėti naują knygą")
        print("2. Pridėti naują skaitytoją")
        print("3. Paskolinti knygą skaitytojui")
        print("4. Atnaujinti knygos informaciją")
        print("5. Pašalinti skaitytoją")
        print("6. Pašalinti knygą")
        print("7. Rodyti visų knygų sąrašą")
        print("8. Rodyti visų paskolintų knygų sąrašą")
        print("9. Rodyti skaitytojo paskolintų knygų istoriją")
        print("10. Rodyti, kiek laiko knyga jau yra paskolinta")
        print("11. Išeiti")

        choice = input("Pasirinkite veiksmą: ")

        if choice == '1':
            title = input("Įveskite knygos pavadinimą: ")
            author = input("Įveskite autorių: ")
            year_published = int(input("Įveskite leidimo metus: "))
            add_book(title, author, year_published)

        elif choice == '2':
            name = input("Įveskite skaitytojo vardą: ")
            email = input("Įveskite el. paštą: ")
            add_reader(name, email)

        elif choice == '3':
            book_id = int(input("Įveskite knygos ID: "))
            reader_id = int(input("Įveskite skaitytojo ID: "))
            return_due_date = input("Įveskite grąžinimo datą (YYYY-MM-DD): ")
            return_due_date = date.fromisoformat(return_due_date)
            borrow_book(book_id, reader_id, return_due_date)

        elif choice == '4':
            book_id = int(input("Įveskite knygos ID: "))
            new_title = input("Įveskite naują pavadinimą (palikite tuščią, jei nenorite keisti): ")
            new_author = input("Įveskite naują autorių (palikite tuščią, jei nenorite keisti): ")
            new_year_published = input("Įveskite naujus leidimo metus (palikite tuščią, jei nenorite keisti): ")
            new_year_published = int(new_year_published) if new_year_published else None
            update_book(book_id, new_title, new_author, new_year_published)

        elif choice == '5':
            reader_id = int(input("Įveskite skaitytojo ID: "))
            delete_reader(reader_id)

        elif choice == '6':
            book_id = int(input("Įveskite knygos ID: "))
            delete_book(book_id)

        elif choice == '7':
            show_all_books()

        elif choice == '8':
            show_borrowed_books()

        elif choice == '9':
            reader_id = int(input("Įveskite skaitytojo ID: "))
            show_reader_history(reader_id)

        elif choice == '10':
            book_id = int(input("Įveskite knygos ID: "))
            show_borrowed_duration(book_id)

        elif choice == '11':
            print("Išeinama...")
            break

        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

# Paleidžiame programą
if __name__ == "__main__":
    main_menu()