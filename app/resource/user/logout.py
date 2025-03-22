from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from app.redis.config_redis import redis_client, LIFE_TIME


class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']

        redis_client.set(jti, "", ex=LIFE_TIME)
        return {"State" : "logout is succufelly"}, 200