# Load resources and stablish the URL
from flask_restful import Api
from api import create_app
from api.controllers.user_controller import Users

app = create_app('dev')
api = Api(app)

api.add_resource(Users, '/Users', '/Users/<string:username>')

if __name__ == '__main__':
    app.run()