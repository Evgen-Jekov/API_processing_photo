from flask_restful import Resource
from flask import request
from werkzeug.security import check_password_hash
from app.models.user.user import UserModel
from app.marshmallow.user.user_scheme import UserSchema
from marshmallow import ValidationError

class UserLogin(Resource):
    def post(self):
        try:
            data = UserSchema().load(request.get_json())
            user = UserModel.query.filter(UserModel.email == data['email']).first()
        except ValidationError as e:
            return {'error validate' : e.messages}, 400
        except Exception as e:
            return {"error" : str(e)}, 500

        if not user:
            return {'search error' : 'user not found in the database'}, 404
        
        if check_password_hash(user.password, data['password']):
        
            token = user.create_token()

            return {'token' : token}, 200
        else: 
            return {'error validate' : "password or email is incorrect"}, 401