from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Workplace, Employee

# Sukuriame pagrindinį Blueprint
main = Blueprint('main', __name__)

# --- Darboviečių maršrutai ---

@main.route('/')
def home():
    return render_template('base.html')

# 1. Darboviečių sąrašo peržiūra
@main.route('/workplaces')
def list_workplaces():
    workplaces = Workplace.query.all()

    # Dinamiškai apskaičiuojame kiekvienos darbovietės darbuotojų skaičių
    for workplace in workplaces:
        workplace.actual_employee_count = Employee.query.filter_by(workplace_id=workplace.id).count()

    return render_template('workplaces.html', workplaces=workplaces)


# 2. Naujos darbovietės pridėjimas
@main.route('/workplaces/add', methods=['GET', 'POST'])
def add_workplace():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']

        new_workplace = Workplace(name=name, city=city)
        db.session.add(new_workplace)
        db.session.commit()

        return redirect(url_for('main.list_workplaces'))
    return render_template('add_workplace.html')

# 3. Darbovietės redagavimas
@main.route('/workplaces/edit/<int:workplace_id>', methods=['GET', 'POST'])
def edit_workplace(workplace_id):
    workplace = Workplace.query.get_or_404(workplace_id)
    if request.method == 'POST':
        workplace.name = request.form['name']
        workplace.city = request.form['city']

        db.session.commit()
        return redirect(url_for('main.list_workplaces'))

    return render_template('edit_workplace.html', workplace=workplace)

# 4. Darbovietės šalinimas
@main.route('/workplaces/delete/<int:workplace_id>', methods=['POST'])
def delete_workplace(workplace_id):
    workplace = Workplace.query.get_or_404(workplace_id)
    if Employee.query.filter_by(workplace_id=workplace_id).count() > 0:
        return "Workplace cannot be deleted as it has employees.", 400  # Klaida, jei yra darbuotojų

    db.session.delete(workplace)
    db.session.commit()
    return redirect(url_for('main.list_workplaces'))

# --- Darbuotojų maršrutai ---

# 1. Darbuotojų sąrašo peržiūra
@main.route('/employees')
def list_employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)

# 2. Naujo darbuotojo pridėjimas
@main.route('/employees/add', methods=['GET', 'POST'])
def add_employee():
    workplaces = Workplace.query.all()
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        position = request.form['position']
        workplace_id = int(request.form['workplace_id'])

        new_employee = Employee(first_name=first_name, last_name=last_name, position=position, workplace_id=workplace_id)
        db.session.add(new_employee)
        db.session.commit()

        return redirect(url_for('main.list_employees'))
    return render_template('add_employee.html', workplaces=workplaces)

# 3. Darbuotojo redagavimas
@main.route('/employees/edit/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    workplaces = Workplace.query.all()
    if request.method == 'POST':
        employee.first_name = request.form['first_name']
        employee.last_name = request.form['last_name']
        employee.position = request.form['position']
        employee.workplace_id = int(request.form['workplace_id'])

        db.session.commit()
        return redirect(url_for('main.list_employees'))
    return render_template('edit_employee.html', employee=employee, workplaces=workplaces)

# 4. Darbuotojo pašalinimas
@main.route('/employees/delete/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('main.list_employees'))

@main.route('/workplaces/search', methods=['GET'])
def search_workplaces():
    query_name = request.args.get('name')  # Paieška pagal pavadinimą
    query_city = request.args.get('city')  # Paieška pagal miestą

    # Filtruojame darboviečių sąrašą pagal pavadinimą ir/ar miestą
    workplaces = Workplace.query
    if query_name:
        workplaces = workplaces.filter(Workplace.name.ilike(f"%{query_name}%"))
    if query_city:
        workplaces = workplaces.filter(Workplace.city.ilike(f"%{query_city}%"))

    workplaces = workplaces.all()
    return render_template('workplaces.html', workplaces=workplaces)

@main.route('/workplaces/<int:workplace_id>')
def workplace_details(workplace_id):
    workplace = Workplace.query.get_or_404(workplace_id)
    employees = Employee.query.filter_by(workplace_id=workplace_id).all()

    actual_employee_count = len(employees)

    return render_template('workplace_details.html',
                           workplace=workplace,
                           employees=employees,
                           employee_count=actual_employee_count)
