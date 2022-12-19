from flask import request
from flask_restful import Resource
from ..services.mail_service import *

class TokenVerification(Resource):
    """
    Resource to verify the token send in a verification email
    """
    def post(self):
        verification_code = request.json.get("code", None)
        return verify_token(verification_code)