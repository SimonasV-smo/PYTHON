
# 1. Pagrindiniai maršrutai ir dinaminių parametrų naudojimas

from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Sveiki atvykę į Flask aplikaciją!'
#
# @app.route('/apie')
# def apie():
#     return 'Tai yra apie mus puslapis.'
#
# @app.route('/vartotojas/<vardas>')
# def vartotojas(vardas):
#     return f'Sveiki, {vardas}!'
#
# @app.route('/skaicius/<int:nr>')
# def skaicius(nr):
#     return f'Jūs įvedėte skaičių: {nr}'
#
# # papildoma
#
# @app.route('/kelione/<start>/<end>')
# def kelione(start, end):
#     return f'Kelionės maršrutas: iš {start} į {end}'

# 2. HTML atsakymas ir nuorodos tarp puslapių

@app.route('/')
def home():
    return 'Sveiki atvykę į Flask aplikaciją!' \
           '<p><a href="/pagrindinis">Pradzia</a></p>'

@app.route('/pagrindinis')
def pagrindinis():
    return '<h1>Mano Flask puslapis</h1>'\
            '<p><h2>Tai yra pagrindinis puslapis</h2></p>'\
            '<p><a href="/apie">Apie mus</a></p>' \
           '<p><a href="/vartotojas/Simonas ir/27">Vartotojas</a></p>'

@app.route('/apie')
def apie():
    return 'Tai yra apie mus puslapis.'\
            '<p><a href="/pagrindinis">Pagrindinis puslapis</a></p>'\
            '<p><a href="/vartotojas/Simonas ir/27">Vartotojas</a></p>'
# papildoma

@app.route('/vartotojas/<vardas> ir/<int:nr>')
def vartotojas(vardas, nr):
    return f'<p>Vartotojas: <b>{vardas}</b></p>'\
            f'<p>Amzius: <b>{nr}</b></p>' \
           '<p><a href="/pagrindinis">Pagrindinis puslapis</a></p>'


app.run()