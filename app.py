# Load resources and stablish the URL
from flask_restful import Api
from api import create_app
from flask_cors import CORS
from api.controllers.user_controller import Users
from api.controllers.auth_controller import Authorize
from api.controllers.housing_situation_controller import HousingSituationCatalog
from api.controllers.statics_IE_controller import statics_IECatalog

app = create_app('dev')
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

api.add_resource(Users, '/users', '/users/<string:username>')
api.add_resource(Authorize, '/authorize', '/authorize/<string:email>')
api.add_resource(HousingSituationCatalog, '/housing_situations', '/housing_situations/')
api.add_resource(statics_IECatalog, '/Statics','/obtain_static/<string:email>')

if __name__ == '__main__':
    app.run()