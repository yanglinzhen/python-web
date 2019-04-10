import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DB_URI = os.environ.get('DEV_DB_URI') or 'sqlite:///' + os.path.join(base_dir, 'data-dev.sqlite')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}