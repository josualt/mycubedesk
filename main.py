import os
from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_result():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    if username == 'josu' and password == 'kaka':
        return render_template('succes.html')
    else:
        return render_template('error.html')


@app.route('/aboutme')
def aboutme():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
