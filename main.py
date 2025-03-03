#
# import sqlite3
#
# conn = sqlite3.connect('sql_injection.db')
# c = conn.cursor()
# #
# inp_username = input('Username: ')
# inp_password = input('Password: ')
#
# with conn:
#     c.execute('SELECT * FROM user WHERE user.username=? AND user.password=?;', (inp_username, inp_password))
#     res = c.fetchall()
#     if res:
#         print('Jūsų profilio duomenyts yra: ')
#         print(res)
#     else:
#         print(f"Vartotojas {inp_username} neegzistuoja arba neteisingas slaptažodis")

# - STEP 3: Get all users with sql injection
# inp_username = input('Username: '), "' OR True;--"
# inp_password = input('Password: '), ""
#
# query = f"SELECT * FROM user WHERE user.username='{inp_username}' AND user.password='{inp_password}';"
#
# with conn:
#     print("=>>>>> ", query)
#     c.execute(query)
#     res = c.fetchall()
#     print("Jūsų profilio duomenys yra:", res)

# STEP 2: Check if users created
# with conn:
#     c.execute('SELECT * FROM user;')
# print(c.fetchall())

# - STEP1: DB and table creation
# query = '''CREATE TABLE IF NOT EXISTS user (
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     username TEXT NOT NULL,
#     password TEXT NOT NULL,
#     email TEXT NOT NULL
# );
# '''
#
# with conn:
#     c.execute(query)
#
# with conn:
#     c.execute('INSERT INTO user VALUES(NULL, "adomas", "123456", "adas@gmail.com")')
#     c.execute('INSERT INTO user(username, password, email) VALUES("Tomas", "Tomas123321", "t@gmail.com")')
#     c.execute('INSERT INTO user(username, password, email) VALUES("Romas", "SuperRomas321!", "romas@gmail.com")')
#
# import sqlite3
#
# conn = sqlite3.connect('task.db')
# c = conn.cursor()
#
# c.execute('''CREATE TABLE admin_users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT NOT NULL UNIQUE,
#     password TEXT NOT NULL,
#     role TEXT DEFAULT 'user'
# );''')
#
# users = [
#     ('admin', 'admin', 'admin'),
#     ('user1', '123', 'user'),
#     ('user2', '321', 'user')
# ]
#
# c.executemany('INSERT INTO admin_users (username, password, role) VALUES (?, ? ,?)', users)
# conn.commit()
#
# c.execute('SELECT * FROM admin_users;')
# res = c.fetchall()
# print(res)
#
# print('--- SQL Injection Atakaos Demonstracija ---')
# inp_username = "' OR True;--"
# inp_password = ''
#
# query = f"SELECT * FROM admin_users WHERE username='{inp_username}' AND password='{inp_password}';"
# print(query)
#
# c.execute(query)
# res = c.fetchall()
#
# print('Result: ', res)
#
# print('--- SQL Injection Atakų Prevencija ---')
# inp_username = "' OR True;--"
# inp_password = ''
#
# query = "SELECT * FROM admin_users WHERE username=? AND password=?"
# print(query)
#
# c.execute(query, (inp_username, inp_password))
# res = c.fetchall()
#
# print(res)
#
#
#
import sqlite3

# Sukurkite duomenų bazės ryšį
conn = sqlite3.connect('task2.db')
c = conn.cursor()

# Sukurkite lentelę Project
create_project_table = """
CREATE TABLE IF NOT EXISTS Project (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    deadline INTEGER NOT NULL
);
"""
with conn:
    c.execute(create_project_table)

# Sukurkite lentelę Task
create_task_table = """
CREATE TABLE IF NOT EXISTS Task (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    project_id INTEGER,
    description TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES Project(id)
);
"""
with conn:
    c.execute(create_task_table)
projects = [
    ('Project A', 10),
    ('Project B', 20),
    ('Project C', 30),
    ('Project D', 40),
    ('Project E', 50)
]

with conn:
    c.executemany("INSERT INTO Project (name, deadline) VALUES (?, ?)", projects)

tasks = [
    (1, 'Task A1', 'Pending'),
    (1, 'Task A2', 'In Progress'),
    (1, 'Task A3', 'Completed'),
    (2, 'Task B1', 'Pending'),
    (2, 'Task B2', 'In Progress'),
    (2, 'Task B3', 'Completed'),
    (3, 'Task C1', 'Pending'),
    (3, 'Task C2', 'In Progress'),
    (3, 'Task C3', 'Completed'),
    (4, 'Task D1', 'Pending'),
    (4, 'Task D2', 'In Progress'),
    (4, 'Task D3', 'Completed'),
    (5, 'Task E1', 'Pending'),
    (5, 'Task E2', 'In Progress'),
    (5, 'Task E3', 'Completed')
]

with conn:
    c.executemany("INSERT INTO Task (project_id, description, status) VALUES (?, ?, ?)", tasks)

def get_tasks_for_project(project_id):
    query = "SELECT * FROM Task WHERE project_id = ?"
    with conn:
        result = c.execute(query, (project_id,)).fetchall()
    return result

tasks_for_project = get_tasks_for_project(1)
for task in tasks_for_project:
    print(task)

def get_projects_with_incomplete_tasks():
    query = """
    SELECT DISTINCT Project.*
    FROM Project
    JOIN Task ON Project.id = Task.project_id
    WHERE Task.status != 'Completed'
    """
    with conn:
        result = c.execute(query).fetchall()
    return result

projects_with_incomplete_tasks = get_projects_with_incomplete_tasks()
for project in projects_with_incomplete_tasks:
    print(project)
