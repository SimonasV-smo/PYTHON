from flask import Flask

app = Flask(__name__)



# @app.route('/')
# def home():
#     return 'Hello World from my first FLASK webApp!!!\nHOMEPAGE'
#
# @app.route('/news')
# def news():
#     return 'Cia pagrindinis naujienu puslapis'
#
# @app.route('/news/<int:item>')
# def news_item(item):
#     return f'Cia naujiena NR {item}'
#
# @app.route('/<text>')
# def any_route(text):
#     return f'jus surinkote marsruta {text} jokio resurso cia nera '


@app.route('/')
def home():
    return '<h1>Homepage</h1><p>Hello World!!</p><p>This is my firs Flask app!!</p>'\
           '<p><a href="verslas">Pereiti i verslo skyriu</a></p>'\
            '<p><a href="/verslas/nekilnojamas-turtas">Pereiti i NT poskyri</a></p>'

@app.route('/verslas')
def verslas():
    return '<h1>Verslo skyrius</h1><p>Verslo naujienos</p>'\
            '<p><a href="/">Gryzti i pradini</a></p>'\
            '<p><a href="/verslas/nekilnojamas-turtas">Pereiti i NT poskyri</a></p>'

@app.route('/verslas/nekilnojamas-turtas')
def verslas_nt():
    return '<h1>Verslo skyrius</h1><h2>NT poskyris</h2>' \
           '<p><a href="/">Gryzti i pradini</a></p>'\
            '<p><a href="/">Gryzti i verslo skyrius</a></p>'

app.run()