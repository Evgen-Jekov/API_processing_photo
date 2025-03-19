from app.extensions import celery_client
from app.config import Config
from flask import Flask
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    api = Api(app)

    celery_client.conf.update(app.config)

    return app