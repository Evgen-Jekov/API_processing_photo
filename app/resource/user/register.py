from flask_restful import Resource
from app.models.config_db import db
from app.models.user.user import UserModel
from app.marshmallow.user.user_scheme import UserSchema
from flask import request
from werkzeug.security import generate_password_hash
from marshmallow import ValidationError
from flasgger import swag_from

class UserRegister(Resource):
    @swag_from('doc.yaml')
    def post(self):
        try:
            user_data = UserSchema().load(request.get_json())
        except ValidationError as e:
            return {'erorr validate' : e.messages}, 400

        if UserModel.query.filter(UserModel.email == user_data['email']).first():
            return {'erorr validate' : 'User with this email already exists'}, 400

        try:
            psh = generate_password_hash(password=user_data['password'])

            user = UserModel(
                username=user_data['username'],
                email=user_data['email'],
                password=psh
            )

            tokens = user.create_token()

            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"erorr database" : str(e)}, 500
        
        dump_data = UserSchema().dump(user)

        return {'user_detail' : dump_data, 'token' : tokens}, 201
