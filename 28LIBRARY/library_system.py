
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

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

#SQLite pavyzdys
engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)

# Sukuriame sesiją
Session = sessionmaker(bind=engine)
session = Session()
