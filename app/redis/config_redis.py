from redis import Redis
from app.jwt.config_jwt import jwt
from datetime import timedelta

redis_client = Redis(
    host="localhost", 
    port=6379, 
    db=0, 
    decode_responses=True
)

LIFE_TIME = timedelta(hours=5)

@jwt.token_in_blocklist_loader
def black_list(jwt_header, jwt_payload: dict):
    jti = jwt_payload['jti']
    token_in_redis = redis_client.get(jti)
    return token_in_redis is not None