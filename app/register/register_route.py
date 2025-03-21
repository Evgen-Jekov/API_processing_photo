from app.resource.user.register import UserRegister

def register_route(api):
    api.add_resource(UserRegister, '/register')