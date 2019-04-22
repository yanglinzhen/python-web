from . import main
import app
from flask import send_from_directory

@main.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}</h1>'.format(name)

@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def catch_all(path):
    return send_from_directory(app.static_file_dir, 'index.html')