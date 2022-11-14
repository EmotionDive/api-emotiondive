# Load resources and stablish the URL
from flask_restful import Api
from api import create_app
from flask_cors import CORS
from api.controllers.user_controller import Users, Username
from api.controllers.auth_controller import Authorize
from api.controllers.housing_situation_controller import HousingSituationCatalog

app = create_app('dev')
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

api.add_resource(Users, '/users', '/users/<string:username>')
api.add_resource(Username, '/username_state', '/username_state/<string:username>')
api.add_resource(Authorize, '/authorize', '/authorize/<string:email>')
api.add_resource(HousingSituationCatalog, '/housing_situations')

if __name__ == '__main__':
    app.run()