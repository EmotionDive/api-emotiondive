from flask import request
from flask_restful import Resource
from ..services.auth_service import *

class Authorize(Resource):
    """
    Resource to authorize an user account action using auth0
    """
    def get(self, email):
        response_obj = get_auth_flags(email) 
        return response_obj