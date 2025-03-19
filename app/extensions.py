from app.celery.celery import create_celery

celery_client = create_celery()