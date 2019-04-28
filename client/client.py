# Run with "python client.py"
from bottle import get, run, static_file

@get('/')
def index():
    return static_file('index.html', root=".")

@get('/logged')
def index():
    return static_file('logged.html', root="./static")

@get('/register')
def index():
    return static_file('register.html', root="./static")

@get('/static/<filename>')
def index(filename):
    return static_file(filename, root="./static")

run(reloader=True, host='127.0.0.1', port=5000)