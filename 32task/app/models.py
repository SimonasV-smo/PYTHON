from app import db

# Darboviečių modelis
class Workplace(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Pagrindinis raktas
    name = db.Column(db.String(100), nullable=False)  # Darbovietės pavadinimas
    city = db.Column(db.String(100), nullable=False)  # Miestas
    employee_count = db.Column(db.Integer, default=0)  # Darbuotojų skaičius (pagal nutylėjimą 0)

    # Lentelės ryšys su darbuotojais (viena darbovietė gali turėti daug darbuotojų)
    employees = db.relationship('Employee', backref='workplace', lazy=True)

    def __repr__(self):
        return f'<Workplace {self.name}>'

# Darbuotojų modelis
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Pagrindinis raktas
    first_name = db.Column(db.String(100), nullable=False)  # Darbuotojo vardas
    last_name = db.Column(db.String(100), nullable=False)  # Pavardė
    position = db.Column(db.String(100), nullable=False)  # Pareigos
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)  # Užsienio raktas į darboviečių lentelę

    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'
