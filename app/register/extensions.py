from app.celery.config_celery import celery_client
from app.config import Config

def register_ex(app):
    app.config.from_object(Config)

    celery_client.conf.update(app.config)