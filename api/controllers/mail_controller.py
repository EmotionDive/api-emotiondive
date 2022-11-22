from flask import request
from flask_restful import Resource
from ..services.mail_service import *

class MailVerification(Resource):
    """
    Resource to verify an user's account
    """
    def get(self, email):
        return send_mail(email)
        
    def post(self, email):
        verification_code = request.json["code"]
        return verify_token(email, verification_code)