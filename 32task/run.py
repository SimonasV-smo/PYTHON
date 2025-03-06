from app import create_app

# Sukuriame Flask aplikacijos instanciją
app = create_app()

# Patikriname, ar failas paleidžiamas tiesiogiai
if __name__ == '__main__':
    app.run(debug=True)  # Paleidžiame serverį su debug režimu
