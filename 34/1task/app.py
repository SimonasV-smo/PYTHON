from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Staliukas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numeris = db.Column(db.Integer, nullable=False, unique=True)
    vietu_skaicius = db.Column(db.Integer, nullable=False)
    uzsakymai = db.relationship('Uzsakymas', backref='staliukas', cascade='all, delete-orphan')


class Uzsakymas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aprasymas = db.Column(db.String, nullable=False)
    kaina = db.Column(db.Float, nullable=False)
    staliukas_id = db.Column(db.Integer, db.ForeignKey('staliukas.id'), nullable=False)

@app.route('/')
def index():
    staliukai = Staliukas.query.all()
    return render_template('index.html', staliukai=staliukai)

@app.route('/staliukas/<int:id>')
def staliukas(id):
    staliukas = Staliukas.query.get(id)
    return render_template('staliukas.html', staliukas=staliukas)

@app.route('/add-staliukas', methods=['POST'])
def add_staliukas():
    numeris = request.form['numeris']
    vietu_skaicius = int(request.form['vietu_skaicius'])
    new_staliukas = Staliukas(numeris=numeris, vietu_skaicius=vietu_skaicius)
    db.session.add(new_staliukas)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add-uzsakymas/<int:staliukas_id>', methods=['POST'])
def add_uzsakymas(staliukas_id):
    aprasymas = request.form['aprasymas']
    kaina = request.form['kaina']
    new_usakymas = Uzsakymas(aprasymas=aprasymas, kaina=kaina, staliukas_id=staliukas_id)
    db.session.add(new_usakymas)
    db.session.commit()
    return redirect(url_for('staliukas', id=staliukas_id))

@app.route('/delete-staliukas/<int:id>', methods=['POST'])
def delete_staliukas(id):
    staliukas = Staliukas.query.get(id)
    if staliukas.uzsakymai:
        return 'Negalima istrinti'
    else:
        db.session.delete(staliukas)
        db.session.commit()
    return redirect(url_for('index'))

with app.app_context():
    db.create_all()

app.run()


