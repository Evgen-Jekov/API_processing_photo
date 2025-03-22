import os
from datetime import timedelta

class Config:
    CELERY_BROKER_URL = os.getenv('REDIS')
    CELERY_RESULT_BACKEND = os.getenv('REDIS')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQL_POSTGRE')
    JWT_SECRET_KEY = os.getenv('JWT')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=10)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
    'title': 'API for work with picture',
    'uiversion': 3,
    'specs_route': '/apidocs/'
    }