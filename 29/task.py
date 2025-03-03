
# 1. Pagrindiniai maršrutai ir dinaminių parametrų naudojimas

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Sveiki atvykę į Flask aplikaciją!'

@app.route('/apie')
def apie():
    return 'Tai yra apie mus puslapis.'

@app.route('/vartotojas/<vardas>')
def vartotojas(vardas):
    return f'Sveiki, {vardas}!'

@app.route('/skaicius/<int:nr>')
def skaicius(nr):
    return f'Jūs įvedėte skaičių: {nr}'

# papildoma

@app.route('/kelione/<start>/<end>')
def kelione(start, end):
    return f'Kelionės maršrutas: iš {start} į {end}'

app.run()