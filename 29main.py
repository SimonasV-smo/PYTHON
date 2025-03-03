from flask import Flask

app = Flask(__name__)



@app.route('/')
def home():
    return 'Hello World from my first FLASK webApp!!!\nHOMEPAGE'

@app.route('/news')
def news():
    return 'Cia pagrindinis naujienu puslapis'

@app.route('/news/<int:item>')
def news_item(item):
    return f'Cia naujiena NR {item}'

@app.route('/<text>')
def any_route(text):
    return f'jus surinkote marsruta {text} jokio resurso cia nera '


app.run()