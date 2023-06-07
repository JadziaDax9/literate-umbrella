import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '12345' #os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = './test.db' #os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False