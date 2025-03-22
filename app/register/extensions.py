from app.celery.config_celery import celery_client
from app.models.config_db import db
from app.jwt.config_jwt import jwt
from app.marshmallow.config_marshmallow import ma
from app.config import Config
from app.models.config_db import migrate
from app.swagger.swagger import swagger
from app.celery.config_redis import redis_client

def register_ex(app):
    app.config.from_object(Config)


    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    swagger.init_app(app)
    migrate.init_app(app, db)
    redis_client.init_app(app)

    celery_client.conf.update(app.config)