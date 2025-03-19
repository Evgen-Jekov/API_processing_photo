from app.extensions import celery_client

@celery_client.task
def number(num):
    return num