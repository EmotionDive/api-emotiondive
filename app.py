# Load resources and stablish the URL
from flask_restful import Api
from api import create_app
from api.controllers.user_controller import Users
from api.controllers.auth_controller import Authorize

app = create_app('dev')
api = Api(app)

api.add_resource(Users, '/users', '/users/<string:username>')
api.add_resource(Authorize, '/authorize', '/authorize/<string:email>')

if __name__ == '__main__':
    app.run()