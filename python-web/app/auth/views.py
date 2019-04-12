from . import auth

@auth.route('/login')
def login():
    return '<h1>Please input your username and password</h1>'