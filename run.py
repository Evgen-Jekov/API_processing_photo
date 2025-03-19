from flask import Flask
from flask_restful import Api
from app.register.extensions import register_ex
from app.register.register_route import register_route

app = Flask(__name__)
api = Api(app)

register_ex(app)
register_route(api)

if __name__ == "__main__":
    app.run(debug=True)