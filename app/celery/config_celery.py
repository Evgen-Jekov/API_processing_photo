from celery import Celery
from app.config import Config

celery_client = Celery(
    __name__,
    broker=Config.CELERY_BROKER_URL,
    backend=Config.CELERY_RESULT_BACKEND,
    include=['app.celery.tasks']
)