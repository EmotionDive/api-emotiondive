import os
from flask import Flask
from flask_restful import Api

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Load resources and stablish the URL
    from api.resources.user import User
    api.add_resource(User, '/User', '/User/<string:username>')

    return app