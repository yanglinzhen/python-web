from . import main

@main.route('/')
def index():
    return '<h1>Hello World!</h1>'

@main.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}</h1>'.format(name)