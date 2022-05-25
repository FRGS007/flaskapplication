from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    log = False
    return render_template('hello.html', log=log)


@app.route('/signin', methods=['POST', 'GET'])
def logging():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        if login == 'maciekpl' and password == 'haslo123':
            return "<p>Sign in successful!</p>"
    return render_template('signin.html')


if __name__ == '__main__':
    app.run()
