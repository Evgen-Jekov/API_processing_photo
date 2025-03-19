from app.extensions import celery_client
from app import create_app

app = create_app()
celery_client.conf.update(app.config)