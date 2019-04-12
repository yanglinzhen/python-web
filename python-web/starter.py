from app import create_app
from app.models import User

app = create_app('default')
if __name__ == '__main__':
    app.run("localhost", 5000, debug=True)
