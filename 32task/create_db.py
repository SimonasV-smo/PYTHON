from app import create_app, db
from app.models import Workplace, Employee
import random


# Funkcija darboviečių užpildymui su didžiaisiais maisto prekių tinklais
def seed_workplaces():
    companies = [
        "Maxima", "Rimi", "Iki", "Norfa", "Lidl", "Aibė",
        "Fresh Market", "Prisma", "Taupa", "Kubas"
    ]
    cities = [
        "Vilnius", "Kaunas", "Klaipėda", "Šiauliai", "Panevėžys",
        "Alytus", "Marijampolė", "Utena", "Tauragė", "Telšiai"
    ]

    for i, company in enumerate(companies):
        # Kiekvieną tinklą susieti su keliais miestais (jei norisi daugiau nei 10 įrašų, pavadinimai gali kartotis)
        for city in cities:
            name = f"{company} {city}"  # Pvz., "Maxima Vilnius", "Rimi Kaunas"
            employee_count = random.randint(5, 10)  # Atsitiktinis darbuotojų skaičius

            workplace = Workplace(name=name, city=city, employee_count=employee_count)
            db.session.add(workplace)

    db.session.commit()
    print("Maisto prekių tinklai pridėti į duomenų bazę!")


# Funkcija darbuotojų užpildymui
def seed_employees():
    first_names = ["Jonas", "Ona", "Petras", "Ieva", "Tomas", "Aistė", "Dalia", "Paulius", "Rūta", "Lukas"]
    last_names = ["Kazlauskas", "Petrauskienė", "Jonaitis", "Ivanauskas", "Bieliūnas", "Zabiela", "Stonkus", "Juknaitė",
                  "Navickas", "Žemaitis"]
    positions = ["Manager", "Developer", "Designer", "Engineer", "Technician", "Analyst", "Consultant", "Coordinator",
                 "Specialist", "Administrator"]

    workplaces = Workplace.query.all()  # Visos darbovietės

    for workplace in workplaces:
        employee_count = random.randint(5, 10)  # Atsitiktinis darbuotojų skaičius
        for _ in range(employee_count):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            position = random.choice(positions)

            employee = Employee(
                first_name=first_name,
                last_name=last_name,
                position=position,
                workplace_id=workplace.id
            )

            db.session.add(employee)

        # Atnaujinkime darbuotojų skaičių darbovietėje
        workplace.employee_count += employee_count

    db.session.commit()
    print("Darbuotojai sėkmingai pridėti!")


# Pagrindinė programa
app = create_app()
with app.app_context():
    db.create_all()  # Sukuriame lenteles, jei jų dar nėra
    seed_workplaces()  # Užpildome darbovietes su tinklais
    seed_employees()  # Užpildome darbuotojus
