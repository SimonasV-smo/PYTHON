from flask import Flask, render_template, request


app = Flask(__name__)

valid_users = ['hello', 'labas', 'ate']

@app.route('/')
def home():
    search_text = request.args.get('paieskoslaukelis')
    search_product = request.args.get('produkto_pavadinimas')
    print(search_text)
    print(search_product)
    return render_template('forma_get.html')


@app.route('/login', methods=['post', 'get'])
def login_user():
    if request.method == 'GET':
        return render_template('forma_post.html')
    elif request.method == 'POST':
        username = request.form.get('loginlaukelis')
        if username in valid_users:
            return render_template('login_result.html', user_login=username)
        else:
            return render_template('forma_post.html')


app.run()

