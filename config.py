from os import environ, path
from dotenv import load_dotenv

basedir: str = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class BaseConfig:
    FLASK_APP = 'create_application'
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
