# importing libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_cors import CORS
from flask_redmail import RedMail

from .config import config_by_name

db = SQLAlchemy()
ma = Marshmallow()
email = RedMail()

def create_app(config_name='dev') -> Flask:
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    ma.init_app(app)
    api_rest = Api(app) # instantiate of the api class
    cors = CORS(app, resources={r"/*": {"origins": "*"}}) # configuration of CORS
    email.init_app(app) # instantiate of the redmail class

    # importing classes
    from api.controllers.user_controller import Users, Username
    from api.controllers.auth_controller import Authorize
    from api.controllers.mail_controller import MailVerification
    from api.controllers.housing_situation_controller import HousingSituationCatalog

    # endpoints of the API
    api_rest.add_resource(Users, '/users', '/users/<string:username>')
    api_rest.add_resource(
        Username, 
        '/verification/username_state', 
        '/verification/username_state/<string:username>'
    )
    api_rest.add_resource(
        MailVerification, 
        '/verification/verify_mail', 
        '/verification/verify_mail/<string:username>'
    )
    api_rest.add_resource(Authorize, '/authorize', '/authorize/<string:email>')
    api_rest.add_resource(HousingSituationCatalog, '/housing_situations')

    return app