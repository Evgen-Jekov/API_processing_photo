from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.models.user.user import UserModel

class UserAccount(Resource):
    @jwt_required()
    def get(self):
        try:
            user = UserModel.query.filter(UserModel.id == get_jwt_identity()).first()

            if not user:
                return {"error" : "user found not"}, 404
        except Exception as e:
            return {"error database" : str(e)}, 500

        return {"username" : user.username}