from datetime import datetime, timedelta

class Book:
    def __init__(self, book_title, book_author, book_year, available=True):
        try:
            book_year = int(book_year)
            if book_year <= 0:
                raise ValueError
        except (ValueError, TypeError):
            print("Netinkama metų reikšmė")
            book_year = 2000

        self.book_title = book_title
        self.book_author = book_author
        self.book_year = book_year
        self.available = available

    def __str__(self):
        return f'Knyga {self.book_title} parašyta {self.book_author} ({self.book_year})'

    def is_classic(self):
        current_year = datetime.now().year
        return current_year - self.book_year >= 50

    @staticmethod
    def due_date(borrow_date, days=14):
        return borrow_date + timedelta(days=days)


class Library:
    def __init__(self):
        self.books_list = []
        self.books_list.append(Book("Haris Poteris", "J.K. Rowling", 1997))
        self.books_list.append(Book("1984", "George Orwell", 1949))
        self.books_list.append(Book("Didysis Getsbis", "F. Scott Fitzgerald", 1925))
        self.books_list.append(Book("Žiedų Valdovas", "J.R.R. Tolkien", 1954))

    def add_book(self, new_book):
        if isinstance(new_book, Book):
            self.books_list.append(new_book)
        else:
            print("Nepavyko pridėti knygos")

    def display_books(self):
        if not self.books_list:
            print('Biblioteka tuščia, sugrįžkite vėliau.')
        else:
            for b in self.books_list:
                print(b)

    def borrow_book(self, book_title, days=14):
        for b in self.books_list:
            if b.book_title == book_title and b.available:
                b.available = False
                b.borrow_date = datetime.now()
                b.due_date = Book.due_date(b.borrow_date, days)
                return f"Knyga pasiskolinta iki {b.due_date.strftime('%Y-%m-%d')}"
        return "Knyga nepasiekiama"

    def return_book(self, book_title):
        for b in self.books_list:
            if b.book_title == book_title and not b.available:
                b.available = True
                return "Knyga sėkmingai grąžinta"
        return "Knyga negali būti grąžinta"

    def filter_books(self, *args, **kwargs):
        results = self.books_list

        for arg in args:
            results = [b for b in results if arg in b.book_title or arg in b.book_author]

        if 'author' in kwargs:
            results = [b for b in results if b.book_author == kwargs['author']]

        if 'year' in kwargs:
            results = [b for b in results if b.book_year == kwargs['year']]

        if 'title' in kwargs:
            results = [b for b in results if b.book_title == kwargs['title']]

        return results


library = Library()

while True:
    print("\nBibliotekos Sistema")
    print("1. Pridėti naują knygą")
    print("2. Peržiūrėti visas knygas")
    print("3. Pasiskolinti knygą")
    print("4. Grąžinti knygą")
    print("5. Filtruoti knygas")
    print("6. Išeiti")

    pasirinkimas = input("Pasirinkite veiksmą (1-6): ")

    try:
        if pasirinkimas == "1":
            book_title = input("Įveskite knygos pavadinimą: ")
            book_author = input("Įveskite knygos autorių: ")
            book_year = input("Įveskite knygos išleidimo metus: ")
            new_book = Book(book_title, book_author, book_year)
            library.add_book(new_book)
            print("Knyga sėkmingai pridėta!")

        elif pasirinkimas == "2":
            library.display_books()

        elif pasirinkimas == "3":
            book_title = input("Įveskite knygos pavadinimą, kurią norite pasiskolinti: ")
            message = library.borrow_book(book_title)
            print(message)

        elif pasirinkimas == "4":
            book_title = input("Įveskite knygos pavadinimą, kurią norite grąžinti: ")
            message = library.return_book(book_title)
            print(message)

        elif pasirinkimas == "5":
            filter_type = input("Įveskite filtravimo tipą (autorius, metai, pavadinimas): ")
            if filter_type == "autorius":
                author = input("Įveskite autoriaus vardą: ")
                filtered_books = library.filter_books(author=author)
            elif filter_type == "metai":
                year = input("Įveskite metus: ")
                filtered_books = library.filter_books(year=year)
            elif filter_type == "pavadinimas":
                book_title = input("Įveskite knygos pavadinimą: ")
                filtered_books = library.filter_books(title=book_title)
            else:
                filtered_books = []

            if filtered_books:
                print("Rastos knygos:")
                for b in filtered_books:
                    print(b)
            else:
                print("Nerasta jokių knygų pagal jūsų kriterijus.")

        elif pasirinkimas == "6":
            print("Išeinama iš programos.")
            break

        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

    except ValueError as e:
        print(f"Klaida: {e}")
    except Exception as e:
        print(f"Nenumatyta klaida: {e}")