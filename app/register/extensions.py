from app.celery.config_celery import celery_client
from app.models.config_db import db
from app.jwt.config_jwt import jwt
from app.marshmallow.config_marshmallow import ma
from app.config import Config
from app.models.config_db import migrate
from app.swagger.swagger import swagger
from app.cache.config_cache import cache_client

def register_ex(app):
    app.config.from_object(Config)


    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    swagger.init_app(app)
    migrate.init_app(app, db)
    cache_client.init_app(app)

    celery_client.conf.update(app.config)