from celery import Celery

celery_client = Celery(__name__, broker='redis://localhost:6379/0', include=['app.tasks.tasks'])