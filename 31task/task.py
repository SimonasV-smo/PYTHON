from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mokiniai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Mokiniai(db.Model):
    __tablename__ = 'mokiniai'

    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String)
    pavarde = db.Column(db.String)
    klase = db.Column(db.String)
    sukurimo_data = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, vardas, pavarde, klase):
        self.vardas = vardas
        self.pavarde = pavarde
        self.klase = klase

    def __repr__(self):
        return f'{self.id} {self.vardas} {self.pavarde} {self.klase} {self.sukurimo_data}'

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        vardas = request.form['vardas']
        pavarde = request.form['pavarde']
        klase = request.form['klase']
        new_mokinys = Mokiniai(vardas, pavarde, klase)
        db.session.add(new_mokinys)
        db.session.commit()
        return redirect(url_for('home'))
    all_rows = Mokiniai.query.all()
    return render_template('task.html', mokiniai_rows=all_rows)

@app.route('/delete/<int:id>')
def delete(id):
    mokinys = Mokiniai.query.get_or_404(id)
    db.session.delete(mokinys)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
