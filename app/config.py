import os

class Config:
    CELERY_BROKER_URL = os.getenv('REDIS')
    CELERY_RESULT_BACKEND = os.getenv('REDIS')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQL_POSTGRE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
    'title': 'API for work with picture',
    'uiversion': 3,
    'specs_route': '/apidocs/'
    }