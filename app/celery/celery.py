from celery import Celery
from app.config import Config

def create_celery(app=None):
    app_name = app.import_name if app else "default_app_name"
    
    celery_client = Celery(
        app_name,
        broker=Config.CELERY_BROKER_URL,
        backend=Config.CELERY_RESULT_BACKEND,
        include=['app.celery.tasks']
    )

    if app:
        celery_client.conf.update(app.config)

    return celery_client