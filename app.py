from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def helloLog():
    log = False
    return render_template('hello.html', log=log)

def helloReg():
    reg = False
    return render_template('hello.html', reg=reg)


@app.route('/signin', methods=['POST', 'GET'])
def logging():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        if login == 'login' and password == 'pass':
            return "<p>Login successful!</p>"
    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        return "<p>Registration successful</p>" #nie dziala
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
