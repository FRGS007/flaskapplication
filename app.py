from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_log():
    log = False
    return render_template('index.html', log=log)


def hello_reg():
    reg = False
    return render_template('index.html', reg=reg)


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
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        return "<p>Registration successful</p>"  # do poprawy
    return render_template('register.html')


@app.route('/post/<int:pid>/<title>')  # pid - post id
def post(pid, title):
    return render_template('post.html', post_id=pid, title=title)


@app.route('/collections')
def posts_collection():
    list = ['x', 'y', 'z']
    dictionary = {'name': 'xyz', 'lastName': 'zyx'}
    return render_template('collections.html', list=list, dictionary=dictionary)


if __name__ == '__main__':
    app.run()
