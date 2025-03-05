
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Projektas(db.Model):
    __tablename__ = 'projektas'

    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String)
    kaina = db.Column(db.Float)
    sukurimo_data = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, pavadinimas, kaina):
        self.pavadinimas = pavadinimas
        self.kaina = kaina

    def __repr__(self):
        return f'{self.id} {self.pavadinimas} {self.kaina} {self.sukurimo_data}'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_rows = Projektas.query.all()
    return render_template('index.html', projektas_rows=all_rows)


app.run()
