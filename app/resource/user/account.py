from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user.user import UserModel
from app.marshmallow.user.user_scheme import UserSchema
from app.cache.config_cache import cache_client

class UserAccount(Resource):
    @jwt_required()
    @cache_client.cached()
    def get(self):
        try:
            user = UserModel.query.filter(UserModel.id == get_jwt_identity()).first()

            if not user:
                return {"error" : "user found not"}, 404
        except Exception as e:
            return {"error database" : str(e)}, 500

        user_detail = UserSchema().dump(user)
        return {"username" : user_detail}, 200