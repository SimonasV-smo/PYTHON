

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/paieska', methods=['GET'])
def paieska():
    zodis = request.args.get('zodis')
    return render_template('forma_get.html', zodis=zodis)

@app.route('/prisijungti', methods=['POST', 'GET'])
def prisijungti():
    if request.method == 'POST':
        vartotojas = request.form['vardas']
        return f'Prisijungete kaip: {vartotojas}'
    return render_template('forma_post.html')

@app.route('/registracija', methods=['GET', 'POST'])
def registracija():
    pranesimas = None  # Pranešimas vartotojui
    if request.method == 'POST':
        vardas = request.form.get('vardas')
        slaptazodis = request.form.get('slaptazodis')
        pakartotas_slaptazodis = request.form.get('pakartotas_slaptazodis')

        # Validacija
        if not vardas or not slaptazodis or not pakartotas_slaptazodis:
            pranesimas = "Klaida: Užpildykite visus laukus!"
        elif len(slaptazodis) < 6:
            pranesimas = "Klaida: Slaptažodis turi būti bent 6 simbolių ilgio!"
        elif slaptazodis != pakartotas_slaptazodis:
            pranesimas = "Klaida: Slaptažodžiai nesutampa!"
        else:
            pranesimas = f"Sėkmingai užsiregistravote, {vardas}!"

    return render_template('forma_registracija.html', pranesimas=pranesimas)

if __name__ == '__main__':
    app.run(debug=True)
